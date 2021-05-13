from django.contrib import admin
from .models import admin_model,user_models,login_user,can_book_call,all_book_call

# Register your models here.

admin.site.register(admin_model)
admin.site.register(user_models)
admin.site.register(login_user)
admin.site.register(can_book_call)
admin.site.register(all_book_call)