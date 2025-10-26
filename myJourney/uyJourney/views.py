from django.shortcuts import render
from .models import LearningJourney, AboutMe


def index(request):
    # Fetch all LearningJourney entries from the database
    journeys = LearningJourney.objects.all().order_by('-date_added')

    # Pass them to the template
    return render(request, 'index.html', {'journeys': journeys})

def about_html(request):
    # Get HTML-related learning entries
    topics = LearningJourney.objects.all().order_by('-date_added')
    about_info = AboutMe.objects.first()  # Get the AboutMe information
    context = {
        'topics': topics,
        'about': about_info
    }
    return render(request, 'aboutMe.html', context)