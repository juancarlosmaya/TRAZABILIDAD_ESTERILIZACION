from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.


def listado_view(request):
    registros = [
        {'registro':"401.pdf",
        'registro_sin_extension':'401',
        'fecha':  datetime.now()
        },
        {'registro':"501.pdf",
        'registro_sin_extension':'501',
        'fecha':  datetime.now()
        },
        {'registro':"901.pdf",
        'registro_sin_extension':'901',
        'fecha':  datetime.now()
        }
    ]
    return render(request,'examinar/examinar.html',context={'registros':registros})

def detalle(request,numero):
    return HttpResponse(numero)