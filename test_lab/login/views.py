#from django.core.context_processors import csrf
#from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse


# Create your views here.
class LoginView(View):
    
    #@csrf_exempt
    def get(self, request):
        return render(request, 'login/index.html')

    #@csrf_exempt
    def post(self, request):
        html = '<html><body>'
        for k, v in request.POST.items():
            html += f'{k}: {v}<br>'
        html += '</body></html>'
        return HttpResponse(html)

