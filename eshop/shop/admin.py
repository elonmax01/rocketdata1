from django.contrib import admin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.http import urlencode
from .models import Factory, Distributor, Dealer, Retailer, IE, Address, Product, Employee
from django.urls import path

# Register your models here.
    

class FactoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'email', 'debt', 'created_on', 'view_products_link', 'view_employees_link')
    list_filter = ('address__city',)
    actions = ['clear_debts']

    def view_products_link(self, obj):
        from django.utils.html import format_html
        count = obj.product_set.count()
        url = (
            reverse("admin:shop_product_changelist")
            + "?"
            + urlencode({"factorys_id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Products</a>', url, count)
    
    view_products_link.short_description = 'Products'

    def view_employees_link(self, obj):
        from django.utils.html import format_html
        count = obj.employee_set.count()
        url = (
            reverse("admin:shop_employee_changelist")
            + "?"
            + urlencode({"factorys_id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Employees</a>', url, count)
    
    view_employees_link.short_description = 'Employees'

    @admin.action(description='Clear all debts')
    def clear_debts(modeladmin, request, queryset):
        queryset.update(debt=0)

class DistributorAdmin(admin.ModelAdmin):
    list_display = ('name', 'link_supplier', 'address', 'email', 'debt', 'created_on', 'view_products_link', 'view_employees_link')
    list_filter = ('address__city',)
    actions = ['clear_debts']

    def view_products_link(self, obj):
        from django.utils.html import format_html
        count = obj.product_set.count()
        url = (
            reverse("admin:shop_product_changelist")
            + "?"
            + urlencode({"distributors_id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Products</a>', url, count)
    
    view_products_link.short_description = 'Products'

    def view_employees_link(self, obj):
        from django.utils.html import format_html
        count = obj.employee_set.count()
        url = (
            reverse("admin:shop_employee_changelist")
            + "?"
            + urlencode({"distributors_id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Employees</a>', url, count)
    
    view_employees_link.short_description = 'Employees'

    def link_supplier(self, obj):
        from django.utils.html import format_html
        return format_html('<a href="{}">{}</a>', reverse('admin:shop_factory_change', args=[obj.factory_id]), obj.factory.name)

    link_supplier.short_description = 'Supplier'

    @admin.action(description='Clear all debts')
    def clear_debts(modeladmin, request, queryset):
        queryset.update(debt=0)

class DealerAdmin(admin.ModelAdmin):
    list_display = ('name', 'link_supplier', 'address', 'email', 'debt', 'created_on', 'view_products_link', 'view_employees_link')
    list_filter = ('address__city',)
    actions = ['clear_debts']

    def view_products_link(self, obj):
        from django.utils.html import format_html
        count = obj.product_set.count()
        url = (
            reverse("admin:shop_product_changelist")
            + "?"
            + urlencode({"dealers_id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Products</a>', url, count)
    
    view_products_link.short_description = 'Products'

    def view_employees_link(self, obj):
        from django.utils.html import format_html
        count = obj.employee_set.count()
        url = (
            reverse("admin:shop_employee_changelist")
            + "?"
            + urlencode({"dealers_id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Employees</a>', url, count)
    
    view_employees_link.short_description = 'Employees'

    @admin.action(description='Clear all debts')
    def clear_debts(modeladmin, request, queryset):
        queryset.update(debt=0)

    def link_supplier(self, obj):
        from django.utils.html import format_html
        if obj.distributor:
            return format_html('<a href="{}">{}</a>', reverse('admin:shop_distributor_change', args=[obj.distributor_id]), obj.distributor.name)
        elif obj.factory:
            return format_html('<a href="{}">{}</a>', reverse('admin:shop_factory_change', args=[obj.factory_id]), obj.factory.name)
        else:
            return None

    link_supplier.short_description = 'Supplier'

class RetailerAdmin(admin.ModelAdmin):
    list_display = ('name', 'link_supplier', 'address', 'email', 'debt', 'created_on', 'view_products_link', 'view_employees_link')
    list_filter = ('address__city',)
    actions = ['clear_debts']

    def view_products_link(self, obj):
        from django.utils.html import format_html
        count = obj.product_set.count()
        url = (
            reverse("admin:shop_product_changelist")
            + "?"
            + urlencode({"retailers_id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Products</a>', url, count)
    
    view_products_link.short_description = 'Products'

    def view_employees_link(self, obj):
        from django.utils.html import format_html
        count = obj.employee_set.count()
        url = (
            reverse("admin:shop_employee_changelist")
            + "?"
            + urlencode({"retailers_id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Employees</a>', url, count)
    
    view_employees_link.short_description = 'Employees'

    def link_supplier(self, obj):
        from django.utils.html import format_html
        if obj.dealer:
            return format_html('<a href="{}">{}</a>', reverse('admin:shop_dealer_change', args=[obj.dealer_id]), obj.dealer.name)
        elif obj.distributor:
            return format_html('<a href="{}">{}</a>', reverse('admin:shop_distributor_change', args=[obj.distributor_id]), obj.distributor.name)
        elif obj.factory:
            return format_html('<a href="{}">{}</a>', reverse('admin:shop_factory_change', args=[obj.factory_id]), obj.factory.name)
        else:
            return None

    link_supplier.short_description = 'Supplier'

    @admin.action(description='Clear all debts')
    def clear_debts(modeladmin, request, queryset):
        queryset.update(debt=0)

class IEAdmin(admin.ModelAdmin):
    list_display = ('name', 'link_supplier', 'address', 'email', 'debt', 'created_on', 'view_products_link', 'view_employees_link')
    list_filter = ('address__city',)
    actions = ['clear_debts']

    def view_products_link(self, obj):
        from django.utils.html import format_html
        count = obj.product_set.count()
        url = (
            reverse("admin:shop_product_changelist")
            + "?"
            + urlencode({"ies_id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Products</a>', url, count)
    
    view_products_link.short_description = 'Products'

    def view_employees_link(self, obj):
        from django.utils.html import format_html
        count = obj.employee_set.count()
        url = (
            reverse("admin:shop_employee_changelist")
            + "?"
            + urlencode({"ies_id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Employees</a>', url, count)
    
    view_employees_link.short_description = 'Employees'

    def link_supplier(self, obj):
        from django.utils.html import format_html
        if obj.retailer:
            return format_html('<a href="{}">{}</a>', reverse('admin:shop_retailer_change', args=[obj.retailer_id]), obj.retailer.name)
        elif obj.dealer:
            return format_html('<a href="{}">{}</a>', reverse('admin:shop_dealer_change', args=[obj.dealer_id]), obj.dealer.name)
        elif obj.distributor:
            return format_html('<a href="{}">{}</a>', reverse('admin:shop_distributor_change', args=[obj.distributor_id]), obj.distributor.name)
        elif obj.factory:
            return format_html('<a href="{}">{}</a>', reverse('admin:shop_factory_change', args=[obj.factory_id]), obj.factory.name)
        else:
            return None
        
    link_supplier.short_description = 'Supplier'

    @admin.action(description='Clear all debts')
    def clear_debts(modeladmin, request, queryset):
        queryset.update(debt=0)

class AddressAdmin(admin.ModelAdmin):
    pass

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'plant', 'display_dealers', 'display_distributors', 'display_retailers', 'display_ies', 'model', 'price', 'date_of_birth')

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'display_company')


admin.site.register(Factory, FactoryAdmin)
admin.site.register(Distributor, DistributorAdmin)
admin.site.register(Dealer, DealerAdmin)
admin.site.register(Retailer, RetailerAdmin)
admin.site.register(IE, IEAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Employee, EmployeeAdmin)
