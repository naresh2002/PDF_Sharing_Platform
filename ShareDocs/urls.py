from django.urls import path
from . import views, api

urlpatterns = [
    # HOME
    path('', views.all_files, name='all_files'),

    # LOGIN & SIGNUP
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),

    # FILE UPLOAD
    path('upload/', views.upload_file, name='upload_file'),
    path('file_uploaded/', views.file_uploaded, name='file_uploaded'),

    # COMMENTS & REPLIES
    path('add_comment/<uuid:file_id>/', views.add_comment, name='add_comment'),
    path('add_reply/<uuid:file_id>/<uuid:parent_id>/', views.add_reply, name='add_reply'),

    # OTHERS
    path('check_user_data/', views.check_user_data, name='check_user_data'),
    path('api/user/<str:username>/', api.get_user_data, name='api_get_user_data'),

]
