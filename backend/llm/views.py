from rest_framework import viewsets, mixins, permissions
from rest_framework_simplejwt import authentication
from .models import Response
from .serializers import ResponseSerializer

class ResponseViewSet(
        viewsets.GenericViewSet,
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        mixins.CreateModelMixin,
        mixins.DestroyModelMixin,):
    serializer_class = ResponseSerializer
    authentication_classes = [authentication.JWTAuthentication]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Response.objects.all()
        return Response.objects.filter(user=user)
    
    def get_permissions(self):
        if self.action == 'destroy':
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]
