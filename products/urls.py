from django.urls import path
from . import views

urlpatterns=[
    path('', views.products,name="products"),
    path('<int:pro_id>', views.productt,name="product"),
    path('search', views.search,name="search"),
]


