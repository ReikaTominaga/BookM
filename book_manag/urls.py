from django.urls import path

from . import views

app_name = 'book_manag'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('inquiry/', views.InquiryView.as_view(), name="inquiry"),
    path('bookm-list/', views.BookmListView.as_view(), name="bookm_list"),
]