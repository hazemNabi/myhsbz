from django.contrib import admin
from django.urls import path,include

from django.contrib.auth import views as auth_views

from .views import *
# from .views import UserRegistrationView,UserLoginAPIView
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    # path('api-token-auth', obtain_auth_token),
    path('api_fbv/',FBV_List),
    path('my_view/',my_view),
    path('api_Address_List/',CBV_Address_List.as_view()),
     path('CBV_Address_By_Id/',CBV_Address_By_Id.as_view()),
    path('api_CBV_Get_All_Orders_List/',CBV_Get_All_Orders_List.as_view()),
    path('get-user-orders-by-id/', GetUserOrderListByID.as_view()),
   
    path('api_cbv/',CBV_List.as_view()),
   
    path('register/', create_account, name='user_registration'),
    path('api-login/', UserLoginView.as_view(), name='user_login'),
    path("search_products/",Search, ),
    # path('CBV_User_info_By_Id/',CBV_User_info_By_Id.as_view()),
  
    # path('api_CBV_ListOfOrders/',views.CBV_ListOfOrders.as_view()),
    path('api_cbvcatag/',CBVCatg_List.as_view()),
    path('api_CBVCoustemSections/',CBVCoustemSections_List.as_view()),
    path('api_CBVProdects_List/',CBVProdects_List.as_view()),
  
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(),
         name='blacklist'),
    path('api/user-detail/',user_detail ),
    # path('rest/generics/', views.generics_list.as_view()),
]
