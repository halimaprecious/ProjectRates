from django.urls import re_path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns =[
    re_path(r'^$',views.home, name= 'home'),

    re_path(r'^accounts/profile/$', views.user_profiles, name='profile'),

    re_path(r'^search/', views.search_projects, name='search_results'),
    re_path(r'^project/(\d+)', views.get_project, name='project_results'),
    re_path(r'^new/project$', views.add_project, name='new-project'),
    re_path(r'ratings/', include('star_ratings.urls', namespace='ratings')),

    re_path(r'^api/projects/$', views.ProjectList.as_view()),
    re_path(r'^api/profiles/$', views.ProfileList.as_view()),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)