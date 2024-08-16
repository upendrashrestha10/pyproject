from django.urls import path
from.import views

urlpatterns = {
    #paths takes 3 arguments

    path('', views.index,  name="index")

}
