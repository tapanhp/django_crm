from django.urls import path
from .views import lead_details, lead_create, lead_update, lead_delete, LeadListView

app_name = "leads"

urlpatterns = [
    path("", LeadListView.as_view(), name="lead_list"),
    path("<int:pk>/", lead_details, name="lead_details"),
    path("<int:pk>/update", lead_update, name="lead_update"),
    path("<int:pk>/delete", lead_delete, name="lead_delete"),
    path("create/", lead_create, name="lead_create"),
]
