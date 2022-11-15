from django.urls import path
from myapp import views

urlpatterns = [
    path("", views.email_login, name="login"),
    path("profile/", views.profile, name="profile"),
    path("logout/", views.logout, name="logout"),
]