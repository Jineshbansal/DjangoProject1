from django.urls import path
from sam import views


urlpatterns = [
    path('sam/',views.home,name="sam-home"),
    path('avf/',views.avfhome,name="avf-home"),
    path('avf/add',views.avfform ,name="avf-create"),

    path('mock/',views.mockhome,name="mock-home"),
] 
