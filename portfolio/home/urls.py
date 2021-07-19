from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from home import views

app_name ='home'
urlpatterns = [
    #/home/
    path('', views.IndexClassView.as_view(), name='home' ),
    #/home/
    path('<int:pk>/',views.FoodDetail.as_view(),name='detail'),
    path('security', views.security, name='security'),

    #adding items 
    path('add',views.createItem.as_view(), name ='create_item'),       
    #for editing
    path('update/<int:id>/',views.update_item,name='update_item'),

    #for delete
    path('delete/<int:id>',views.delete_item,name='delete_item')
]