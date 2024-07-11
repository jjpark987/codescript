from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, CategoryViewSet, SubcategoryViewSet, ProblemViewSet, ExampleViewSet, SubmissionViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'subcategories', SubcategoryViewSet, basename='subcategory')
router.register(r'problems', ProblemViewSet, basename='problem')
router.register(r'examples', ExampleViewSet, basename='example')
router.register(r'submissions', SubmissionViewSet, basename='submission')

urlpatterns = [    
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='get_token'),    #POST
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh'), #POST
]
