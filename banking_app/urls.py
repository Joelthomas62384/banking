from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("login",views.login_page,name="login"),
    path("register",views.register_page,name="register"),
    path("logout",views.logout_page,name="logout"),
    path("get_user/<str:username>/", views.get_user),
    path('get_branches/<str:district>/', views.get_branches, name='get_branches'),
    
]
