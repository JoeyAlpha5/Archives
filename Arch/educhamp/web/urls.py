from .views import index, dashboard, slides, videos, announcements, registration
from django.urls import path
from django.contrib.auth import views

urlpatterns = [
    path('', views.LoginView.as_view(template_name="web/index.html")),
    path('dashboard/', dashboard),
    path('register/', registration),
    path('dashboard/slides', slides),
    path('dashboard/videos', videos),
    path('dashboard/announcements', announcements),
    path('login/', views.LoginView.as_view(template_name="web/index.html")),
    path('logout/', views.LogoutView.as_view(template_name="web/index.html")),
]