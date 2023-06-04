from django.contrib import admin
from django.urls import path, include
from .views import TestView
#from Auth.views import LoginView
from Authentications.views import Register_Account, Login_User
from Listen_Portal.views import Get_Info, Change_Info
from Notifications_Management.views import GetUserNotifs
from Device_Listen_Portal.views import Device_Portal, TestDevice
from Devices_Management.views import GetUsersDevices, Add_Device, GetUserDevice
from User_Listen_Portal.views import User_Portal
from Transaction_Portal.views import Subscribe_Device


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('test-api',  TestView.as_view(), name='login-user'),
    path('login-user', Login_User.as_view(), name='login-user'),
    path('register-account', Register_Account.as_view(), name='register-account'),
    path('add-device', Add_Device.as_view(), name='add-device'),
    path('change-info', Change_Info.as_view(), name='change-info'),
    path('user-notifications', GetUserNotifs.as_view(), name='user-notifications'),
    #path('device-listen-portal', Device_Portal.as_view(), name='device-listen-portal'),
    path('user-listen-portal', User_Portal.as_view(), name='user-listen-portal'),
    path('user-subscription', Subscribe_Device.as_view(), name='user-subscription'),
    
    path('receive', TestDevice.as_view(), name="receive"),
    path('device-receive', Device_Portal.as_view(), name="receive"),
    path('get-user-devices', GetUsersDevices.as_view(), name='get-user-devices'),
    path('get-user-device', GetUserDevice.as_view(), name='get-user-device')
]
