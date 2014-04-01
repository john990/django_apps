from django.contrib import admin
from fascinate.models import Img, Vote


class VoteInline(admin.StackedInline):
    model = Vote
    extra = 3


class ImgAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['path', 'name']}),
        ('Others', {'fields': ['width', 'height'], 'classes': ['collapse']})
    ]
    inlines = [VoteInline]


admin.site.register(Img, ImgAdmin)
