
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from user_accounts.api_views import *


from Inventory_management.urls import router
router.register(r'user_accounts/staff/register', StaffCreatViewSet, basename='register_staff')
router.register(r'user_accounts/login', LoginViewSet, basename='login')
router.register(r'user_accounts/user', UserList, basename='User')



urlpatterns = [
    # ------------------jwt------------
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    #-----------------customUrl---------------
    path('api/', include(router.urls)),
    
]
