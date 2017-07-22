from django.conf.urls import url
from . import views
from django.contrib.auth.views import login
urlpatterns = [
	url(r'^$',views.home),
	url(r'^login/$',login ,{'template_name':'accounts/log.html'}),
	url(r'^import_sheet/', views.import_sheet, name="import_sheet"),
	url(r'^import_source/', views.import_source, name="import_source"),
	url(r'^view_approval/', views.view_approval, name="view_approval"),
	url(r'^view_source/', views.view_source, name="view_source"),
	url(r'^export/', views.export_data, name="export"),
	url(r'^filtered/', views.view_filtered, name="view_filtered"),
	url(r'^edit/', views.edit_view, name="edit_view"),
	url(r'^update/', views.update_db, name="update_db")

]