from django.core.management.base import BaseCommand
from pub_priv_school_ls.models import School  # Replace with your model

class Command(BaseCommand):
    help = 'round all instances of School'
    

    def handle(self, *args, **kwargs):
        for schools in School.objects.all():
            schools.kindergarten = round(schools.kindergarten)
            schools.kindergarten_male = round(schools.kindergarten_male)
            schools.kindergarten_female = round(schools.kindergarten_female)
            
            schools.first_grade = round(schools.first_grade)
            schools.first_grade_male = round(schools.first_grade_male)
            schools.first_grade_female = round(schools.first_grade_female)
            
            schools.second_grade = round(schools.second_grade)
            schools.second_grade_male = round(schools.second_grade_male)
            schools.second_grade_female = round(schools.second_grade_female)
            
            schools.third_grade = round(schools.third_grade)
            schools.third_grade_male = round(schools.third_grade_male)
            schools.third_grade_female = round(schools.third_grade_female)
            
            schools.fourth_grade = round(schools.fourth_grade)
            schools.fourth_grade_male = round(schools.fourth_grade_male)
            schools.fourth_grade_female = round(schools.fourth_grade_female)
            
            schools.fifth_grade = round(schools.fifth_grade)
            schools.fifth_grade_male = round(schools.fifth_grade_male)
            schools.fifth_grade_female = round(schools.fifth_grade_female)
            
            schools.sixth_grade = round(schools.sixth_grade)
            schools.sixth_grade_male = round(schools.sixth_grade_male)
            schools.sixth_grade_female = round(schools.sixth_grade_female)
            
            schools.seventh_grade = round(schools.seventh_grade)
            schools.seventh_grade_male = round(schools.seventh_grade_male)
            schools.seventh_grade_female = round(schools.seventh_grade_female)
            
            schools.eighth_grade = round(schools.eighth_grade)
            schools.eighth_grade_male = round(schools.eighth_grade_male)
            schools.eighth_grade_female = round(schools.eighth_grade_female)
            schools.save()
            
        self.stdout.write(self.style.SUCCESS('Successfully rounded all instances of School'))