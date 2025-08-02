"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""






from django.contrib import admin
from django.urls import include, path
from django.conf import settings

from django.conf.urls.static import static
urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/",include('django.contrib.auth.urls')),
    path("logout.html/", include(("home.urls", "logout"), namespace="logout")),
    path("register.html/", include(("home.urls", "register"), namespace="register")),
    path("login.html/", include(("home.urls", "login"), namespace="login")),
    path("", include(("home.urls", "home"), namespace="home")),
    path(
        "forgetPassword.html/",
        include(("home.urls", "forgetPassword"), namespace="forgetPassword"),
    ),
    path("dashboard.html/", include(("home.urls", "dashboard"), namespace="dashboard")),
    path("view_transcation.html/", include(("home.urls", "view_transcation"), namespace="view_transcation")),
       
    
] + static(settings.STATIC_URL)
