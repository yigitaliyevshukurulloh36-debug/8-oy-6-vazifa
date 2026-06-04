from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField


class Course(models.Model):
    name = models.CharField(max_length=255, verbose_name='Kurs nomi')
    price = models.DecimalField(max_digits=10, decimal_places=2,
                                validators=[MinValueValidator(0, message="Narxni 0 dan katta kiritishingiz kerak !!!")],
                                verbose_name="Narx")
    duration = models.IntegerField(validators=[MinValueValidator(0, message="0 dan katta raqam kiriting")],
                                   verbose_name="Davomiyligi")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kurs"
        verbose_name_plural = "Kurslar"


class Student(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nomi")
    age = models.IntegerField(validators=[MinValueValidator(7, message="Yoshi 7 dan  oshganlar uchun !!!"),
                                          MaxValueValidator(50, message="50 yoshgacha olinadi !!!")],
                              verbose_name="Yosh")
    image = models.ImageField(upload_to='Students_image/', null=True, blank=True, verbose_name="Rasmi")
    address = models.CharField(max_length=255, verbose_name='Manzil 📍')
    mark = models.IntegerField(validators=[
        MinValueValidator(0 , message="Eng kichik ball 0 yoki undan katta bo'lishi kerak "),
        MaxValueValidator(100, message="Eng yuqori ball 100 gavha bo'lishi kerak ")
    ], verbose_name="Baho")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="students", verbose_name="Kursi")
    phone = PhoneNumberField(region='UZ', unique=True, help_text="Namuna: +998901234567", error_messages={
        'invalid': "Iltimos raqamni namunadagidek kiriting !!!",
        'null': "Raqam kiritish shart !!! ",
        'unique': "Bu raqam orqali LOGIN mavjud !!!",
    }, verbose_name="TEL ☎️")
    email = models.EmailField(max_length=255, unique=True, null=True, help_text='Namuna misol@gmail.com',
                              error_messages={
                                  'invalid': "Iltimos raqamni namunadagidek kiriting !!!",
                                  'unique': "Bu raqam orqali LOGIN qilingan !!!",
                              }, verbose_name="Email 📧")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Talaba"
        verbose_name_plural = "Talabalar"


class Teacher(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nomi")
    age = models.IntegerField(validators=[MinValueValidator(20, message="Yoshi 20 dan  oshganlar uchun !!!"),
                                          MaxValueValidator(60, message="60 yoshgacha olinadi !!!")],
                              verbose_name="Yosh")
    image = models.ImageField(upload_to='Teachers_image/', null=True, blank=True, verbose_name="Rasmi")  
    skill = models.CharField(max_length=255, verbose_name="Tajriba")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="teachers", verbose_name="Kursi")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "O'qituvchi"
        verbose_name_plural = "O'qituvchilar"

class Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="payments", verbose_name="Talaba")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Summa")
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name="To'lov sanasi")

    def __str__(self):
        return f"{self.student.name} - {self.amount}"
    
    class Meta:
        verbose_name = "To'lov"
        verbose_name_plural = "To'lovlar"


