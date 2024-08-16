from django.shortcuts import render
from django.views.decorators.http import require_POST
from .models import tree  

def predict(request):
    prediction = None
    if request.method == 'POST':
        age = int(request.POST.get('age'))
        gender = request.POST.get('gender')
        prediction = tree.predict(age, gender)
        
    return render(request, 'pages/index.html', {'prediction': prediction})
