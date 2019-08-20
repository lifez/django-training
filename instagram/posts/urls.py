from django.urls import path

from .views import CreatePostView, ListPostView

urlpatterns = [
    path("", ListPostView.as_view(), name="posts"),
    path("new/", CreatePostView.as_view(), name="new_post"),
]