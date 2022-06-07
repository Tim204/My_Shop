from django.urls import path
from .import views

app_name ='shop'

urlpatterns =[
    path('', views.index, name='index'),
    path('product/', views.product_list, name='product_list'),
    path('search/', views.SearchResulView.as_view(), name='search_results'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]