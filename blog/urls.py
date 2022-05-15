from django.urls import path
from blog import views



urlpatterns = [
    path('', views.render_posts, name='blog'),
    path('post/<int:post_id>', views.post_detail, name='post_detail'),
]