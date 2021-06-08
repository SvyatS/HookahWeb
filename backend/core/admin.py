from django.contrib import admin

from .models import *


admin.site.register(ExtendedUser)
admin.site.register(Table)
admin.site.register(Reserve)
admin.site.register(Review)
admin.site.register(Product)


