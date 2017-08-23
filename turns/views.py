from django.shortcuts import render
from .models import Turn
# Create your views here.

def post_turns(request):
    turn = Turn.objects.all()
    return render(request, 'turns/post_turns.html', {'turn': turn})