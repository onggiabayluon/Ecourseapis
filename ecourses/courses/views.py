from rest_framework import viewsets, generics

from .serializers import CategorySerializer

from .models import Category


class CategoryViewSet(viewsets.ModelViewSet, generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = [permissions.IsAuthenticated]
