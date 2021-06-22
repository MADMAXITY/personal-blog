from django.urls import path, include
import blog.views as views
urlpatterns = [
    path('', views.start),
    path('getdata/', views.senddata),
    path('postdata/', views.postdata),
]
