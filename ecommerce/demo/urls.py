from django.urls import path
from . import views
app_name = 'demo'
urlpatterns = [
    path('', views.cetegories, name='categories'),
    path('products/<slug:category>/', views.products, name='product_by_category'),
   path("product/<slug:slug>/", views.product_detail, name="product_detail"),
]