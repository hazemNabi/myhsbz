
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
# from prodect.views import  ProtectedView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('account.urls')),
    path('',include('api.urls')),
    path('',include('order.urls')),
    path('',include('prodect.urls')),
  
    path('api/token-auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token-refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
# {
#     "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4ODUwMDgzMSwiaWF0IjoxNjg3NjM2ODMxLCJqdGkiOiI2ZjY1ZGQyZDU2NWM0MGEwOTQzOTczZDRhMGQxZTU5MyIsInVzZXJfaWQiOjF9.ItFK13eziR7CMUfJaVMuTITiS-esh297smUmGCDX0TY",
#     "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg3NjM2ODkxLCJpYXQiOjE2ODc2MzY4MzEsImp0aSI6IjMxZjA3MzZkNTc5ZTQ2YTJhNzVkMDZiMGVhOTliNzJlIiwidXNlcl9pZCI6MX0.yj1XdnmKAG321BpUNH9YOurUjLGVsq4v4VwbGXENizY"
# }