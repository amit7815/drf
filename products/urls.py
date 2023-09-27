from django.urls import path

from . import views 

urlpatterns = [
    path('', views.product_list_create_view),
    path('<int:pk>/', views.product_detail_view)  # here pk is actual field name
    # path('', views.product_alt_view),
    # path('<int:pk>/', views.product_alt_view)
]
