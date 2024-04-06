from django.urls import path
from product.views import ProductBuyView, ProductListView, ProductCreateView, ProductDetailView, ProductUpdateView, ProductDeleteView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('<int:pk>/detail/', ProductDetailView.as_view(), name='product_detail'),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('<int:pk>/buy/', ProductBuyView.as_view(), name='product_buy'),
]
