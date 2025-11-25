from django.urls import path
from .views import UserRegitser,UserLogin,UserDetail,VerifyEmail
urlpatterns = [
    path("register/",UserRegitser.as_view(),name="register"),
    path("login/",UserLogin.as_view(),name="login"),
    path("me/",UserDetail.as_view(),name="UserDetails"),

    #VerifyEmail
    path("verify_email/<uuid:token>/",VerifyEmail.as_view(),name="verify_email"),
]