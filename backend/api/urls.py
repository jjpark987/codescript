from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .models import Category, Subcategory, Problem, Submission

router = DefaultRouter()
# router.register(r'users', UserViewSet, basename='user')
# router.register(r'search-queries', SearchQueryViewSet, basename='search-query')
# router.register(r'products', ProductViewSet, basename='product')
# router.register(r'reviews', ReviewViewSet, basename='review')


urlpatterns = [    
    path('token/', TokenObtainPairView.as_view(), name='get_token'),    # POST
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh'),  # POST
]
