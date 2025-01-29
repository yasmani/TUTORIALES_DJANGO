from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings



# Create your views here.

def formulariocontacto(request):
    return render(request, "formularioContacto.html")


def contactar(request):
    if request.method == "POST":
        asunto=request.POST["txtasunto"]
        mensaje = request.POST["txtmensaje"] + "/ Email: " + request.POST["txtemail"]
        email_desde = settings.EMAIL_HOST_USER
        email_para = ["yasmani.gutierrez03@gmail.com"]
        send_mail(asunto, mensaje, email_desde, email_para,fail_silently=False)
        return render(request, "contactoexitoso.html")
    return render(request, "formularioContacto.html")