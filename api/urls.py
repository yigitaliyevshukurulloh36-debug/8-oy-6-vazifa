from django.urls import path
from .views import (CourseAPIView, CourseRetrieveAPIView, StudentAPIView, 
                    StudentRetrieveAPIView, TeacherAPIView, TeacherRetrieveAPIView,
                    PaymentAPIView, PaymentRetrieveAPIView)

urlpatterns = [
    path('courses/', CourseAPIView.as_view()),
    path('courses/<int:pk>/', CourseRetrieveAPIView.as_view()),

    path('students/', StudentAPIView.as_view()),
    path('students/<int:pk>/', StudentRetrieveAPIView.as_view()),

    path('teachers/', TeacherAPIView.as_view()),
    path('teachers/<int:pk>/', TeacherRetrieveAPIView.as_view()),

    path('payments/', PaymentAPIView.as_view()),
    path('payments/<int:pk>/', PaymentRetrieveAPIView.as_view()),
]