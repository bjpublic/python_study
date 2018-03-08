from django.conf.urls import url
from supermarket import views
 
urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^supermk$', views.supermk),
    url(r'^data$', views.data, name='data'),
    url(r'^d3sample$', views.d3sample),
]

