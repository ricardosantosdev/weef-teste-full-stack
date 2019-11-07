from django.db import models
from pyUFbr.baseuf import ufbr
from django.utils import timezone


class Course(models.Model):
    name = models.CharField(max_length=40, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Courses"

class Instructor(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    cpf = models.CharField(max_length=14, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Instructors"

class Class(models.Model):

    STATE_CHOICES = [(_, _) for _ in ufbr.list_uf]

    course = models.ForeignKey(Course, null=True, blank=True, on_delete=models.CASCADE)
    date_request = models.DateTimeField("Solicitação", default=timezone.now)
    course_type = models.CharField("Tipo de curso", max_length=24, null=False, blank=False)
    start_date = models.DateField("Data de início")
    end_date = models.DateField("Data do fim")
    cep = models.CharField("CEP", max_length=9, null=False, blank=False)
    state = models.CharField("Estado", max_length=2, choices=STATE_CHOICES, default='SP')
    city = models.CharField("Cidade", max_length=24, null=False, blank=False)
    students = models.IntegerField("Estudantes", default=1, null=False, blank=False)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name_plural = "Classes"


