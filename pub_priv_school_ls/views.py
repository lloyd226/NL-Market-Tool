from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import InputData
from .distance_calc import calculate_distance
from .models import School
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    #this code is run after inputs are submitted which saves the input data
    places = ['Ak','AL','AR','AZ','CA','CO','CT','DC','DE','FL','GA','HI','IA','ID','IL',
              'IN','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH',
              'NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT',
              'VT','VA','WA','WV','WI','WY']
    return render(request, "pub_priv_school_ls/index.html", {"places": places})

def area(request, loc):
    if request.method == "POST":
        form = InputData(request.POST)
        if form.is_valid():
            input_longitude = form.cleaned_data["input_longitude"]
            input_latitude = form.cleaned_data["input_latitude"]
            radius = form.cleaned_data["radius"]
            #updates distance for all the schools
            all_schools = School.objects.filter(state__contains=loc)
            for schools in all_schools:
                schools.distance = round(calculate_distance(float(input_latitude), float(input_longitude), float(schools.latitude), float(schools.longitude)), 2)
                schools.save()
            return redirect(reverse("pub_priv_school_ls:list", args=[radius,float(input_latitude), float(input_longitude), loc]))
    else:
        #creates empty form to be filled out
        form = InputData()
        
    places = ['Ak','AL','AR','AZ','CA','CO','CT','DC','DE','FL','GA','HI','IA','ID','IL',
              'IN','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH',
              'NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT',
              'VT','VA','WA','WV','WI','WY']
    
    return render(request, "pub_priv_school_ls/state.html", {"form": form, 'loc':loc, 'places':places})
    
def list(request, radius, latitude, longitude, loc):
    #for the new location button
    if request.method == "POST":
        return redirect(reverse("pub_priv_school_ls:index"))
    
    #creates all the context which are then used in html request
    local_schools = School.objects.filter(state__contains=loc).filter(distance__lt=float(radius)).order_by("distance")
    num_schools = local_schools.count()
    int_schools(local_schools)
    
    #get context for totals for male students    
    total_kindergarten_m = sum(schools.kindergarten_male for schools in local_schools)
    total_first_m = sum(schools.first_grade_male for schools in local_schools)
    total_second_m = sum(schools.second_grade_male for schools in local_schools)
    total_third_m = sum(schools.third_grade_male for schools in local_schools)
    total_fourth_m = sum(schools.fourth_grade_male for schools in local_schools)
    total_fifth_m = sum(schools.fifth_grade_male for schools in local_schools)
    total_sixth_m = sum(schools.sixth_grade_male for schools in local_schools)
    total_seventh_m = sum(schools.seventh_grade_male for schools in local_schools)
    total_eighth_m = sum(schools.eighth_grade_male for schools in local_schools)
    
    adressable_market_m = total_kindergarten_m + total_first_m + total_second_m + total_third_m + total_fourth_m + total_fifth_m + total_sixth_m + total_seventh_m + total_eighth_m
    
    #get context for female students
    total_kindergarten_f = sum(schools.kindergarten_female for schools in local_schools)
    total_first_f = sum(schools.first_grade_female for schools in local_schools)
    total_second_f = sum(schools.second_grade_female for schools in local_schools)
    total_third_f = sum(schools.third_grade_female for schools in local_schools)
    total_fourth_f = sum(schools.fourth_grade_female for schools in local_schools)
    total_fifth_f = sum(schools.fifth_grade_female for schools in local_schools)
    total_sixth_f = sum(schools.sixth_grade_female for schools in local_schools)
    total_seventh_f = sum(schools.seventh_grade_female for schools in local_schools)
    total_eighth_f = sum(schools.eighth_grade_female for schools in local_schools)
    
    adressable_market_f = total_kindergarten_f + total_first_f + total_second_f + total_third_f + total_fourth_f+ total_fifth_f + total_sixth_f + total_seventh_f + total_eighth_f
    
    #get context for demographics 
    total_hisp = sum(schools.hispanic_students for schools in local_schools)
    total_whi = sum(schools.white_students for schools in local_schools)
    total_black = sum(schools.black_students for schools in local_schools)
    total_asian = sum(schools.asian_students for schools in local_schools)
    total_hawi = sum(schools.hawaiian_students for schools in local_schools)
    total_native = sum(schools.native_students for schools in local_schools)
    total_multi = sum(schools.multi_race_students for schools in local_schools)
    
    data = [total_hisp,total_whi,total_black,total_asian,total_hawi,total_native,total_multi]
    context = {"local_schools": local_schools, "latitude":latitude, "longitude":longitude,
        "num_schools": num_schools,
        "total_kindergarten_m": total_kindergarten_m, 
        "total_first_m": total_first_m,
        "total_second_m": total_second_m,
        "total_third_m": total_third_m,
        "total_fourth_m": total_fourth_m,
        "total_fifth_m": total_fifth_m,
        "total_sixth_m": total_sixth_m,
        "total_seventh_m": total_seventh_m,
        "total_eighth_m": total_eighth_m,
        "adressable_market_m": adressable_market_m,
        "total_kindergarten_f": total_kindergarten_f, 
        "total_first_f": total_first_f,
        "total_second_f": total_second_f,
        "total_third_f": total_third_f,
        "total_fourth_f": total_fourth_f,
        "total_fifth_f": total_fifth_f,
        "total_sixth_f": total_sixth_f,
        "total_seventh_f": total_seventh_f,
        "total_eighth_f": total_eighth_f,
        "adressable_market_f": adressable_market_f,
        "data": data,
        }
    
    return render(request, "pub_priv_school_ls/list.html", context)

def int_schools(local_schools):
    for schools in local_schools:
        schools.kindergarten = int(schools.kindergarten)
        schools.kindergarten_male = int(schools.kindergarten_male)
        schools.kindergarten_female = int(schools.kindergarten_female)
            
        schools.first_grade = int(schools.first_grade)
        schools.first_grade_male = int(schools.first_grade_male)
        schools.first_grade_female = int(schools.first_grade_female)
            
        schools.second_grade = int(schools.second_grade)
        schools.second_grade_male = int(schools.second_grade_male)
        schools.second_grade_female = int(schools.second_grade_female)
            
        schools.third_grade = int(schools.third_grade)
        schools.third_grade_male = int(schools.third_grade_male)
        schools.third_grade_female = int(schools.third_grade_female)
            
        schools.fourth_grade = int(schools.fourth_grade)
        schools.fourth_grade_male = int(schools.fourth_grade_male)
        schools.fourth_grade_female = int(schools.fourth_grade_female)
            
        schools.fifth_grade = int(schools.fifth_grade)
        schools.fifth_grade_male = int(schools.fifth_grade_male)
        schools.fifth_grade_female = int(schools.fifth_grade_female)
            
        schools.sixth_grade = int(schools.sixth_grade)
        schools.sixth_grade_male = int(schools.sixth_grade_male)
        schools.sixth_grade_female = int(schools.sixth_grade_female)
            
        schools.seventh_grade = int(schools.seventh_grade)
        schools.seventh_grade_male = int(schools.seventh_grade_male)
        schools.seventh_grade_female = int(schools.seventh_grade_female)
            
        schools.eighth_grade = int(schools.eighth_grade)
        schools.eighth_grade_male = int(schools.eighth_grade_male)
        schools.eighth_grade_female = int(schools.eighth_grade_female)
