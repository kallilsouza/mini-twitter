from django.contrib import admin

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_active', 'followers_count']
    search_fields = ['user__username']
    autocomplete_fields = ['user', 'followers']
    
    def is_active(self, obj):
        return obj.user.is_active
    is_active.boolean = True

    def followers_count(self, obj):
        return obj.followers.count()