from django.urls import path
from . import views

urlpatterns = [
    path("", views.upload_and_drafts, name="upload_and_drafts"),
    path("approve/<int:pk>/", views.approve_product, name="approve_product"),
    path("approved/", views.approved_products, name="approved_products"),
    path("docs/", views.api_documentation, name="api_documentation"),
]
