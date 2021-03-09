from django.urls import include, path

from . import views

urlpatterns = [
    path('formation/', include([
        path('', views.index, name='index'),
        path('blog/', views.blog, name='blog'),
        path('post/<int:pk>/', views.post_detail, name='post_detail'),
        path('post/new/', views.post_new, name='post_new'),
    ])),
]