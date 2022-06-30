from django.contrib import admin

class PostAdmin(admin.ModelAdmin):
    list_display = ['text_preview', 'author', 'created_at']
    autocomplete_fields = ['author']
    readonly_fields = ['created_at']

    def text_preview(self, obj):
        return f"{obj.text[:10]}..."

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj=obj)
        if obj is None:
            fields.remove('created_at')
        return fields