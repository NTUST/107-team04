from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    #index,post_list 皆為首頁, view為個別文章的頁面, category為特定分類的文章列表, (new add save update)
    url(r'^$', views.index, name='index'),
    url(r'^category/$', views.category, name='category'),
    url(r'^view/$', views.view, name='view'),
    url(r'^view/(?P<p_id>[0-9]+)/post_comment/$', views.post_comment, name='post_comment'), 
    url(r'^save/$', views.save, name='save'), 
    url(r'^about/$', views.about, name='about'), 
    ]
urlpatterns += staticfiles_urlpatterns()