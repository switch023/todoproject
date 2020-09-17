from django.urls import path
from .views import topfunc, signupfunc, loginfunc, logoutfunc, listfunc, detailfunc, TodoCreate, TodoDelete, TodoUpdate

urlpatterns = [
    path('', topfunc, name='top'),
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('logout/', logoutfunc, name = 'logout'),
    path('list/', listfunc, name='list'),
    path('detail/<int:pk>', detailfunc, name = 'detail'),
    path('create/', TodoCreate.as_view(), name = 'create'),
    path('delete/<int:pk>', TodoDelete.as_view(), name = 'delete'),
    path('update/<int:pk>', TodoUpdate.as_view(), name = 'update'),

]