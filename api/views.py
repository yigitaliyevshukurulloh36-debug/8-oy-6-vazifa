from rest_framework import status
from rest_framework.generics import get_object_or_404, ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView

from .srializers import (CourseSerializer, StudentSerializer, StudentAdminSerializer, 
                         TeacherSerializer, PaymentSerializer)
from .models import Course, Student, Teacher, Payment
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated

class StudentAPIView(ListCreateAPIView):
    queryset = Student.objects.all()
    
    def get_serializer_class(self):
        if self.request.user and self.request.user.is_staff: 
            return StudentAdminSerializer
        return StudentSerializer  
    
    def get_queryset(self):
        queryset = Student.objects.all()
        mark = self.request.query_params.get('mark')
        course = self.request.query_params.get('course')
        if mark:
            queryset = queryset.filter(mark=mark)
        if course:
            queryset = queryset.filter(course_id=course)
        return queryset


class StudentRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    
    def get_serializer_class(self):
        if self.request.user and self.request.user.is_staff:
            return StudentAdminSerializer
        return StudentSerializer

class CourseAPIView(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer



class TeacherAPIView(ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    def get_queryset(self):
        queryset = Teacher.objects.all()
        course = self.request.query_params.get('course')
        if course:
            queryset = queryset.filter(course_id=course)
        return queryset

class TeacherRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class PaymentAPIView(ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class PaymentRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer