from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserViewSet, CategoryViewSet, SubcategoryViewSet, ProblemViewSet, SubmissionViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'subcategories', SubcategoryViewSet, basename='subcategory')
router.register(r'problems', ProblemViewSet, basename='problem')
router.register(r'submissions', SubmissionViewSet, basename='submission')


urlpatterns = [    
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='get_token'),    #POST
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh'), #POST
]
