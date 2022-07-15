from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login as dj_login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from twilio.rest import Client

from . import twilio_params
from .forms import UserCreationForm, UserForm
from .models import User, Evenement


def connexion(request):
    page = 'Connexion'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        # email = request.POST.get('email')
        contact1 = request.POST.get('contact1')
        password = request.POST.get('password')
        try:
            # user = User.objects.get(email=email)
            user = User.objects.get(contact1=contact1)
        except:
            messages.error(request, 'Cet Utilisateur ne Figure pas das notre Base de Donnée, Réessayer !')

        user = authenticate(request, contact1=contact1, password=password)

        if user is not None:
            dj_login(request, user)
            # messages.success(request, '')
            return redirect('home')
        else:
            messages.error(request, 'Paramètres de Connexion Incorrect, Réessayer SVP !')

    ctx = {
        'page':page,
    }
    return render(request, 'parametres/login.html', ctx)

def deconnexion(request):
    logout(request)
    return redirect('home')

def inscription(request):
    # page = 'Inscription'
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
            message = client.messages.create(
                # messaging_service_sid='MG861a989809b54af7efa430b3b7b7e788',
                messaging_service_sid='MGb9f3bb71658713e9e34664053f5e3865',
                body='Bienvenus sur Kolia-Ci, Soutenir une Proche dans les moments Douloureux',
                to=user.contact1
            )
            print(message.sid)
            subject = 'Bienvenus sur KOLIA-CI'
            message = 'SOUTENIR UN PROCHE DANS LES MOMENTS DOULOUREUX'
            send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)
            dj_login(request, user)
            return redirect('parametres:phone_verification')
        else:
            messages.error(request, 'Une Erreur est Survenue Réessayer SVP !!')
            return redirect('inscription')

    ctx = {
        'form':form,
        # 'page':page,
    }

    return render(request, 'parametres/inscription.html', ctx)

def user_profile(request, pk):
    # user = User.objects.get(id=pk)
    user = get_object_or_404(User, id=pk)
    messages_annonces = user.message_set.all()
    annonces = user.annonces.all()
    evenements = Evenement.objects.all()
    ctx = {
        'user':user,
        'annonces':annonces,
        'evenements':evenements,
        'messages_annonces':messages_annonces,
    }
    return render(request, 'parametres/profile.html', ctx)


@login_required(login_url='connexion')
def edit_user(requests):
    user = requests.user
    form = UserForm(instance=user)
    if requests.method == "POST":
        form = UserForm(requests.POST, requests.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('parametres:user_profile', pk=user.id)

    ctx = {
        'form': form,
    }
    return render(requests, 'parametres/edit-user.html', ctx)


from django.shortcuts import render, redirect

from .forms import VerificationForm, TokenForm

account_sid = 'ACa9b3a79bcacc0ec38c29135fc5e395d1'
auth_token = '85aa55fb1024bfe53a8d05104af76b91'
# verify = client.verify.services(os.environ['TWILIO_VERIFY_SERVICE_SID'])
client = Client(account_sid, auth_token)

def verifications(phone_number, via):
    return client.verify.services(settings.TWILIO_VERIFY_SERVICE_SID).verifications.create(to=phone_number, channel=via)

def verification_checks(phone_number, token):
    return client.verify.services(settings.TWILIO_VERIFY_SERVICE_SID).verification_checks.create(to=phone_number, code=token)

def phone_verification(request):
    if request.method == 'POST':
        form = VerificationForm(request.POST)
        if form.is_valid():
            request.session['phone_number'] = form.cleaned_data['phone_number']
            verification = twilio_params.verifications(form.cleaned_data['phone_number'], form.cleaned_data['via'])
            return redirect('parametres:token_validation')
    else:
        form = VerificationForm()
    return render(request, 'parametres/phone_verification.html', {'form': form})


def token_validation(request):
    if request.method == 'POST':
        form = TokenForm(request.POST)
        if form.is_valid():
            verification = twilio_params.verification_checks(request.session['phone_number'], form.cleaned_data['token'])

            if verification.status == 'approved':
                request.session['is_verified'] = True
                return redirect('home')
            else:
                for error_msg in verification.errors().values():
                    form.add_error(None, error_msg)
    else:
        form = TokenForm()
    return render(request, 'parametres/token_validation.html', {'form': form})


def verified(request):
    if not request.session.get('is_verified'):
        return redirect('parametres:inscription')
    return render(request, 'parametres/connexion_inscription.html')
# Create your views here.
