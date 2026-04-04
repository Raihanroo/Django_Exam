# Django Inventory Management System (DRF)

## Project Overview
A Django REST Framework-based inventory management system with Excel file upload, product approval workflow, and comprehensive API endpoints.

## Features

### 1. **Upload Excel & Manage Drafts**
- Upload Excel files with product data
- Automatic data parsing and validation
- Products stored as "Draft" status initially
- Table view with ascending order by Product ID
- Approve button to move products to approved status

**Screenshot - Initial Upload Page:**
![Upload Page](https://github.com/Raihanroo/Django_Exam/raw/main/screenshots/1-upload-page.png)

### 2. **Draft Products Management**
- View all draft products in a table format
- Columns: Product ID, Name, Category, Price, Quantity, Last Updated, Action
- Approve button to move product to approved status
- Products sorted by Product ID (ascending: 1, 2, 3... 10)

**Screenshot - Draft Products with Data:**
![Draft Products](https://github.com/Raihanroo/Django_Exam/raw/main/screenshots/2-draft-products.png)

### 3. **Product Approval**
- Click "Approve" button to move product from Draft to Approved
- Success message displayed
- Product automatically removed from Draft list
- Remaining draft products continue to display

**Screenshot - After Approval:**
![After Approval](https://github.com/Raihanroo/Django_Exam/raw/main/screenshots/3-after-approval.png)

### 4. **Approved Products List**
- View all approved products
- Search functionality by name or category
- Delete button (yellow) to remove products
- Confirmation dialog before deletion
- "Back to Upload" button to return to draft management

**Screenshot - Approved Products:**
![Approved Products](https://github.com/Raihanroo/Django_Exam/raw/main/screenshots/4-approved-products.png)

### 5. **Delete Confirmation**
- Click delete button to trigger confirmation dialog
- Dialog asks "Are you sure you want to delete this product?"
- OK button to confirm deletion
- Cancel button to abort deletion

**Screenshot - Delete Confirmation:**
![Delete Confirmation](https://github.com/Raihanroo/Django_Exam/raw/main/screenshots/5-delete-confirmation.png)

### 6. **Search & Filter**
- Search approved products by name or category
- Real-time filtering as you type
- Black search button for clarity
- Shows only matching products

**Screenshot - Search Results:**
![Search Results](https://github.com/Raihanroo/Django_Exam/raw/main/screenshots/6-search-results.png)

## Technology Stack

- **Backend:** Django 5.2.1
- **API Framework:** Django REST Framework 3.14.0
- **Database:** PostgreSQL (via Neon)
- **Frontend:** Bootstrap 5.3.0 (Inline CSS/JS)
- **File Processing:** Pandas 2.2.2, OpenPyXL 3.1.2
- **Deployment:** Vercel

## Project Structure

```
Django_Exam/
├── inventory_system/          # Main project settings
│   ├── settings.py           # Django configuration
│   ├── urls.py               # URL routing
│   ├── wsgi.py               # WSGI application
│   └── asgi.py               # ASGI application
├── products/                  # Main app
│   ├── models.py             # Product model
│   ├── views.py              # ViewSets and API views
│   ├── serializers.py        # DRF serializers
│   ├── urls.py               # App URL routing
│   └── migrations/           # Database migrations
├── templates/
│   └── dashboard.html        # Main UI dashboard
├── manage.py                 # Django management
├── requirements.txt          # Python dependencies
├── vercel.json              # Vercel deployment config
└── build_files.sh           # Build script

```

## Data Model

### Product Model
| Field | Type | Description |
|-------|------|-------------|
| id | AutoField | Primary key |
| product_id | IntegerField (unique) | Unique product identifier |
| name | CharField(255) | Product name |
| category | CharField(100) | Product category |
| price | DecimalField | Product price |
| quantity | IntegerField | Stock quantity |
| status | CharField | "Draft" or "Approved" |
| last_updated | DateTimeField | Auto-updated timestamp |

## API Endpoints

### 1. **Product List & Create**
- **GET** `/api/products/` - List all products
- **POST** `/api/products/` - Create a new product

### 2. **Product Detail**
- **GET** `/api/products/{id}/` - Get product details
- **PUT** `/api/products/{id}/` - Update product
- **DELETE** `/api/products/{id}/` - Delete product

### 3. **Upload Excel**
- **POST** `/api/products/upload_excel/`
  - Form data: `excel_file` (multipart/form-data)
  - Response: `{"message": "Successfully processed X products"}`

### 4. **Approve Product**
- **POST** `/api/products/{id}/approve/`
  - Changes product status to "Approved"

### 5. **Filter Endpoints**
- **GET** `/api/products/drafts/` - Get all draft products
- **GET** `/api/products/approved/` - Get all approved products

### 6. **Query Parameters**
- `?status=Draft` or `?status=Approved` - Filter by status
- `?search=keyword` - Search by name or category
- `?page=1` - Pagination (100 items per page)

## Excel File Format

Required columns in Excel file:
- `product_id` - Unique product identifier
- `name` - Product name
- `category` - Product category
- `price` - Product price
- `quantity` - Stock quantity

**Supported column name variations:**
- product_id: productid, product id, id, product
- name: product_name, productname, title
- category: cat, type, product_type
- price: cost, amount, unit_price
- quantity: qty, stock, quantity_in_stock

## Installation & Setup

### Local Development

1. **Clone the repository**
```bash
git clone https://github.com/Raihanroo/Django_Exam.git
cd Django_Exam
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run migrations**
```bash
python manage.py migrate
```

5. **Start development server**
```bash
python manage.py runserver
```

6. **Access the application**
```
http://localhost:8000/
```

## Deployment

### Vercel Deployment

The project is configured for Vercel deployment:

1. **Push to GitHub**
```bash
git add .
git commit -m "Your message"
git push origin main
```

2. **Connect to Vercel**
   - Go to https://vercel.com
   - Import your GitHub repository
   - Set environment variables (if needed)
   - Deploy

3. **Live URL**
```
https://django-exam.vercel.app/
```

## Usage Workflow

### Step 1: Upload Excel File
1. Go to the dashboard
2. Click "Choose File" and select your Excel file
3. Click "Upload Excel" button
4. Products will appear in the Draft Products table

### Step 2: Review Draft Products
1. View all uploaded products in the table
2. Check product details (ID, Name, Category, Price, Quantity)
3. Products are sorted by Product ID in ascending order

### Step 3: Approve Products
1. Click "Approve" button for each product you want to approve
2. Product status changes from "Draft" to "Approved"
3. Product moves to the Approved Products list

### Step 4: View Approved Products
1. Click "View Approved Products" button
2. See all approved products in a separate table
3. Use search to filter by name or category

### Step 5: Delete Products (Optional)
1. In Approved Products list, click the yellow "Delete" button
2. Confirmation dialog will appear
3. Click "OK" to confirm deletion
4. Product will be removed from the system

## Example API Requests

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

### Search Approved Products
```bash
curl "http://localhost:8000/api/products/approved/?search=laptop"
```

### Delete Product
```bash
curl -X DELETE http://localhost:8000/api/products/1/
```

## Key Features Implemented

✅ Excel file upload with flexible column mapping
✅ Automatic data validation and error handling
✅ Draft and Approved product workflow
✅ RESTful API with DRF
✅ Search and filter functionality
✅ Pagination support (100 items per page)
✅ Product deletion with confirmation
✅ Responsive Bootstrap UI
✅ Vercel deployment ready
✅ No static files required (inline CSS/JS)

## Browser Compatibility

- Chrome/Edge (Latest)
- Firefox (Latest)
- Safari (Latest)
- Mobile browsers

## Performance

- **Upload Speed:** Optimized for large Excel files
- **Pagination:** 100 products per page
- **Search:** Real-time filtering
- **Database:** PostgreSQL with connection pooling

## Future Enhancements

- User authentication and authorization
- Product image upload
- Bulk operations (approve/delete multiple)
- Export to Excel
- Advanced filtering and sorting
- Product history/audit log
- Email notifications

## License

This project is open source and available under the MIT License.

## Support

For issues or questions, please create an issue on GitHub:
https://github.com/Raihanroo/Django_Exam/issues

## Live Demo

**URL:** https://django-exam.vercel.app/

---

**Created by:** Raihan
**Last Updated:** April 2026
