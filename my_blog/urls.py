from datetime import date
from django.urls import path
from . import views
from .views import SinglePostView

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="start_page"),
    path("posts", views.AllPostsView.as_view(), name="all-posts"),
    path("posts/<slug:slug>", views.SinglePostView.as_view(), name="post"),
    path("read-later", views.ReadLater.as_view(), name="read-later")
]