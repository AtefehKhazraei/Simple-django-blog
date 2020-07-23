from django.contrib import admin
from .models import post

#Editing what data we want to see on the list wich shows on admin page
class PostAdmin(admin.ModelAdmin):
    list_display = ["title","__str__","timestamp","updated",]
    list_display_links = ["updated"]
    list_filter = ["updated","timestamp"]
    list_editable = ["title"]
    search_fields = ["title","content"]
    class meta:
        model=post
# Register your models here.
admin.site.register(post,PostAdmin)

