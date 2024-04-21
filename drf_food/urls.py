from django.urls import path
from drf_food import views as rest_view

urlpatterns = [

    path('', rest_view.FoodCategoryList.as_view()),

]