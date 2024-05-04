from django.contrib import admin
from main.models import Contact, Company


@admin.register(Contact)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('email', 'country', 'city', 'street', 'house_number', 'company')
    search_fields = ('city',)

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        search_term_lower = search_term.title()
        queryset |= self.model.objects.filter(city__icontains=search_term_lower)
        return queryset, use_distinct


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'provider', 'debt', 'date_created')
    actions = ['clear_debt']

    def clear_debt(self, request, queryset):
        queryset.update(debt=0)

    clear_debt.short_description = 'Очистить задолженность'
