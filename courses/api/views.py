from rest_framework import generics
from ..models import Subject, Course, Content
from .serializers import SubjectSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .serializers import CourseSerializer
from .permissions import IsEnrolled
from .serializers import CourseWithContentsSerializer
from rest_framework.decorators import action

API_HOME_DICT = {
    "intro": "this is a set of API endpoints I built for my SkillNG app incase in furture I want to convert the app to a react app, its endpoints are as shown below",
    "Endpoints": {"subjects/": "To retrieve all the subjects/categories in the database",
                  'subjects/<pk>/': "to retrieve a particular subject/category",
                  'courses/<pk>/enroll/': "to enroll a user for a course",
                  'courses/': "to retrieve all available courses",
                  'courses/<pk>/': "to retrieve a particular course",
                  'courses/<pk>/contents/': "to retrieve contents of a particular course",
                  }
}


class APIHomeView(APIView):
    queryset = Course.objects.all()

    def get(self, request):
        return Response(API_HOME_DICT)


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(detail=True, methods=['get'],
            serializer_class=CourseWithContentsSerializer,
            authentication_classes=[BasicAuthentication],
            permission_classes=[IsAuthenticated, IsEnrolled])
    def contents(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class CourseEnrollView(APIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, pk, format=None):
        course = get_object_or_404(Course, pk=pk)
        course.students.add(request.user)
        return Response({'enrolled': True})


class SubjectListView (generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetailView (generics.RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
