from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from users import urls as user_urls
from softdesk_management import urls as project_urls
from softdesk_issue import urls as issue_urls
from rest_framework_simplejwt import views as jwt_views

router = routers.DefaultRouter()

urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
    path('api/', include(project_urls)),
    path('api/', include(issue_urls)),
    path('api/users/', include(user_urls)),
    path(
        'api/token/',
        jwt_views.TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'api/token/refresh/',
        jwt_views.TokenRefreshView.as_view(),
        name='token_refresh'
    ),
]
