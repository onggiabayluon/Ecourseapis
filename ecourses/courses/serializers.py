from rest_framework import serializers

from .models import Category, Course


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, course):
        request = self.context['request']
        name = course.image.name

        if name.startswith("static/"):
            path = '/%s' % name
        else:
            path = '/static/%s' % name

        return request.build_absolute_uri(path)

    class Meta:
        model = Course
        fields = ["id", "subject", "created_date", "category", "image"]
