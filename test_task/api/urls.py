from django.urls import include, path

from .views import RequestView

app_name = 'api'


urlpatterns = [
    path('test-task/', RequestView.as_view(), name='request-view'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
