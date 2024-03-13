from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
# from drf_yasg import openapi
# from drf_yasg.views import get_schema_view

# schema_view = get_schema_view(
#     openapi.Info(
#         title="REST API",
#         default_version="v1",
#         description="Rest API",
#         terms_of_service="https://starterkit.app",
#         contact=openapi.Contact(email="supercode@af.com"),
#         license=openapi.License(name="MIT License"),
#     ),
#     public=True,
#     permission_classes=[permissions.AllowAny],
# )


urlpatterns = [
    path("accounts/", include("accounts.urls")),
    path("users/", include("accounts.urls")),
    # approval engine
    path("approval_engine/", include('approval_engine.urls')),
    # all urls 
    path("app/", include("api.urls")),
]
