from django.urls import path

from . import views 

urlpatterns = [
    path('', views.product_list_create_view),
    # path('', views.product_mixin_view),
    path('<int:pk>/update/', views.product_update_view),
    path('<int:pk>/destroy/', views.product_delete_view),
    path('<int:pk>/', views.product_detail_view)
    # path('<int:pk>/', views.product_mixin_view)  # here pk is actual field name
    # path('', views.product_alt_view),
    # path('<int:pk>/', views.product_alt_view)
]
