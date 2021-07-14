from django.shortcuts import render

def home(request):
    print(request.GET)
    print("queryset")
    
    return render(
        request, 
        './home.html'
    )