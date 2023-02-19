from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import settings
from django.conf.urls.static import static
from authentication.views import (
    RegisterView,
    LoginView,
    AddUserView,
    SelfUpdateView,
    UpdatePasswordView,
    DeleteUserView,
)
# from base.views import (
#     ShowSelfView,
#     ShowAllTeachersView,
#     ShowAllStaffsView,
#     ShowAllStudentsView,
#     ShowAllUnapprovedUser
# )

urlpatterns = [
    path('admin/', admin.site.urls),

    # Authentication URLs
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

#     # Authentication App routes
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('adduser/', AddUserView.as_view()),

    path('selfupdate/', SelfUpdateView.as_view()),
    path('updatepass/', UpdatePasswordView.as_view()),
    path('deleteuser/', DeleteUserView.as_view()),

#     # Base App routes
#     path('showuser/', ShowSelfView.as_view()),
#     path('adminteacher/', ShowAllTeachersView.as_view()),
#     path('adminstudent/', ShowAllStudentsView.as_view()),
#     path('adminstaff/', ShowAllStaffsView.as_view()),
#     path('adminunapproveduser/', ShowAllUnapprovedUser.as_view())
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)