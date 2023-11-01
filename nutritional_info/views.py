from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import receipes
from django.core.paginator import Paginator
from django.views.decorators.http import require_POST, require_GET


# Create your views here.

class global_vars:
    """
    Global variables
    """
    #We use this variable to store data for a longer time
    data_post_form = {}

class GetInfos(TemplateView):
    template_name = 'index.html'


@require_POST
def post_form(request):
    if request.method =='POST':
        #Process gender checkboxes
        gender = str(request.POST.get('gender'))
        height = int(request.POST.get('height'))
        weight = int(request.POST.get('weight'))
        age = int(request.POST.get('age'))
        goal = int(request.POST.get('activity_level'))


        """
        Calculate TMB
        """
        if gender == 'male':
            TMB = 66.5+(13.75*weight)+(5.003*height)-(6.755*age)

        if gender == 'female':
            TMB = 665.1+(9.563*weight)+(1.850*height)-(4.676*age)
        
        """
        Calculate gain, mantain or lose weight
        """
        GAIN_WEIGHT = 400
        LOSE_WEIGHT = -400
        MANTAIN_WEIGHT = 0

        if goal == 1:
            #lose weight
            calories_per_day = TMB + LOSE_WEIGHT

        elif goal == 2:
            #gain weight
            calories_per_day = TMB + GAIN_WEIGHT

        elif goal == 3:
            calories_per_day = TMB + MANTAIN_WEIGHT

        else:
            print(f'[{__file__}] Some wrong value sent, please check for development team')

        #Around 10-35%, i'll choose 20%
        REQUIRED_PROTEIN = round((((20*calories_per_day)/100)/4), 2)

        #Around 45-65%, i'll choose 50%
        REQUIRED_CARBO = round(((50*calories_per_day)/100)/4, 2)

        #Around 20-35%, i'll choose 25%
        REQUIRED_FAT = round(((25*calories_per_day)/100)/9, 2)

        #Calculate necessary water
        water_per_day = round((35*55)/1000, 1)

        global_vars.data_post_form = {
                        'POST_FORM': {
                            'TMB': int(TMB), 
                            "GOAL": int(calories_per_day),
                            "PROTEIN": REQUIRED_PROTEIN,
                            "CARBO": REQUIRED_CARBO,
                            "FAT": REQUIRED_FAT,
                            "WATER": water_per_day,
                            "PERSONAL_INFO":{
                                "GENDER": gender,
                                "WEIGHT": weight,
                                "HEIGHT": height,
                                "AGE": age,
                        }}}


        return render(request, 'dashboard.html', global_vars.data_post_form)
    
@require_GET
def get_receipes(request):
    """
    Return the receips from Database
    """
    all_receipes = receipes.objects.all()

    for receipe in all_receipes:
        #Return as a list format
        receipe.ingredients = [ingrediente.strip() for ingrediente in receipe.ingredients.split(';')]
    
    return render(
                request, 'dashboard.html', 
                {"data": all_receipes, 
                "POST_FORM": global_vars.data_post_form['POST_FORM']}
                )


    



