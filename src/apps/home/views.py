from django.http import JsonResponse

# Create your views here.
from django.views.generic import TemplateView

TEMPLATE_URL = 'home'


def health_check(request):
    return JsonResponse({'status': 'ok'})

class HomepageView(TemplateView):
    template_name = f'{TEMPLATE_URL}/home.html'