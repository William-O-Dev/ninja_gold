from django.shortcuts import render, redirect
import random
from time import gmtime, strftime

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []
    
    return render(request, 'index.html')

def process_money(request):
    if request.POST['choice'] == 'farm':
        your_gold = random.randint(10,20)
        request.session['gold'] += your_gold
        activity = f"Earned {your_gold} gold from the {request.POST['choice']}! ({strftime('%Y.%m.%d %H:%M %p', gmtime())})"
        request.session['activities'].insert(0,(activity, "earned"))

    if request.POST['choice'] == 'cave':
        your_gold = random.randint(5, 10)
        request.session['gold'] += your_gold
        activity = f"Earned {your_gold} gold from the {request.POST['choice']}! ({strftime('%Y.%m.%d %H:%M %p', gmtime())})"
        request.session['activities'].insert(0, (activity, "earned"))

    if request.POST['choice'] == 'house':
        your_gold = random.randint(2,5)
        request.session['gold'] += your_gold
        activity = f"Earned {your_gold} gold from the {request.POST['choice']}! ({strftime('%Y.%m.%d %H:%M %p', gmtime())})"
        request.session['activities'].insert(0, (activity, "earned"))

    if request.POST['choice'] == 'casino':
        your_gold = random.randint(-50,50)
        request.session['gold'] += your_gold
        if your_gold >= 0:
            activity = f"Earned {your_gold} gold from the {request.POST['choice']}! ({strftime('%Y.%m.%d %H:%M %p', gmtime())})"
            result = "earned"
        else:
            your_gold = your_gold * -1
            activity = f"Entered a {request.POST['choice']} and lost {your_gold} gold...ouch! ({strftime('%Y.%m.%d %H:%M %p', gmtime())})"
            result = "lost"
        request.session['activities'].insert(0, (activity, result))

    return redirect('/')
