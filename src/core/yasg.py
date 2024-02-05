from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf import settings

schema_view = get_schema_view(
    openapi.Info(
        title="Gas station CRM Api",
        default_version='v1',
        description="Gas station CRM api documentations",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="haydarovakbar640@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    url=settings.HOST,
)
