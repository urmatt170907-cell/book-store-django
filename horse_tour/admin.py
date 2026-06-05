from django.contrib import admin
from .models import Tourist, Horse, TourCategory, HorseTour, Comment

@admin.register(Tourist)
class TouristAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'passport_id')
    search_fields = ('fullname', 'passport_id')

@admin.register(Horse)
class HorseAdmin(admin.ModelAdmin):
    list_display = ('name', 'booked_by')
    search_fields = ('name',)

@admin.register(TourCategory)
class TourCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(HorseTour)
class HorseTourAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')
    search_fields = ('title',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('tour', 'created_at')
    list_filter = ('created_at',)
