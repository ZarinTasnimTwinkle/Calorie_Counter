from django.shortcuts import render,redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum
from .models import *
from .forms import *

def registerPage(request):   
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account Created Successfully")
            return redirect('login')
    else:
        form = UserForm()
        
    context = {
        'form_title': 'Register Your Account',
        'form': form,
        'btn': 'Register',
    }
    return render(request, 'base.html', context)

def loginPage(request):
    if request.method == 'POST':
        form = AuthForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Logged-in Successfully")
            return redirect('dashboard')
    else:
        form = AuthForm()
        
    context = {
        'form_title': 'Login Here',
        'form': form,
        'btn': 'Login',
    }
    return render(request, 'base.html', context)

def logoutPage(request):
    logout(request)
    return redirect('login')

#----------------------------------------------------------------------------------#

@login_required
def UserEditPage(request):

    try:
        user = UserEditModel.objects.get(user=request.user)
    except UserEditModel.DoesNotExist:
        user = UserEditModel.objects.create(user=request.user)

    if request.method == "POST":
        r_formData = UserEditForm(request.POST, instance=user)
        if r_formData.is_valid():
            userData = r_formData.save(commit=False)

            if userData.gender == "Male":
                userData.bmr = 66.47 + (13.75 * userData.weight) + (5.003 * userData.height) - (6.755 * userData.age)
            else:
                userData.bmr = 655.1 + (9.563 * userData.weight) + (1.850 * userData.height) - (4.676 * userData.age)
            
            userData.save()
            return redirect('dashboard')

    form = UserEditForm(instance=user)
    context = {
        'form': form,
        'btn': 'Submit'
    }
    return render(request, 'UserEdit.html', context)

@login_required
def dashboardPage(request):

    try:
        user = UserEditModel.objects.get(user=request.user)
    except UserEditModel.DoesNotExist:
        user = UserEditModel.objects.create(user=request.user)

    if request.method == "POST":
        r_formData = FoodEntryForm(request.POST)
        if r_formData.is_valid():
            calorie = r_formData.save(commit=False)
            calorie.user = request.user
            calorie.save()
        
    ideal_bmr = user.bmr or 0
    consumed_calorie = FoodEntryModel.objects.filter(user=request.user).aggregate(total_calorie=Sum('calories'))['total_calorie'] or 0
    needed_calorie = ideal_bmr - consumed_calorie

    form = FoodEntryForm()
    context = {
        'form': form,
        'ideal_bmr': round(ideal_bmr, 2),
        'consumed_calorie': round(consumed_calorie, 2),
        'needed_calorie': round(needed_calorie, 2)
    }
    return render(request, 'dashboard.html', context)