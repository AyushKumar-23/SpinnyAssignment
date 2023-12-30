from django.urls import path
from .views import BoxList, UpdateBox, MyBoxList, AddBox, DeleteBox

urlpatterns = [
    path('list-all-boxes/', BoxList.as_view(), name='box-list'),
    path('add-box/',AddBox.as_view(),name='add-box'),
    path('update-box/<int:pk>/', UpdateBox.as_view(), name='box-detail'),
    path('list-my-boxes/', MyBoxList.as_view(), name='my-box-list'),
    path('delete-box/<int:pk>/',DeleteBox.as_view(),name='delete-box'),
]