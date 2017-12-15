from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailsView, CreateexpView, DetailsexpView, RealsolutionsView, MerojobView, RojgariView, AayulogicView

urlpatterns = {
    url(r'^companies/$', CreateView.as_view(), name="create"),
    url(r'^companies/(?P<pk>[0-9]+)/$', DetailsView.as_view(), name="details"),
    url(r'^expenses/$', CreateexpView.as_view(), name="expcreate"),
    url(r'^expenses/(?P<pk>[0-9]+)/$', DetailsexpView.as_view(), name="expdetails"),
    url(r'^companies/realsolutions$', RealsolutionsView.as_view(), name="realsolutions"),
    url(r'^companies/merojob$', MerojobView.as_view(), name="merojob"),
    url(r'^companies/rojgari$', RojgariView.as_view(), name="rojgari"),
    url(r'^companies/aayulogic$', AayulogicView.as_view(), name="aayulogic"),
}

urlpatterns = format_suffix_patterns(urlpatterns)