from django.http import HttpResponse 
from django.shortcuts import render , redirect
from httpcore import request
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404

def home(request):
    return render(request , 'user/index.html')

def test(request):
    labtests = Labtest.objects.all()
    items = Labtestitems.objects.all()

    return render(request, "user/LabTest.html", {
        "labtests": labtests,
        "items": items
    })



def labtest_detail(request, labtest_id):
    labtest = get_object_or_404(Labtest, id=labtest_id)
    items = labtest.items.all()

    return render(request, "user/labtest_detail.html", {
        "labtest": labtest,
        "LabtestDatass": items
    })



def lab_item_details(request, labtest_id, item_id):
    # Labtestitemdetailss = Labtestitemsdetails.objects.get(id=item_id)
    Labtestitemdetailss = get_object_or_404(Labtestitemsdetails, id=item_id)

    return render(request, "user/lab_item_details.html", {
        "Labtestitemdetailss": Labtestitemdetailss
    })


def doctor(request):
    doctors = Doctor.objects.all()
    doctorProfile = DoctorProfile.objects.all()
    return render(request , "user/Doctor.html", {"doctors": doctors, "doctorProfile": doctorProfile})

def doctor_profile(request, doctor_id):
    doctor = get_object_or_404(DoctorProfile, id=doctor_id)
    if request.method == "POST":
        doctorname = request.POST.get('doctorname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        disease = request.POST.get('disease')
        prescription = request.FILES.get('prescription')
        appointment = Appointment(
            doctorname=doctorname,
            username=username,
            email=email,
            phone=phone,
            date=date,
            disease=disease,
            prescription=prescription
        )
        appointment.save()
    return render(request, "user/doctor_profile.html", {"doctor": doctor})

def registration(request):
    if request.method == 'POST':
       username = request.POST.get('username')
       email = request.POST.get("email")
       password = request.POST.get('password')
       confirm_password = request.POST.get("confirm_password")
       user = UserData(username = username , email = email , password = password , confirm_password = confirm_password)
       user.save()
    return render(request, "user/registration.html")

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)   
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')

    return render(request, "user/login.html")


@login_required(login_url='login')
def dashboard(request):
    return render(request, "user/dashboard.html")

def medicine_list(request):
    medicines = Medicine.objects.all()
    return render(request, "user/medicine.html", {"medicines": medicines})

def medicine_detail(request, id):
    medicine = Medicine.objects.get(id=id)
    return render(request, "user/medicinedetails.html", {"medicine": medicine})
