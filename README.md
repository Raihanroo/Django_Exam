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

Django Inventory System API Summary
This is a simple Django-based inventory management system with 3 main APIs:

1. Upload & Draft List API
URL: / (root)
View Function: upload_and_drafts()
Method: GET and POST
Functionality:
GET: Displays all products with "Draft" status, paginated (10 per page)
POST: Accepts an Excel file (.xlsx) upload, reads product data (product_id, name, category, price, quantity), and creates/updates products with status="Draft"
2. Approve Product API
URL: /approve/<int:pk>/
View Function: approve_product()
Method: POST (or GET redirect)
Functionality: Changes a product's status from "Draft" to "Approved" based on the primary key (pk)
3. Approved Products List API
URL: /approved/
View Function: approved_products()
Method: GET
Functionality: Displays all products with "Approved" status. Supports search query (?q=) to filter by name or category. Paginated (10 per page).
Data Model: Product
Field	Type	Description
product_id	IntegerField (unique)	Unique product identifier
name	CharField(255)	Product name
category	CharField(100)	Product category
price	DecimalField	Product price
quantity	IntegerField	Stock quantity
last_updated	DateTimeField	Auto-updated timestamp
status	CharField	"Draft" or "Approved"
URL Routing
All routes are under the root path /:

/ → upload_and_drafts
/approve/<pk>/ → approve_product
/approved/ → approved_products



