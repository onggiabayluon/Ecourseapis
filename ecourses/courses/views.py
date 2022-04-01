from rest_framework import viewsets, generics

from .serializers import CategorySerializer, CourseSerializer

from .models import Category, Course

from .paginators import BasePagination


class CategoryViewSet(viewsets.ModelViewSet, generics.ListAPIView):
    """
    API endpoint that allows Category to be viewed
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = [permissions.IsAuthenticated]


class CourseViewSet(viewsets.ModelViewSet, generics.ListAPIView):
    """
    API endpoint that allows courses to be viewed
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = BasePagination

    def get_queryset(self):
        courses = Course.objects.filter(active=True)

        q = self.request.query_params.get('q')
        if q is not None:
            courses = courses.filter(subject__icontains=q)
            
        category_id = self.request.query_params.get('category_id')
        if category_id is not None:
            courses = courses.filter(category_id=category_id)
            
        return courses
