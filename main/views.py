# -.- coding:utf8 -.-
from django.shortcuts import render_to_response, redirect
from django.views.decorators.cache import cache_page
from main.models import Zombie, Twit
from django.template import RequestContext
from main.forms import ZombieForm, TwitForm


@cache_page(60 * 15)
def home(request):
    zombies = Zombie.objects.all()
    return render_to_response('home.html', {'zombies': zombies, })


@cache_page(60 * 15)
def show_twits(request, pk):
    zombie = Zombie.objects.get(pk=pk)
    return render_to_response('show_twits.html', {'zombie': zombie, })


def add_zombie(request):
    form = ZombieForm()
    if request.method == 'POST':
        form = ZombieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render_to_response('add_zombie.html', {
        'form': form,
    }, RequestContext(request))


def add_twit(request):
    form = TwitForm()
    if request.method == 'POST':
        form = TwitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render_to_response('add_twit.html', {
        'form': form,
        }, RequestContext(request))


def edit_zombie(request, pk):
    zombie = Zombie.objects.get(pk=pk)
    form = ZombieForm(instance=zombie)
    if request.method == 'POST':
        form = ZombieForm(request.POST, instance=zombie)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render_to_response('add_zombie.html', {
        'form': form,
        }, RequestContext(request))


def delete_zombie(request, pk):
    zombie = Zombie.objects.get(pk)
    zombie.delete()
    return redirect('home')


def edit_twit(request, pk):
    twit = Twit.objects.get(pk=pk)
    form = TwitForm(instance=twit)
    if request.method == 'POST':
        form = TwitForm(request.POST, instance=twit)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render_to_response('add_twit.html', {
        'form': form,
        }, RequestContext(request))


def delete_twit(request, pk):
    twit = Twit.objects.get(pk=pk)
    twit.delete()
    return redirect('home')
