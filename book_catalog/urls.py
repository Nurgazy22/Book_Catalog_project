from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from books.swagger import schema_view


urlpatterns = [
    path('admin/', admin.site.urls), # Django admin interface
    path('api/', include('books.urls')),    path('docs/', include_docs_urls(title='Book Catalog API')),  # Routes books
    path('schema/', get_schema_view(title='Book Catalog API Schema')),  # API schema provided by DRF
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Swagger UI API docs
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  # ReDoc for API docs
    path('dj-rest-auth/', include('dj_rest_auth.urls')),  # Routes for authentication via dj-rest-auth
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),  # Routes for registration
    path('accounts/', include('allauth.urls')),  # Routes for django-allauth
]