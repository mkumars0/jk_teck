from django.urls import path
from app1 import views
app_name='app1'

urlpatterns=[
    path('',views.home,name='home'),
    path('registration/',views.regForm,name='registration'),
    path('register/',views.register,name='register'),
    path('view/',views.viewReg,name='view'),
    path('find_us/',views.find_us, name = 'find_us'),
    path('projects/',views.projects, name = 'projects'),

]
