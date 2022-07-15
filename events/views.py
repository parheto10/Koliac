from django.contrib import messages
from django.contrib.auth import authenticate, login as dj_login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from parametres.models import Evenement, User
from .forms import AnnonceForm, AnnonceUpdateForm
from .models import Annonce, Message
from datetime import datetime, date


def home(request):
    q = request.GET.get('q') if request.GET.get('q') !=None else ''

    annonces = Annonce.objects.filter(
        Q(categorie__nom__icontains=q) |
        Q(titre__icontains= q) |
        Q(programme__icontains= q)
    )
    evenements = Evenement.objects.all().order_by('nom')[0:5]
    annonces_count = annonces.count()
    messages_annonces = Message.objects.filter(
        Q(annonce__categorie__nom__contains=q)
    )[:5]

    ctx = {
        'annonces': annonces,
        'evenements': evenements,
        'annonces_count': annonces_count,
        'messages_annonces': messages_annonces,
    }
    return render(request, 'events/home.html', ctx)


def annonce(request, pk):
    annonce = get_object_or_404(Annonce, id=pk)
    annonce_messages = annonce.message_set.all().order_by('-created_le')
    participants = annonce.participant.all()
    if request.method=='POST':
        message = Message.objects.create(
            user=request.user,
            annonce=annonce,
            contenu=request.POST.get('contenu')
        )
        annonce.participant.add(request.user)
        return redirect('annonce', pk=annonce.id)

    ctx = {
        'annonce': annonce,
        'annonce_messages': annonce_messages,
        'participants': participants,
    }

    return render(request, 'events/annonce.html', ctx)

@login_required(login_url='connexion')
def add_annonce(request):
    form = AnnonceForm
    evenements = Evenement.objects.all()
    if request.method == 'POST':
        categorie = request.POST.get("categorie")
        categorie, created = Evenement.objects.get_or_create(nom=categorie)
        Annonce.objects.create(
            user=request.user,
            categorie=categorie,
            date=request.POST.get('date'),
            carte_annonce=request.POST.get('carte_annonce'),
            titre=request.POST.get('titre'),
            programme=request.POST.get('programme'),
        )
        return redirect('home')
    ctx = {
        'form': form,
        'evenements': evenements,
    }
    return render(request, 'events/create_annonce.html', ctx)

@login_required(login_url='connexion')
def update_annonce(request, pk):
    d_date = 1
    annonce = get_object_or_404(Annonce, id=pk)
    form = AnnonceUpdateForm(instance=annonce)
    evenements = Evenement.objects.all()
    # month, day, year = annonce.date.strftime(annonce.date)
    # annonce.date = '-'.join([year, month, day]) + ' 00:00:00'

    if request.user != annonce.user:
        return HttpResponse("Vous n'êtes pas l'auteur de ce groupe, impossible de le Modifier !")

    if request.method == 'POST':
        categorie_name = request.POST.get("categorie")
        categorie, created = Evenement.objects.get_or_create(nom=categorie_name)
        form = AnnonceUpdateForm(request.POST, instance=annonce)
        annonce.titre = request.POST.get('titre')
        annonce.date = request.POST.get('date')
        # annonce.date = date.strftime(request.POST.get('date'), 'YYYY-mm-dd')
        # annonce.date = date.strftime(request.POST.get('date'), '%Y-%m-%d %H:%M:%S')
        # # annonce.date = date.strftime(request.POST.get('date'), 'YYYY-mm-dd')
        annonce.programme = request.POST.get('programme')
        annonce.carte_annonce = request.POST.get('carte_annonce')
        annonce.categorie = categorie
        annonce.save()
        return redirect('home')
    ctx = {
        'form' : form,
        'evenements': evenements,
        'annonce' : annonce,
        'd_date':d_date,
    }
    return render(request, 'events/create_annonce.html', ctx)


@login_required(login_url='connexion')
def delete_message(request, pk=None):
    obj = get_object_or_404(Message, id=pk)

    if request.user != obj.user:
        HttpResponse("Vous n'êtes pas l'auteur de ce groupe, impossible de le Supprimer !")

    if request.method == 'POST':
        obj.delete()
        return redirect('home')
    ctx = {
        'obj': obj
    }
    return render(request, 'events/supprimer.html', ctx)
# Create your views here.
