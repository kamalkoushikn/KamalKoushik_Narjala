from django.urls import path

from .views import ContactListView,ContactCreateView
    

urlpatterns = [
    path("", ContactListView.as_view(), name="contact_list"),
    path("create/", ContactCreateView, name="contact_form"),
]