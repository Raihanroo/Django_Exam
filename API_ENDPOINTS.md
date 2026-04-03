# Inventory System API Endpoints

## Setup
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## API Endpoints

### Products List & Create
- **GET** `/api/products/` - List all products
- **POST** `/api/products/` - Create a new product

### Product Detail
- **GET** `/api/products/{id}/` - Get product details
- **PUT** `/api/products/{id}/` - Update product
- **DELETE** `/api/products/{id}/` - Delete product

### Upload Excel
- **POST** `/api/products/upload_excel/`
  - Form data: `excel_file` (multipart/form-data)
  - Response: `{"message": "Successfully processed X products"}`

### Approve Product
- **POST** `/api/products/{id}/approve/`
  - Changes product status to "Approved"

### Filter Endpoints
- **GET** `/api/products/drafts/` - Get all draft products
- **GET** `/api/products/approved/` - Get all approved products

### Query Parameters
- `?status=Draft` or `?status=Approved` - Filter by status
- `?search=keyword` - Search by name or category
- `?page=1` - Pagination (10 items per page)

## Example Requests

### Upload Excel
```bash
curl -X POST http://localhost:8000/api/products/upload_excel/ \
  -F "excel_file=@products.xlsx"
```

### Get Draft Products
```bash
curl http://localhost:8000/api/products/drafts/
```

### Approve Product
```bash
curl -X POST http://localhost:8000/api/products/1/approve/
```

### Search Products
```bash
curl "http://localhost:8000/api/products/?search=laptop&status=Approved"
```
