import email
from django.shortcuts import render
from app.models import Comments
from django.contrib import messages


def home(request):
    print(request)
    print("queryset")
    
    if "POST"==request.method:
        print("POSTFSDFSDF")
    #    import pdb; pdb.set_trace()
        nombre = request.POST['nombre']
        correo = request.POST['correo']
        comentario = request.POST['comentario']
        Comments.objects.create(
            email = correo,
            name =  nombre,
            comment = comentario,
        )
        messages.success(request, "Mensaje enviado!")
        
    return render(
        request, 
        './home.html'
         
    )