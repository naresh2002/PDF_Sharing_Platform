from django.db import models
import uuid

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

# class UploadedFile(models.Model):
class File(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # file = models.FileField(upload_to='')
    name = models.FileField(upload_to='')
    # uploaded_by = models.CharField(max_length=50)
    owner = models.CharField(max_length=50) # user OR owner 
    # upload_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # user_name = models.CharField(max_length=50)
    user = models.CharField(max_length=50)
    # uploaded_file = models.ForeignKey(UploadedFile, related_name='comments', on_delete=models.CASCADE)
    file_id = models.ForeignKey(File, related_name='comments', on_delete=models.CASCADE)
    # parent = models.ForeignKey('self', related_name='replies', null=True, blank=True, on_delete=models.CASCADE)
    parent_comment_id = models.ForeignKey('self', related_name='replies', null=True, blank=True, on_delete=models.CASCADE)
    # text = models.CharField(max_length=255)
    comment_text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
