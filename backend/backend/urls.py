from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import settings
from django.conf.urls.static import static
from user.views import (
    ProfileButtonView, 
    ShowTeachersView, 
    ShowStudentsView, 
    RegisterUserToCustomUserModelView,
    ShowProfilePrivateView,
    WaitForApprovalRegisterUserToCustomUserModelView,
    CheckWaitForApprovalRegisterUserToCustomUserModelView
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Authentication URLs
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Api routes
    path('api/waituser/', WaitForApprovalRegisterUserToCustomUserModelView.as_view()),
    path('api/checkwaituser/<str:id>', CheckWaitForApprovalRegisterUserToCustomUserModelView.as_view()),
    path('api/registeruser/', RegisterUserToCustomUserModelView.as_view()),
    path('api/profilebutton/', ProfileButtonView.as_view()),
    path('api/showteachers/', ShowTeachersView.as_view()),
    path('api/showstudents/', ShowStudentsView.as_view()),
    path('api/myprofile/<str:id>/', ShowProfilePrivateView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)