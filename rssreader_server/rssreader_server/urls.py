from django.urls import path, include

urlpatterns = [
    path('api/v1/', include('api_v1.urls'))
]
