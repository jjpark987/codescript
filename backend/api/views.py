from rest_framework import viewsets, permissions
from rest_framework_simplejwt import authentication
from django.contrib.auth.models import User
from .models import Category, Subcategory, Problem, Submission
from .serializers import UserSerializer, CategorySerializer, SubcategorySerializer, ProblemSerializer, SubmissionSerializer

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    authentication_classes = [authentication.JWTAuthentication]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return User.objects.all()
        return User.objects.filter(id=user.id)

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]
    
class BaseViewSet(viewsets.ModelViewSet):
    authentication_classes = [authentication.JWTAuthentication]

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]
    
class CategoryViewSet(BaseViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SubcategoryViewSet(BaseViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer

class ProblemViewSet(BaseViewSet):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer

class SubmissionViewSet(viewsets.ModelViewSet):
    authentication_classes = [authentication.JWTAuthentication]
    serializer_class = SubmissionSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Submission.objects.all()
        return Submission.objects.filter(user=user)
    
    def get_permissions(self):
        if self.action == 'destroy':
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]
