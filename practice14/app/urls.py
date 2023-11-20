from django.urls import path
from app.views import create_post_view,all_posts_view,post_page_view

urlpatterns = [
    path('', all_posts_view, name='all_posts_url'),
    path('create_post/',create_post_view, name='create_post_url'),
    path('show_post/<int:pk>/', post_page_view, name='show_post_url' )
 
]

