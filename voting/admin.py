from django.contrib import admin

from .models import Bandmate, Groupname, Vote


admin.site.register(Bandmate)
admin.site.register(Groupname)
admin.site.register(Vote)
