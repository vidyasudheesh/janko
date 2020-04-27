from django.contrib import admin
from . models import Snippet


class SnippetAdmin(admin.ModelAdmin):
    list_display = ('Name','Algorithem','Style','Language','Length','Paper')


admin.site.register(Snippet , SnippetAdmin)

# Register your models here.
