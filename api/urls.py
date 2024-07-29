from django.urls import path
from .views import UserCreateView, UserDetailView, ExpenseCreateView, UserExpensesView, OverallExpensesView

urlpatterns = [
    path('users/', UserCreateView.as_view(), name='create-user'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('expenses/', ExpenseCreateView.as_view(), name='add-expense'),
    path('users/<int:user_id>/expenses/', UserExpensesView.as_view(), name='user-expenses'),
    path('expenses/overall/', OverallExpensesView.as_view(), name='overall-expenses'),
]
