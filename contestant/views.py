from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone as tz
from django.views.generic import *
from .forms import Create, Profile
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Account
from django.contrib.auth import login, logout
from django.contrib.auth.views import login_required

# Create your views here.
def home(request):
    context = {
        'title'     : 'Home',
        'messages': messages.get_messages,
    }
    return render(request, 'home.html', context)

def register(request):
    if request.user.is_authenticated:
        return redirect(to='contestant:dashboard')
    if request.method == 'POST':
        # message = messages
        form = Create(request.POST)
        if form.is_valid():
            print(" Saved ")
            form.save()
            return redirect(to='contestant:login')
        else:
            print(" not saved ")
            form = Create
            context = {'form': form,
                       'message': messages
                       }
            return render(request, 'registration/register.html', context)
    else:
        form = Create
        context = {'form': form}
        return render(request, 'registration/register.html', context)
    

def complete_profile(request):
    # if request.user.is_authenticated:
    #     return redirect(to='contestant:dashboard')
    
    current_user = request.user
    if request.method == 'POST':
        profile, created = Account.objects.get_or_create(user=current_user)
        for key, value in request.FILES:
            print(f'{Key}: {value}')
        form = Profile(request.POST,
                       request.FILES,
                       instance=current_user)
        if form.is_valid():
            image = request.POST.get('image')
            # print('Image :', image)
            # try:
            #     print('Image URL :', image.url)
            # except:
            #     print('cant fetch image url')
            current_user.account.phone = request.POST.get('phone')
            current_user.account.image = image
            current_user.account.save()
            form.save()
            return redirect(to='contestant:dashboard')
        else:
            context = {
                'form'  : Profile,
                'message': messages
            }
            return render(request, 'registration/register.html', context)
    else:
        context = {
            'message' : messages,
            'form'    : Profile
        }
        return render(request, 'registration/register.html', context)

# def save(request):
#     user = request.user
#     user.account.phone = 


@login_required(login_url='contestant:accounts/login')
def dashboard(request):
    user = User
    print(f'request: {request} ')
    context = {
        'id': user,
        'title': 'Dashboard',
        'media': settings.MEDIA_URL,
        
    }
    return render(request, 'dashboard.html', context)


def vote(request, user):
    ip = request.META['REMOTE_ADDR']
    print('IP Address is : ',ip)
    
    user = User.objects.get(username=user)
    context = {
        'user'  : user,
        'title' : "Vote"
    }
    if ip in user.account.voters:
        contestant = user.first_name + ' ' + user.last_name
        messages.error(request, message=f'You have already voted for {contestant} ')
        return redirect(to='index')
    else:
        return render(request, 'vote.html', context)

# def cant_vote(request):
    

def voted(request, user):
    contestant = User.objects.get(username=user)
    contestant.account.votes += 1
    ip = request.META['REMOTE_ADDR']
    contestant.account.voters += f'{ip}\n'
    contestant.account.save()
    profile = Account.objects.get(user=contestant)
    profile.votes += 1    
    timer = 'on'
    messages.info('Thanks for voting for me!')
    if timer == 'on':
        import time
        time.sleep(3.5)
        return redirect(to='index')
    context = {
        'user': contestant,
    }
    return render(request, 'voted.html', context)

class Leader(ListView):
    template_name = 'leaderboard.html'
    queryset = Account.objects.all().order_by('-votes')
    context_object_name = 'contestants'
    paginate_by = 50
    