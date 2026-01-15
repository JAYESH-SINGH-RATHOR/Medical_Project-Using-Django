from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('test/', views.test, name='test'),
    path('test/<int:labtest_id>/', views.labtest_detail, name='labtest_detail'),
    path('test/<int:labtest_id>/item/<int:item_id>/',views.lab_item_details ,name='lab_item_details'),
    path('doctor', views.doctor, name='doctor'),
    path('doctor/<int:doctor_id>/', views.doctor_profile, name='doctor_profile'),
    path('registration', views.registration, name='registration'),
    path('login/', views.login_view, name='login'),
    path('medicine/', views.medicine_list, name='medicine_list'),
    path('medicine/<int:id>/', views.medicine_detail, name='medicine_detail'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
