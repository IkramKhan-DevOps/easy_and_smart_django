from django.urls import include, path

app_name = "learning"
urlpatterns = [

    path('ch1/', include('learning.ch1_basic.urls', namespace="ch1")),
    path('ch2/', include('learning.ch2_oop.urls', namespace="ch2")),

    # path('ch3/', include('learning.ch3_generic.urls', namespace="ch3")),
    # path('ch4/', include('learning.ch4_advance.urls', namespace="ch4")),
    # path('ch5/', include('learning.ch5_premium.urls', namespace="ch5")),
    # path('ch6/', include('learning.ch6_enterprise.urls', namespace="ch6")),

]