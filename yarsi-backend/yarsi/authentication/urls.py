from .api.signup import Signup
from .api.login import Login
from .api.logout import Logout
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', Signup.as_view()),
    path('login/', Login.as_view()),
    path('logout/', Logout.as_view()),

]
