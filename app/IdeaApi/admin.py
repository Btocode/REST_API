from django.contrib import admin

from .models import Idea, Notification, Suggestion, User

# Register your models here.
# admin.site.register(User)
# admin.site.register(Idea)
# admin.site.register(Notification)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("userId","firstName", "email", "age")
@admin.register(Idea)
class IdeaAdmin(admin.ModelAdmin):
    list_display = ("ideaId","ideatitle", "ideatags","user")

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ("notiId","notiType","user")
@admin.register(Suggestion)
class SuggestionAdmin(admin.ModelAdmin):
    list_display = ("user","ideaId","content")



