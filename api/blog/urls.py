from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from blog import views
from blog.views import PostViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts_ist')

urlpatterns = router.urls

urlpatterns += [
    path('test/', views.test),
]

urlpatterns += [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
