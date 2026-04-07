from django.shortcuts import render, redirect
from .models import FlightModel
from .forms import CreateFlight

def index(request):
    query = request.GET.get('query')
    
    new_date = request.GET.get('new_date')
    new_price = request.GET.get('new_price')
    
    flys = FlightModel.objects.all()
    query_result = None
    combinate_result = None
    
    if query:
        query_result = flys.filter(description__icontains=query)
        
    if new_date and new_price:
        combinate_result = flys.filter(
            date=new_date,
            price_ticket=new_price
        )
        
    if request.method == 'POST':
        form = CreateFlight(request.POST)
        if form.is_valid():
            fly = form.save(commit=False)
            fly.save()
            return redirect('index')
        
    else:
        form = CreateFlight()
        
    return render(request, 'main/index.html', {
        'flys': flys,
        'query': query,
        'new_date': new_date,
        'new_price': new_price,
        
        'form': form,
        'title': 'Рейсы',
        
        'query_result': query_result,
        'combinate_result': combinate_result
    })
    
def delete(request):
    if request.method == 'POST':
        fly = FlightModel.objects.get(id=request.POST['id'])
        fly.delete()
        return redirect('index')

# Create your views here.
