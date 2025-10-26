from django.contrib import admin
from .models import LearningJourney

@admin.register(LearningJourney)
class LearningJourneyAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_added')      # Show title and date in admin list
    search_fields = ('title', 'description')    # Enable search by title or description

