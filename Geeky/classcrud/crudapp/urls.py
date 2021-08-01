from django.urls import path, include

from .import views


urlpatterns=[
   
    
    path('',views.UserAddShowView.as_view(),name='add'),
    path('delete/<int:id>/',views.UserDeleteData.as_view(),name='delete'),
    path('<int:id>/',views.UpdateUserView.as_view(),name='update'),
    path('api/',include('crudapp.api.urls'))
    
    
    
    ]