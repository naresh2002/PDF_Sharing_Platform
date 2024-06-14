from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from .forms import SignUpForm, LoginForm, UploadedFileForm, CommentForm
from .models import User, File, Comment
from django.contrib.auth import logout as django_logout
from django.http import JsonResponse

# LOGIN
def login(request):
    error = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(username=username)
                if check_password(password, user.password):
                    # Login successful, we can implement session management here
                    request.session['user_name'] = user.username
                    request.session.save()
                    return redirect('all_files')
                else:
                    # Invalid password
                    error = "Invalid username or password."
            except User.DoesNotExist:
                # Invalid username
                error = "Invalid username or password."
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form, 'error': error})

# SIGNUP
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})



# LOGOUT
def logout(request):
    django_logout(request)
    return redirect('all_files')

# ALL FILES
def all_files(request):
    if request.session.get('user_name') :
        pdf_files = File.objects.filter(name__icontains='.pdf')
        form = CommentForm()
        user_name = request.session.get('user_name')
        return render(request, 'all_files.html', {'pdf_files': pdf_files, 'form' : form, 'user_name': user_name})
    else:
        return redirect('login')

# UPLOAD FILE
def upload_file(request):
    if request.session.get('user_name') :
        if request.method == 'POST':
            form = UploadedFileForm(request.POST, request.FILES)
            if form.is_valid():
                uploaded_file = form.save(commit=False)
                uploaded_file.owner = request.session.get('user_name')
                uploaded_file.save()
                return redirect('file_uploaded')
        else:
            form = UploadedFileForm()
    else:
        return redirect('login')
    return render(request, 'upload.html', {'form': form})

# FILE UPLOADED
def file_uploaded(request):
    return render(request, 'file_uploaded.html')

# ADD COMMENT
def add_comment(request, file_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            user_name = request.session.get('user_name')
            comment_text = form.cleaned_data['comment_text']
            file = File.objects.get(id=file_id)
            Comment.objects.create(user=user_name, file_id=file, comment_text=comment_text)
            return redirect('all_files')
    else:
        form = CommentForm()
    return render(request, 'add_comment.html', {'form': form})

# ADD REPLY
def add_reply(request, file_id, parent_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            user_name = request.session.get('user_name')
            comment_text = form.cleaned_data['comment_text']
            file = File.objects.get(id=file_id)
            parent_comment = Comment.objects.get(id=parent_id)
            Comment.objects.create(user=user_name, file_id=file, parent_comment_id=parent_comment, comment_text=comment_text)
            return redirect('all_files')
    else:
        form = CommentForm()
    return render(request, 'add_reply.html', {'form': form})

def check_user_data(request):
    username = request.GET.get('username', None)
    email = request.GET.get('email', None)
    data = {
        'username_is_taken': User.objects.filter(username__iexact=username).exists() if username else False,
        'email_is_taken': User.objects.filter(email__iexact=email).exists() if email else False,
    }
    return JsonResponse(data)