from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'), # user name. email and age
    path('save-user', views.save_user, name='save-user'),
    path('calc-bmi', views.calc_bmi, name='bmi-show'), # show calculated BMI
    path('all-entries', views.all_entries, name='bmi-entries')
]

