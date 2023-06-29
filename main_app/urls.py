from django.urls import path

from . import views


urlpatterns = [
    # Leave as empty string for base url
    path('', views.menu, name="menu"),
    path('reservation/', views.get_reserv, name='Reservation'),
    path('about_us/', views.about_us, name='about_us'),
]
