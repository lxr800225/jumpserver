from django.conf.urls import patterns, include, url


urlpatterns = patterns('jperm.views',
    # Examples:
    # url(r'^$', 'jumpserver.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    (r'^perm_edit/$', 'perm_edit'),
    (r'^perm_add/$', 'perm_add'),
    (r'^dept_perm_edit/$', 'dept_perm_edit'),
    (r'^perm_list/$', 'perm_list'),
    (r'^dept_perm_list/$', 'dept_perm_list'),
    (r'^perm_user_detail/$', 'perm_user_detail'),
    # (r'^perm_list_ajax/$', 'perm_list_ajax'),
    (r'^perm_detail/$', 'perm_detail'),
    (r'^perm_del/$', 'perm_del'),
    (r'^perm_asset_detail/$', 'perm_asset_detail'),
    (r'^sudo_list/$', 'sudo_list'),
    (r'^sudo_add/$', 'sudo_add'),
    (r'^sudo_del/$', 'sudo_del'),
    (r'^sudo_edit/$', 'sudo_edit'),
    (r'^sudo_detail/$', 'sudo_detail'),
    (r'^cmd_add/$', 'cmd_add'),
    (r'^cmd_list/$', 'cmd_list'),
    (r'^cmd_del/$', 'cmd_del'),
    (r'^cmd_edit/$', 'cmd_edit'),
)
