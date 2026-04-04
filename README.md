# Django Inventory Management System (DRF)

A Django REST Framework-based inventory management system with Excel file upload, product approval workflow, and comprehensive API endpoints.

---

## 📋 Features Overview

### 1. Upload Excel & Manage Drafts
Upload Excel files with product data and manage draft products before approval.

![Upload Excel & Manage Drafts](https://github.com/Raihanroo/Django_Exam/raw/main/screenshots/01-upload-page.png)

**Features:**
- Choose and upload Excel files
- Automatic data parsing and validation
- Products stored as "Draft" status initially
- Blue "Upload Excel" button for submission
- Green "View Approved Products" button for navigation

---

### 2. Draft Products List
View all uploaded products in a table format with approval workflow.

![Draft Products List](https://github.com/Raihanroo/Django_Exam/raw/main/screenshots/02-draft-products.png)

**Features:**
- Table with columns: Product ID, Name, Category, Price, Quantity, Last Updated, Action
- Products sorted by Product ID in ascending order (1, 2, 3... 10)
- Yellow "Approve" button for each product
- Success message notification when product is approved
- Real-time table updates

---

### 3. Product Approval
Approve products to move them from Draft to Approved status.

![Product Approval](https://github.com/Raihanroo/Django_Exam/raw/main/screenshots/03-approval-success.png)

**Features:**
- Green success notification: "Product approved successfully!"
- Remaining draft products continue to display
- Approved products move to the Approved Products list
- Seamless workflow transition

---

### 4. Approved Products List
View all approved products with search and delete functionality.

![Approved Products List](https://github.com/Raihanroo/Django_Exam/raw/main/screenshots/04-approved-products.png)

**Features:**
- Complete list of all approved products
- Yellow "Delete" button for each product
- "Back to Upload" button for navigation
- Search field for filtering by name or category
- Black "Search" button for submission
- Ascending order by Product ID

---

### 5. Delete Confirmation Dialog
Confirmation dialog before deleting products.

![Delete Confirmation](https://github.com/Raihanroo/Django_Exam/raw/main/screenshots/05-delete-confirmation.png)

**Features:**
- Modal dialog with confirmation message
- "Are you sure you want to delete this product?"
- Yellow "OK" button to confirm deletion
- Green "Cancel" button to abort deletion
- Prevents accidental deletions

---

### 6. Search & Filter
Search approved products by name or category.

![Search & Filter](https://github.com/Raihanroo/Django_Exam/raw/main/screenshots/06-search-results.png)

**Features:**
- Real-time search functionality
- Filter by product name or category
- Instant results display
- Search field with placeholder text
- Black "Search" button

---

## 🛠️ Technology Stack

| Component | Technology |
|-----------|-----------|
| Backend | Django 5.2.1 |
| API Framework | Django REST Framework 3.14.0 |
| Database | PostgreSQL (Neon) |
| Frontend | Bootstrap 5.3.0 |
| File Processing | Pandas 2.2.2, OpenPyXL 3.1.2 |
| Deployment | Vercel |
| Server | Gunicorn 21.2.0 |

---

## 📁 Project Structure

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

---

## 📊 Data Model

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

---

## 🔌 API Endpoints

### Product Management
- **GET** `/api/products/` - List all products
- **POST** `/api/products/` - Create a new product
- **GET** `/api/products/{id}/` - Get product details
- **PUT** `/api/products/{id}/` - Update product
- **DELETE** `/api/products/{id}/` - Delete product

### Excel Upload
- **POST** `/api/products/upload_excel/`
  - Form data: `excel_file` (multipart/form-data)
  - Response: `{"message": "Successfully processed X products"}`

### Workflow Actions
- **POST** `/api/products/{id}/approve/` - Approve a product
- **GET** `/api/products/drafts/` - Get all draft products
- **GET** `/api/products/approved/` - Get all approved products

### Query Parameters
- `?status=Draft` or `?status=Approved` - Filter by status
- `?search=keyword` - Search by name or category
- `?page=1` - Pagination (100 items per page)

---

## 📄 Excel File Format

### Required Columns
Your Excel file should contain these columns:

| Column | Description | Example |
|--------|-------------|---------|
| product_id | Unique product identifier | 1, 2, 3... |
| name | Product name | Wireless Headphones |
| category | Product category | Electronics |
| price | Product price | 2500.00 |
| quantity | Stock quantity | 50 |

### Supported Column Name Variations
The system automatically detects column names:

- **product_id**: productid, product id, id, product
- **name**: product_name, productname, title
- **category**: cat, type, product_type
- **price**: cost, amount, unit_price
- **quantity**: qty, stock, quantity_in_stock

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.11+
- pip (Python package manager)
- Git

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

---

## 🌐 Deployment

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

---

## 📖 Usage Workflow

### Step 1: Upload Excel File
1. Go to the dashboard
2. Click "Choose File" and select your Excel file
3. Click "Upload Excel" button
4. Products will appear in the Draft Products table

### Step 2: Review Draft Products
1. View all uploaded products in the table
2. Check product details (ID, Name, Category, Price, Quantity)
3. Products are sorted by Product ID in ascending order (1, 2, 3... 10)

### Step 3: Approve Products
1. Click the yellow "Approve" button for each product
2. Product status changes from "Draft" to "Approved"
3. Success notification appears
4. Product moves to the Approved Products list

### Step 4: View Approved Products
1. Click the green "View Approved Products" button
2. See all approved products in a separate table
3. Use search to filter by name or category

### Step 5: Delete Products (Optional)
1. In Approved Products list, click the yellow "Delete" button
2. Confirmation dialog will appear
3. Click "OK" to confirm deletion
4. Product will be removed from the system

---

## 💻 Example API Requests

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

---

## ✨ Key Features Implemented

✅ Excel file upload with flexible column mapping
✅ Automatic data validation and error handling
✅ Draft and Approved product workflow
✅ RESTful API with Django REST Framework
✅ Search and filter functionality
✅ Pagination support (100 items per page)
✅ Product deletion with confirmation dialog
✅ Responsive Bootstrap UI
✅ Vercel deployment ready
✅ No static files required (inline CSS/JS)
✅ Real-time notifications
✅ Ascending order sorting by Product ID

---

## 🌍 Browser Compatibility

- ✅ Chrome/Edge (Latest)
- ✅ Firefox (Latest)
- ✅ Safari (Latest)
- ✅ Mobile browsers

---

## ⚡ Performance

- **Upload Speed:** Optimized for large Excel files
- **Pagination:** 100 products per page
- **Search:** Real-time filtering
- **Database:** PostgreSQL with connection pooling
- **Response Time:** < 500ms for most operations

---

## 🔮 Future Enhancements

- User authentication and authorization
- Product image upload
- Bulk operations (approve/delete multiple)
- Export to Excel
- Advanced filtering and sorting
- Product history/audit log
- Email notifications
- Role-based access control
- Product categories management

---

## 📝 License

This project is open source and available under the MIT License.

---

## 🤝 Support

For issues or questions, please create an issue on GitHub:
https://github.com/Raihanroo/Django_Exam/issues

---

## 🎯 Live Demo

**URL:** https://django-exam.vercel.app/

Try the application live and test all features!

---

**Created by:** Raihan  
**Last Updated:** April 2026  
**Version:** 2.0 (DRF)
