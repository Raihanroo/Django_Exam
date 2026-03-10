# Django_Exam
#Django Practical Exam – File Upload, Draft Approval & Approved Products
I created the project and shared the image here from the beginning level 
<img width="1035" height="368" alt="image" src="https://github.com/user-attachments/assets/4bcee7eb-e6e6-4ac8-a6fc-ed80e65ade4e" />

This is a simple table which I created, and if you see it on the table, there are file options then name is chose fiele after clicking chose file take excel file from my destop   the  click the uploadExcel button , then the senario will be lick this 

 <img width="1041" height="754" alt="image" src="https://github.com/user-attachments/assets/c3d08d54-aeb8-45b4-b3f9-cea9e5e8ba61" />
when i click approved all like this 
<img width="1072" height="643" alt="image" src="https://github.com/user-attachments/assets/500e7431-fa5b-4352-ad63-99d0a19cad47" />

When I click the View Approved Products green button, the picture will be like this

<img width="1188" height="782" alt="image" src="https://github.com/user-attachments/assets/bad03f14-e48f-482c-8acf-ca4afcd5c92a" />

Then search the category name in a search field and click the bluck search button, the picture will be like this 

<img width="1528" height="452" alt="image" src="https://github.com/user-attachments/assets/aabb9376-1814-431e-b795-34593980dedb" />


This is the main scenario of Django Practical Exam – File Upload, Draft Approval & Approved Products

What the project does (based on the code)
1) Landing page
When you open the site, you land on a simple page with two buttons:

View Approved Products
Draft & Upload
This comes from:

views.landing() → renders templates/landing.html
Route:

/ (home)
2) Draft & Upload (Excel import + approve/edit)
This is the “work” page of the project.

You can:

Upload an .xlsx file
Django reads the rows using openpyxl
Each row becomes a Product with status Draft
If a product ID already exists, it skips it and shows a message
Then it shows a table of all Draft products with:

Edit button (change name/category/price/quantity)
Approve button (moves status from Draft → Approved)
Routes:

/draftupload/ → upload + list drafts
/approve/<product_id>/ → approve a draft product (POST)
/edit/<product_id>/ → edit a draft product (GET/POST)
Main logic is in:

practical/views.py (draft_upload, approve_product, edit_product)
3) Approved Products (search + filter + pagination)
This page lists only products with status Approved.

It supports:

Search by name or category
Filter by date range using the product’s last_updated
Choose results per page (5 / 10 / 20)
Pagination
Route:

/approvedproducts/
Main logic is in:

practical/views.py (approved_products)
Data model
There is only one model:

Product (in practical/models.py)
Fields:

product_id (AutoField primary key)
name (unique)
category
price (Decimal)
quantity (Integer)
last_updated (auto updated every save)
status (Draft or Approved)
Project structure (important files)
manage.py — Django command runner
practical/settings.py — settings (SQLite database, templates folder configured)
practical/urls.py — URL routes for the project
practical/views.py — all app logic (upload, approve, edit, filters)
practical/models.py — Product model
templates/ — HTML pages:
landing.html
draftupload.html
approvedproducts.html
edit_product.html
How to run it locally
1) Create and activate a virtual environment (recommended)
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate
2) Install dependencies
This repo doesn’t include a requirements.txt, but based on the imports you will need at least:

Django
openpyxl
Install:

pip install django openpyxl
3) Run migrations
python manage.py makemigrations
python manage.py migrate
4) Start the server
python manage.py runserver
Then open:

http://127.0.0.1:8000/
Excel file format (what the upload expects)
The code reads from row 2 (so row 1 is header).

It expects the first 5 columns to be:

product_id
name
category
price
quantity
Only .xlsx is accepted.

Notes / small limitations I noticed
ALLOWED_HOSTS = [] so this is meant for local development.
The repo currently doesn’t have a dependency file (requirements.txt), so installation is manual.
Approving a product is done through a POST request, which is good (it avoids approving by just visiting a link).

