from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),
    path('file_uploaded/', views.file_uploaded, name='file_uploaded'),
    path('logout/', views.logout, name='logout'),

    path('add_comment/<int:file_id>/', views.add_comment, name='add_comment'),
    path('add_reply/<int:file_id>/<int:parent_id>/', views.add_reply, name='add_reply'),

    path('check_user_data/', views.check_user_data, name='check_user_data'),

    # path('add_comment/<int:uploaded_file_id>/', views.add_comment, name='add_comment'),
    # path('reply_comment/<int:uploaded_file_id>/<int:parent_id>/', views.reply_comment, name='reply_comment'),

    # path('view_pdf/<int:file_id>/', views.view_pdf, name='view_pdf'),
    # path('view_pdf/<int:file_id>/', views.ViewPdf.as_view(), name='view_pdf'),
]
