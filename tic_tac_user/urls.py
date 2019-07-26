from django.conf.urls import url
from tic_tac_user import views

urlpatterns = [
url(r'^$',views.home),
url(r'^tic_tac_toe/',views.tic_tac_toe,name='tic_tac_toe'),
]