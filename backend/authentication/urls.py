from django.urls import path
from .views import SignUpView, SignInView,get_profile_pic

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('user/<str:user_id>/profile-pic/', get_profile_pic, name='get-profile-pic')
]

