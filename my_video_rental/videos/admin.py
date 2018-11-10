from django.contrib import admin

# Register your models here.
from . import models

# hmm
class MovieAdmin(admin.ModelAdmin):
    # ordering field
    fields = ['release_year', 'title', 'length']
    
    # fungsi search
    # tambahin di bawah, admin.site.register
    search_fields = ['title']

    # menu filter di sebelah kanan
    list_filter = ['release_year']

    # nambahin tambahan data di list
    list_display = ['title', 'release_year', 'length']

    list_editable = ['length']

class CustomerAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name']

admin.site.register(models.Customer)
admin.site.register(models.Movie, MovieAdmin)