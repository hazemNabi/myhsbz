
from django.urls import path
from account.views import ProFiel,update_client,complete_task,task,assign_employee,commission,dashboard,user_type_summary,manage_employees,delete_object,edit_employee,add_employee,add_client,manage_client
# from .views import UserRegistrationView,UserLoginAPIView
from account import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('accounts/', views.accounts, name='accounts'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('ProFiel/', views.ProFiel, name='ProFiel'),
    path('addclient/', views.add_client, name='addclient'),
    path('delete_object/<int:id>', views.delete_object, name='delete_object'),
    path('update_client/<int:id>', views.update_client, name='update_client'),
    path('assign_employee/<int:task_id>', views.assign_employee, name='assign_employee'),
    path('manage_client/', views.manage_client, name='manage_client'),
    path('manage_employees/', views.manage_employees, name='manage_employees'),
    path('add_employee/', views.add_employee, name='add_employee'),
    path('user_type_summary/', views.user_type_summary, name='user_type_summary'),
    path('edit_employee/<int:id>/', views.edit_employee, name='edit_employee'),
    path('commission/<int:id>',commission,name='commission'),

]    