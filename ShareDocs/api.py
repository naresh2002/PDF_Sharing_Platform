from django.http import JsonResponse
from .models import User

def get_user_data(request, username):
    try:
        user = User.objects.get(username=username)
        data = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
        }
        return JsonResponse({'data': data})
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
