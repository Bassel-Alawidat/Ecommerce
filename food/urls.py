from . import views
from django.urls import path,include
app_name='food'
urlpatterns = [
    
    #food/
    path('',views.IndexClassView.as_view(),name='index'),
    #path('',views.index,name='index'),
    #food/
    #path('<int:item_id>/',views.detail,name='detail'),
    #path('<int:pk>',views.DetailView.as_view(),name='detail'),
    path('item/<int:item_id>/', views.FoodDetailView.as_view(), name='detail'), # Using class based 
    path('item/',views.item,name='item'),
    #add item
    path('add/',views.create_item,name='create_item'),
    #path('add/',views.CreatItem.as_view(),name='create_item'), #usnigclass based
    #edit item
    path('update/<int:id>/', views.update_item, name='update_item'),
    path('delete/<int:id>/',views.delete_item,name='delete_item'),
    
]
