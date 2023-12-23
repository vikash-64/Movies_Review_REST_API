from django.urls import path
from .views import MovieListCreateView, MovieRetrieveUpdateDestroyView, ReviewListCreateView, ReviewRetrieveUpdateDestroyView

urlpatterns = [
    path('movies/', MovieListCreateView.as_view()),
    path('movies/<int:pk>/', MovieRetrieveUpdateDestroyView.as_view()),
    path('reviews/', ReviewListCreateView.as_view()),
    path('reviews/<int:pk>/', ReviewRetrieveUpdateDestroyView.as_view()),
]
