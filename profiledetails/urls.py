from django.urls import path
from profiledetails.views import *
from django.urls import path,include

from rest_framework import routers
from knox.views import LogoutView
from knox import views as knox_views
router = routers.DefaultRouter()
router.register('user_register', RegisterView, basename='task')

urlpatterns = [ 
    path('',include(router.urls)),
    path('get_login_otp_mobile',ValidatePhoneSendOTP.as_view(),name='get-login-otp-mobile'),
    path('verify_login_otp_mobile',VerifyPhoneOTPView.as_view(),name='login-otp-verify'),
    path('logout',knox_views.LogoutView.as_view(), name='logout'),
    path('user_get', User_get_view.as_view({'get':'list'}), name='user_get'),
    path('user_update', User_update_view.as_view({'get':'retrieve','put':'update'}), name='user_update')
]