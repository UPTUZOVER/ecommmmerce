from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from products.views import (
                        ProductViewSet,
                        ProductDetailViewSet,
                        CategoryViewSet,
                        CategoryDetailViewSet
                        )


from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



from rest_framework_swagger.views import get_swagger_view

schema_view = get_schema_view(
    openapi.Info(
        title="INCOME EXPENSES API",
        default_version='v1',
        description="Your API description",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@expenses.com"),
        license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [

    path("SuperAdmin/", admin.site.urls),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    #path('api/', include('products.urls')),


    #products uchun
    path('api/products/', ProductViewSet.as_view()),
    path('api/products/<str:pk>/', ProductDetailViewSet.as_view(), name='product-detail'),
    path('api/categories/', CategoryViewSet.as_view()),
    path('api/categories/<int:pk>/', CategoryDetailViewSet.as_view(), name='category-detail'),
    

    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]






if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

