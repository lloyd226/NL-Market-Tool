import pandas as pd
from django.core.management.base import BaseCommand
from pub_priv_school_ls.models import School

class Command(BaseCommand):
    help = 'Import info from an Excel file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='The path to the Excel file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        try:
            # Read the Excel file
            df = pd.read_excel(file_path)
            
            print("Colomns in excel file:", df.columns.tolist())

            # Iterate over the rows and create Record objects
            for index, row in df.iterrows():
                record = School(
                    distance=row["Distance"],
                    school_name=row['School Name'],
                    latitude=row['Latitude'],
                    longitude=row['Longitude'],
                    school_type=row["School Type"],
                    state=row["State"],
                    adress=row["Adress"],
                    school_zip=row["Zip"],
                    kindergarten=row["Kindergarten"],
                    first_grade=row["First Grade"],
                    second_grade=row["Second Grade"],
                    third_grade=row["Third Grade"],
                    fourth_grade =row["Fourth Grade"],
                    fifth_grade=row["Fifth Grade"],
                    sixth_grade =row["Sixth Grade"],
                    seventh_grade =row["Seventh Grade"],
                    eighth_grade =row["Eighth Grade "],
                    kindergarten_male =row["Kindergarten Male"],
                    first_grade_male =row["First Grade Male"],
                    second_grade_male =row["Second Grade Male"],
                    third_grade_male =row["Third Grade Male"],
                    fourth_grade_male =row["Fourth Grade Male"],
                    fifth_grade_male =row["Fifth Grade Male"],
                    sixth_grade_male =row["Sixth Grade Male"],
                    seventh_grade_male =row["Seventh Grade Male"],
                    eighth_grade_male =row["Eighth Grade Male"],
                    kindergarten_female =row["Kindergarten Female"],
                    first_grade_female =row["First Grade Female"],
                    second_grade_female =row["Second Grade Female"],
                    third_grade_female =row["Third Grade Female"],
                    fourth_grade_female =row["Fourth Grade Female"],
                    fifth_grade_female=row["Fifth Grade Female"],
                    sixth_grade_female =row["Sixth Grade Female"],
                    seventh_grade_female =row["Seventh Grade Female"],
                    eighth_grade_female =row["Eighth Grade Female"],
                    hispanic_students =row["Hispanic Students"],
                    white_students =row["White Students"],
                    black_students =row["Black Students"],
                    asian_students =row["Asian Students"],
                    hawaiian_students =row["Hawaiian Students"],
                    native_students =row["Native Students"],
                    multi_race_students =row["Multi-Race Students"]
                )
                record.save()
            
            self.stdout.write(self.style.SUCCESS('Successfully imported info'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))