from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student_table
from .forms import Student_form_data
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    data = {
        'name': "abc",
        'age': 17,
        'department': "BCA"
    }
    marks = [100, 98, 97]
    return render(request, 'home.html', {
        'data1': data,
        'marks1': marks
    })

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def form1(request):
    if request.method == 'POST':
        reg_no = request.POST.get('reg_no')
        name = request.POST.get('name')
        marks = request.POST.get('marks')
        email = request.POST.get('email')
        dob = request.POST.get('dob')

        Student_table.objects.create(
            reg_no=reg_no,
            name=name,
            email=email,
            dob=dob,
            marks=marks
        )

        return HttpResponse("Saved successfully")

    return render(request, 'student_form.html')
def student_form_dj(request):
    if request.method == 'POST':
        form = Student_form_data(request.POST)

        if form.is_valid():
            Student_table.objects.create(
                reg_no=form.cleaned_data['reg_no'],
                name=form.cleaned_data['name'],
                marks=form.cleaned_data['marks'],
                email=form.cleaned_data['email'],
                dob=form.cleaned_data['dob']
            )

            return HttpResponse("Student Saved Successfully!")

    else:
        form = Student_form_data()

    return render(request, 'student_form_data.html', {'form': form})
def user_login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(
            request,
            username=username,
            password=password
        )
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            return HttpResponse("Invalid username or password")
    return render(request,'login.html')
@login_required(login_url='login')
def dashboard(request):
    return render(request,'dashboard.html')

def user_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')
    return redirect('dashboard')
