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
    
    path('get_registerview',RegisterView.as_view({'get':'list'}),name='registerView'),
    
    path('search_user_View',Search_user_View.as_view({'get':'list'}),name='search_user_View'),
    
    path('get_login_otp_mobile',ValidatePhoneSendOTP.as_view(),name='get-login-otp-mobile'),
    
    path('verify_login_otp_mobile',VerifyPhoneOTPView.as_view(),name='login-otp-verify'),
    
    path('logout',knox_views.LogoutView.as_view(), name='logout'),
    
    path('user_get', User_get_view.as_view({'get':'list'}), name='user_get'),
    
    path('user_update', User_update_view.as_view({'get':'retrieve','put':'update'}), name='user_update'),
    
    path('upload_image', Upload_image_view.as_view({'get':'list'}), name='upload_image'),
    
    path('favourite_user', Favourite_user_view.as_view({'get':'list','post':'create'}), name='favourite_user'),
    
    path('chatting', Chatting_view.as_view({'get':'list','post':'create','put':'update',"delete":"destroy"}), name='chatting'),
    
    path('favourite_notification', Favourite_notification_view.as_view({'get':'list'}), name='like_notification'),
    
    path('favourite_seen', Favourite_seen_view.as_view({'put':'update'}), name='favourite_seen'),
    
    path('chatting_seen', Chatting_seen_view.as_view({'put':'update'}), name='chatting_seen'),
    
    path('favourite_count', Favourite_count_view.as_view({'get':'list'}), name='favourite_count'),
    
]