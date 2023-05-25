from django.urls import path

from . import views 

# /api/products/
urlpatterns = [
    path('', views.ProductListCreateApiView.as_view(), name='create_product'),
    path('list/', views.ProductMixinView.as_view()),
    path('<int:pk>/', views.ProductDetailApiView.as_view()),
    path('<int:pk>/update/', views.ProductUpdateApiView.as_view(), name='product-edit'),
    path('<int:pk>/delete/', views.ProductDestroyApiView.as_view()),
    # path('<int:pk>/', views.product_detail_view, name='product-detail')
]