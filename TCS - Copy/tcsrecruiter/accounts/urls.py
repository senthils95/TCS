from django.conf.urls import url
from . import views
from django.contrib.auth.views import login
urlpatterns = [
	url(r'^$',views.home),
	url(r'^login/$',login ,{'template_name':'accounts/log.html'}),
	#url(r'^import_sheet/', views.import_sheet, name="import_sheet"),
	url(r'^import_source/', views.import_source, name="import_source")
]