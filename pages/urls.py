from django.urls import path
from . import views

urlpatterns = [
    # path('api/users/',views.ListUsers.as_view()),
    # path('api/token/auth/', views.CustomAuthToken.as_view()),
    path('',views.index,name="index"),
    path('admin/advisor/',views.admin_page,name="Admin Page"),
    path('user/register/',views.register,name="register"),
    path('user/login/',views.login_user,name="login"),
    path('user/<int:id>/advisor/',views.advisor_list,name="COntent List"),
    path('user/<int:id>/advisor/booking/',views.booked_calls,name="Book"),
    path('user/<user_id>/advisor/<advisor_id>/',views.call_advisors,name="Bookcall"),
]