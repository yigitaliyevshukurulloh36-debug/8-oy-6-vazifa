from rest_framework import serializers
from .models import Course, Student, Teacher, Payment



class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    course_write = serializers.ChoiceField(
        choices=Course.objects.all(), write_only=True,
    )


    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'address', 'mark', 'phone', 'email', 'course', 'course_write']
        depth = 1  

    
    def create(self, validated_data):
        course_write = validated_data.pop("course_write")
        student = Student.objects.create(course=course_write, **validated_data)
        student.save()
        return student

    def update(self, instance, validated_data):
        instance.course =  validated_data.pop("course_write") or instance.course
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
    
class StudentAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'  
        depth = 1

class TeacherSerializer(serializers.ModelSerializer):
    course_write = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(), write_only=True, source='course'
    )
    class Meta:
        model = Teacher
        fields = ['id', 'name', 'age', 'image', 'skill', 'course', 'course_write']
        depth = 1

class PaymentSerializer(serializers.ModelSerializer):
    payment_write = serializers.ChoiceField(
        choices=Student.objects.all(), write_only=True,
    )

    class Meta:
        model = Payment
        fields = ['id', 'student', 'payment_write', 'amount', 'payment_date']
        depth = 1

        

    def create(self, validated_data):
        payment_write = validated_data.pop("payment_write")
        student = Student.objects.create(payment=payment_write, **validated_data)
        student.save()
        return student
    




    def update(self, instance, validated_data):
        instance.payment = validated_data.pop("payment_write") or instance.payment
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
            