from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index.as_view(), name='index'),
    path('create/', createTest.as_view(), name='create'),
    path('tests/', testList.as_view(), name='testList'),
    path('tests/<str:test_name>/', testPage.as_view(), name='testPage'),
    path('registration/', Registration.as_view(), name='reg'),
    path('login/', User_login.as_view(), name='login'),
    path('logout/', User_logout.as_view(), name='logout'),
    path('aboutus/', AboutUs.as_view(), name='aboutus'),
]