from django.urls import path
from cbv import views
urlpatterns = [
    path("fbv/<pk>/", views.fbvview, name="fbv"),
    path("ucbv/<pk>/", views.ucbvview.as_view(), name="ucbv"),
    path("pcbv/<pk>/", views.pcbvview.as_view(), name="pcbv"),
    path("success/", views.success, name="success"),


]

'''
    path("fbv/<data>/", views.fbvview, name="fbv"),
    path("ucbv/<data>/", views.ucbvview.as_view(), name="ucbv"),
    path("pcbv/<data>/", views.pcbvview.as_view(), name="pcbv"),
    '''
