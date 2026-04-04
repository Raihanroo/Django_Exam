import pandas as pd
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import render
from django.db.models import Q
from .models import Product
from .serializers import ProductSerializer


def _normalize_columns(df):
    """Normalize column names to lowercase and strip whitespace"""
    df.columns = df.columns.str.lower().str.strip()
    return df


def _get_column_mapping(df):
    """Create flexible column mapping for various Excel formats"""
    columns = set(df.columns)
    
    mappings = {
        "product_id": ["product_id", "productid", "product id", "id", "product"],
        "name": ["name", "product_name", "productname", "title"],
        "category": ["category", "cat", "type", "product_type"],
        "price": ["price", "cost", "amount", "unit_price"],
        "quantity": ["quantity", "qty", "stock", "quantity_in_stock"],
    }
    
    result = {}
    for key, variations in mappings.items():
        for var in variations:
            if var in columns:
                result[key] = var
                break
        if key not in result:
            raise ValueError(f"Could not find column for '{key}'. Available columns: {', '.join(columns)}")
    
    return result


def _process_excel_row(row, column_map):
    """Extract and validate data from Excel row"""
    try:
        return {
            "product_id": str(row[column_map["product_id"]]).strip(),
            "name": str(row[column_map["name"]]).strip(),
            "category": str(row[column_map["category"]]).strip(),
            "price": float(row[column_map["price"]]),
            "quantity": int(row[column_map["quantity"]]),
            "status": "Draft",
        }
    except (ValueError, KeyError) as e:
        raise ValueError(f"Invalid data in row: {str(e)}")


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    parser_classes = (MultiPartParser, FormParser)
    search_fields = ["name", "category"]

    def get_queryset(self):
        queryset = Product.objects.all()
        status_filter = self.request.query_params.get("status")
        search = self.request.query_params.get("search")
        
        if status_filter:
            queryset = queryset.filter(status=status_filter)
        
        if search:
            queryset = queryset.filter(
                Q(name__icontains=search) | Q(category__icontains=search)
            )
        
        return queryset.order_by("product_id")

    @action(detail=False, methods=["post"], parser_classes=(MultiPartParser, FormParser))
    def upload_excel(self, request):
        """Upload products from Excel file"""
        file = request.FILES.get("excel_file")
        
        if not file:
            return Response(
                {"error": "No file provided"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            df = pd.read_excel(file)
            
            if df.empty:
                raise ValueError("Excel file is empty")
            
            df = _normalize_columns(df)
            column_map = _get_column_mapping(df)
            
            created_count = 0
            for idx, row in df.iterrows():
                data = _process_excel_row(row, column_map)
                Product.objects.update_or_create(
                    product_id=data["product_id"],
                    defaults={
                        "name": data["name"],
                        "category": data["category"],
                        "price": data["price"],
                        "quantity": data["quantity"],
                        "status": data["status"],
                    },
                )
                created_count += 1
            
            return Response(
                {"message": f"Successfully processed {created_count} products"},
                status=status.HTTP_201_CREATED
            )
        
        except ValueError as e:
            return Response(
                {"error": f"Validation Error: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {"error": f"Error: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST
            )

    @action(detail=True, methods=["post"])
    def approve(self, request, pk=None):
        """Approve a product"""
        product = self.get_object()
        product.status = "Approved"
        product.save()
        serializer = self.get_serializer(product)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def drafts(self, request):
        """Get all draft products"""
        drafts = self.get_queryset().filter(status="Draft")
        page = self.paginate_queryset(drafts)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = self.get_serializer(drafts, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def approved(self, request):
        """Get all approved products"""
        approved = self.get_queryset().filter(status="Approved")
        page = self.paginate_queryset(approved)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = self.get_serializer(approved, many=True)
        return Response(serializer.data)


def dashboard(request):
    """Render dashboard UI"""
    return render(request, 'dashboard.html')
