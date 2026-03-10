import pandas as pd
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Product
from django.db.models import Q


def upload_and_drafts(request):
    if request.method == "POST" and request.FILES.get("excel_file"):
        file = request.FILES["excel_file"]
        try:
            df = pd.read_excel(file)
            for _, row in df.iterrows():
                Product.objects.update_or_create(
                    product_id=row["product_id"],
                    defaults={
                        "name": row["name"],
                        "category": row["category"],
                        "price": row["price"],
                        "quantity": row["quantity"],
                        "status": "Draft",
                    },
                )
            messages.success(request, "Excel uploaded successfully!")
        except Exception as e:
            messages.error(request, f"Error: {e}")
        return redirect("upload_and_drafts")

    draft_list = Product.objects.filter(status="Draft").order_by("-last_updated")
    paginator = Paginator(draft_list, 10)
    page_obj = paginator.get_page(request.GET.get("page"))
    return render(request, "products/drafts.html", {"page_obj": page_obj})


def approve_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.status = "Approved"
    product.save()
    messages.success(request, f"Product {product.product_id} approved!")
    return redirect("upload_and_drafts")


def approved_products(request):
    query = request.GET.get("q", "")
    products = Product.objects.filter(status="Approved").order_by("-last_updated")
    if query:
        products = products.filter(
            Q(name__icontains=query) | Q(category__icontains=query)
        )

    paginator = Paginator(products, 10)
    page_obj = paginator.get_page(request.GET.get("page"))
    return render(request, "products/approved.html", {"page_obj": page_obj})
