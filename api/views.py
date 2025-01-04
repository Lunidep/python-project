from django.http import JsonResponse
from django.views import View

class PingPongController(View):
    def get(self, request, *args, **kwargs):
        if request.path == '/ping':
            return JsonResponse({'message': 'pong'})
        elif request.path == '/pong':
            return JsonResponse({'message': 'ping'})
        else:
            return JsonResponse({'error': 'Not Found'}, status=404)