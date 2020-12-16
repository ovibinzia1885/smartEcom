from django.contrib import admin

from product.models import Category,Product,Images

admin.site.register(Category)
admin.site.register(Images)
class productImages(admin.TabularInline):
        model=Images
        extra = 5


class ProductAdmin(admin.ModelAdmin):
        list_display = ['title', 'status', 'created_at', 'updated_at', 'image']
        list_filter = ['title', 'created_at']
        list_per_page = 10
        search_fields = ['title', 'new_price', 'detail']
        inlines = [productImages]
admin.site.register(Product,ProductAdmin)
