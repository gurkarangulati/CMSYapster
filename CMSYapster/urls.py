from django.conf.urls import patterns, include, url
from django.contrib import admin
import calendars.urls
import tasks.urls
import gits.urls
import listings.urls
import cms_channels.urls
import cms_reports.urls
import wiki.urls
import stats.urls

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'CMSYapster.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^calendar/', include(calendars.urls)),
                       url(r'^tasks/', include(tasks.urls)),
                       url(r'^gits/', include(gits.urls)),
                       url(r'^lists/', include(listings.urls)),
                       url(r'^channels/', include(cms_channels.urls)),
                       url(r'^reports/', include(cms_reports.urls)),
                       url(r'^wiki/', include(wiki.urls)),
                       url(r'^statistics/', include(stats.urls)),
                       url(r'^login/', 'admins.views.login_user'),
                       url(r'^home/', 'stats.views.homepage'),
                       url(r'^get/home_stats/$', 'stats.views.home_stats'),
                       url(r'^get/location_option/$', 'stats.views.location_option'),
                       url(r'^post/specific_search/$', 'stats.views.specific_search'),
                       url(r'^post/messenger/$', 'chat.views.chat'),
                       url(r'^post/search/$', 'cms_search_log.views.form_fields'),
                       url(r'^post/search/results/$', 'cms_search_log.views.results'),
                       url(r'^search/$', 'stats.views.search'),
                       url(r'^announcements/$', 'announcements.views.annoucements_manage'),
                       url(r'^statistics/databases/$', 'db_manager.views.home_database'),
                       url(r'^databases/graphs/$', 'db_manager.views.graphs_rds'),
                       url(r'^statistics/servers/$', 'db_manager.views.home_server'),
                       url(r'^servers/graphs/$', 'db_manager.views.graphs_ec2'),
                       url(r'^databases/rds/graph/$', 'db_manager.views.display_one_graph_rds'),
                       url(r'^databases/ec2/graph/$', 'db_manager.views.graph_ec2'),
                       url(r'^statistics/databases/rds/(?P<instance>[a-zA-Z0-9_.-]+)/$', 'db_manager.views.rds_details'),
                       url(r'^statistics/servers/ec2/(?P<instance>[a-zA-Z0-9_.-]+)/$', 'db_manager.views.ec2_details'),
                       url(r'^contacts/$', 'contacts.views.contacts_lists'),
                       url(r'^contacts/lists/(?P<list>[a-zA-Z0-9_.-]+)/$', 'contacts.views.contacts_lists_details'),
                       url(r'^contacts/lists/(?P<list>[a-zA-Z0-9_.-]+)/contacts/(?P<contact>[a-zA-Z0-9_.-]+)/$', 'contacts.views.contacts_details'),
                       url(r'^permissionsgroups/$', 'groups.views.group_manage'),
                       url(r'^permissionsgroups/(?P<group>[a-zA-Z0-9_.-]+)/$', 'groups.views.group_details'),
                       url(r'^cmsusers/$', 'admins.views.users_manage'),
                       url(r'^cmsusers/(?P<username>[a-zA-Z0-9_.-]+)/edit/$', 'admins.views.edit_cmsuser'),
                       url(r'^(?P<username>[a-zA-Z0-9_.-]+)/$', 'admins.views.profile'),
                       url(r'^(?P<username>[a-zA-Z0-9_.-]+)/photos/$', 'admins.views.edit_profile_pic'),
                       url(r'^$', 'stats.views.homepage'),
                       )