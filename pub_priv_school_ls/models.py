from django.db import models

# Create your models here.

class School(models.Model):
    distance = models.FloatField(default=-1.0)
    school_name = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=10, decimal_places=7)
    longitude = models.DecimalField(max_digits=10, decimal_places=7)
    school_type = models.CharField(max_length=200, default='a')
    state = models.CharField(max_length=5, default='a')
    adress = models.CharField(max_length=200, default='a')
    school_zip = models.IntegerField(default=0)
    
    kindergarten = models.FloatField(default=-1.0)
    first_grade = models.FloatField(default=-1.0)
    second_grade = models.FloatField(default=-1.0)
    third_grade = models.FloatField(default=-1.0)
    fourth_grade = models.FloatField(default=-1.0)
    fifth_grade = models.FloatField(default=-1.0)
    sixth_grade = models.FloatField(default=-1.0)
    seventh_grade = models.FloatField(default=-1.0)
    eighth_grade = models.FloatField(default=-1.0)
    
    kindergarten_male = models.FloatField(default=-1.0)
    first_grade_male = models.FloatField(default=-1.0)
    second_grade_male = models.FloatField(default=-1.0)
    third_grade_male = models.FloatField(default=-1.0)
    fourth_grade_male = models.FloatField(default=-1.0)
    fifth_grade_male = models.FloatField(default=-1.0)
    sixth_grade_male = models.FloatField(default=-1.0)
    seventh_grade_male = models.FloatField(default=-1.0)
    eighth_grade_male = models.FloatField(default=-1.0)
    
    kindergarten_female = models.FloatField(default=-1.0)
    first_grade_female = models.FloatField(default=-1.0)
    second_grade_female = models.FloatField(default=-1.0)
    third_grade_female = models.FloatField(default=-1.0)
    fourth_grade_female = models.FloatField(default=-1.0)
    fifth_grade_female = models.FloatField(default=-1.0)
    sixth_grade_female = models.FloatField(default=-1.0)
    seventh_grade_female = models.FloatField(default=-1.0)
    eighth_grade_female = models.FloatField(default=-1.0)
    
    hispanic_students = models.IntegerField(default=-1)
    white_students = models.IntegerField(default=-1)
    black_students = models.IntegerField(default=-1)
    asian_students = models.IntegerField(default=-1)
    hawaiian_students = models.IntegerField(default=-1)
    native_students = models.IntegerField(default=-1)
    multi_race_students = models.IntegerField(default=-1)
    
    
    def __str__(self):
        return self.school_name
    