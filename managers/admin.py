from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Manager


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ["username", "number", "email", "created_at", "amount_of_trade"]

    fieldsets = (
        (
            'Менеджеры',
            {
                "classes": ("wide",),
                "fields": ("username", "number", "email", "password"),
            },
        ),
    )

    add_fieldsets = (
        (
            'Менеджеры',
            {
                "classes": ("wide",),
                "fields": ("username", "number", "email", "password",),
            },
        ),
    )


    def save_model(self, request, obj, form, change):
        obj.set_password(form.cleaned_data["password"])  # Хешируем пароль
        super().save_model(request, obj, form, change)


