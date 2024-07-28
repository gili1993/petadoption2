from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def home(request):
    return render(request, 'petadoption2app/home.html')

def volunteer(request):
    return render(request, 'petadoption2app/volunteer.html')

def donate(request):
    return render(request, 'petadoption2app/donate.html')

def foster(request):
    return render(request, 'petadoption2app/foster.html')

def success_stories(request):
    return render(request, 'petadoption2app/success_stories.html')

def contact(request):
    """
    The contact view handles displaying the contact form and sending the contact message via email.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['email']
            recipients = [settings.EMAIL_HOST_USER]
            
            send_mail(subject, message, sender, recipients)
            return render(request, 'petadoption2app/contact_success.html')
    else:
        form = ContactForm()
    
    context = {'form': form}
    return render(request, 'petadoption2app/contact.html', context)

def adoption_records(request):
    return render(request, 'petadoption2app/adoption_records.html')

def adoption_process(request):
    return render(request, 'petadoption2app/adoption_process.html')

def about_us(request):
    """
    The about_us view displays information about the organization.
    """
    return render(request, 'petadoption2app/about_us.html')

def resources(request):
    """
    The resources view provides helpful information and links for pet owners and those considering adoption.
    """
    return render(request, 'petadoption2app/resources.html')


def blog_news(request):
    """
    The blog_news view displays articles, updates, news stories, and announcements related to pet adoption and the activities of the Pet Adoption Center.
    """
    # For demonstration, we'll use a static list of blog posts. In a real application, this would come from a database.
    blog_posts = [
        {
            'title': 'Welcome to Our New Blog!',
            'date': 'July 20, 2024',
            'content': 'We are excited to launch our new blog! Here, you will find the latest news, updates, and stories from the Pet Adoption Center. Stay tuned for more updates!',
            'author': 'Gili Levy'
        },
        {
            'title': 'Adoption Event Success',
            'date': 'July 15, 2024',
            'content': 'Our recent adoption event was a huge success! We found loving homes for over 30 pets. Thank you to everyone who came out and supported us.',
            'author': 'Gili Levy'
        },
        {
            'title': 'Volunteer Spotlight: Meet John Doe',
            'date': 'July 10, 2024',
            'content': 'John Doe has been a dedicated volunteer at the Pet Adoption Center for over 5 years. Learn more about his story and the amazing work he does for our organization.',
            'author': 'Gili Levy'
        }
    ]
    context = {'blog_posts': blog_posts}
    return render(request, 'petadoption2app/blog_news.html', context)


def user_account(request):
    """
    The user_account view handles user registration by displaying a registration form and processing the form data.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    
    context = {'form': form}
    return render(request, 'petadoption2app/user_account.html', context)


def privacy_security(request):
    return render(request, 'petadoption2app/privacy_security.html')

def available_pets(request):
    """
    The privacy_security view displays information about the organization's privacy policies and security measures.
    """
    return render(request, 'petadoption2app/available_pets.html') 

def adoption_application(request):
    return render(request, 'petadoption2app/adoption_application.html')

def available_pets(request):
    # For demonstration, we will use a static list of pets. In a real application, this would come from a database.
    pets = [
        {'name': 'Buddy', 'species': 'Dog', 'age': 3, 'description': 'A friendly and energetic dog.'},
        {'name': 'Whiskers', 'species': 'Cat', 'age': 2, 'description': 'A calm and affectionate cat.'},
        {'name': 'Thumper', 'species': 'Rabbit', 'age': 1, 'description': 'A playful and curious rabbit.'},
    ]
    context = {'pets': pets}
    return render(request, 'petadoption2app/available_pets.html', context)

def success_stories(request):
    stories = [
        {
            'title': "Max's Story",
            'image': 'images/max.jpg',
            'content': 'Max was found as a stray, and after spending some time in our shelter, he found his forever home with the Smith family. He is now a cherished family member who loves to play and cuddle.',
            'author': 'The Smith Family'
        },
        {
            'title': "Bella's Story",
            'image': 'images/bella.jpg',
            'content': 'Bella was a shy kitten who blossomed into a confident and playful cat after being adopted by Lisa Brown. She now enjoys sunbathing and playing with her toys.',
            'author': 'Lisa Brown'
        },
        {
            'title': "Charlie’s Story",
            'image': 'images/charlie.jpg',
            'content': 'Charlie was an older dog with a calm demeanor. He found his perfect match with the Johnson family, who appreciate his gentle nature and loving personality.',
            'author': 'The Johnson Family'
        }
    ]
    context = {'stories': stories}
    return render(request, 'petadoption2app/success_stories.html', context)

