"""
URL configuration for inventory_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def api_root(request):
    return Response({
        'message': 'Inventory System API',
        'endpoints': {
            'products': '/api/products/',
            'upload_excel': '/api/products/upload_excel/',
            'drafts': '/api/products/drafts/',
            'approved': '/api/products/approved/',
        }
    })

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', api_root, name='api-root'),
    path('', include('products.urls'))
]
