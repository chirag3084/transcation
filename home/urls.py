from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter
from .views import TranscationViewSet

router = DefaultRouter()
router.register("transcations", TranscationViewSet)

# Registering the app's namespace
app_name = "home"


urlpatterns = [
    path("login/", views.login_page, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout_page, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("", views.home, name="home"),
    path("export_data_as_json/", views.export_data_as_json, name="export_data_as_json"),
    path("add_transcation/", views.add_transcation, name="add_transcation"),
    path("view_transcation/", views.view_transcation, name="view_transcation"),
    path(
        "export_data_as_json_by_id/<int:id>",
        views.export_data_as_json_by_id,
        name="export_data_as_json_by_id",
    ),
    # path("load_json_data/", views.load_json_data, name="load_json_data"),
    path("export_data_as_text/", views.export_data_as_text, name="export_data_as_text"),
    path("all_data/", views.all_data, name="all_data"),
    path("table/", views.table, name="table"),
    path(
        "password_reset/",
        views.auth_views.PasswordResetView.as_view(
            template_name="password_reset_form.html"
        ),
        name="password_reset_form",
    ),
    path(
        "password_reset/done/",
        views.auth_views.PasswordResetDoneView.as_view(
            template_name="password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "password_reset_confirm/<uidb64>/<token>/",
        views.auth_views.PasswordResetConfirmView.as_view(
            template_name="password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "password_reset_complete",
        views.auth_views.PasswordResetCompleteView.as_view(
            template_name="password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    path("api/v1/", include(router.urls)),
    path("plot_transactions/", views.plot_transactions, name="plot_transactions"),
]
