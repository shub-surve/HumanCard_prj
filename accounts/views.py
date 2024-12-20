from django.shortcuts import render, redirect
from django.contrib.auth import login , authenticate , logout
from django.core.mail import send_mail
from django.conf import settings
from django.core.files.base import ContentFile
from .forms import UserRegistrationForm, HumanCardForm , UserLoginForm , ContactForm
from .models import HumanCard
import base64
import uuid
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import HumanCardSerialized

def homepage(request):
    # human_card = HumanCard.objects.get(request.user)
    return render(request , 'home.html' )

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        human_card_form = HumanCardForm(request.POST)

        if user_form.is_valid() and human_card_form.is_valid():
            # Create and save user
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            # Create HumanCard
            human_card = human_card_form.save(commit=False)
            human_card.user = user
            human_card.email = user.email

            # Handle profile picture
            profile_pic_data = request.POST.get('profile_pic')
            if profile_pic_data:
                try:
                    format, imgstr = profile_pic_data.split(';base64,')
                    ext = format.split('/')[-1]  # Extract file extension
                    profile_pic = ContentFile(base64.b64decode(imgstr), name=f"{user.username}_profile_pic.{ext}")
                    human_card.profile_pic.save(profile_pic.name, profile_pic)
                except Exception as e:
                    print(f"Error processing profile picture: {e}")

            human_card.save()

            # Send verification email
            verification_token = str(uuid.uuid4())
            verification_link = f"http://localhost:8000/verify/{verification_token}/"
            send_mail(
                'Verify your email',
                f'Click the link to verify your email: {verification_link}',
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                fail_silently=False,
            )
            print(human_card.humancard_id)
            return redirect('email_sent')  # Redirect to login after successful registration
    else:
        user_form = UserRegistrationForm()
        human_card_form = HumanCardForm()

    return render(request, 'register.html', {'user_form': user_form, 'human_card_form': human_card_form})

def email_sent(request):
    return render(request , 'email_sent.html')

def user_login(request):
    # print(request.user.token)
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to a home page or dashboard after login
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = UserLoginForm()

    return render(request, 'login.html', {'form': form})

def verify_email(request, token):
    return render(request, 'verification_success.html')

def logout_view(request): 
    logout(request) 
    return redirect('home')

def contact_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = HumanCard.objects.filter(email=email).first()
            print(user)
            if user:
                first_name = user.first_name
                print(first_name)
            else:
                first_name = "User"
            
            send_mail(
                'Query Received',
                f'Dear {first_name},\nWe have received your query.\nWe will revert to solve it.\nThanks for reaching out.',
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False
            )
            form.save()
            return redirect('query_received')
    else:
        form = ContactForm()
        
    return render(request, 'contactpage.html', {'form': form, 'title': 'ContactPage'})

def view_profile(request):
    human_card = HumanCard.objects.get(user = request.user)
    return render(request , 'profile.html' , {"human_card" :human_card})


class HumanCard_API(APIView):
    def get(self , request):
        if request.user.is_superuser:
            human_card = HumanCard.objects.all()
            serializer = HumanCardSerialized(human_card , many=True)
            print(serializer.data)
            return Response(serializer.data)
        else:
            return Response({'error': 'You are not allowed to use the API'} , status=status.HTTP_403_FORBIDDEN)

