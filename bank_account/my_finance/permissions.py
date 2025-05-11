from rest_framework import permissions

class IsAdminOrOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        # Разрешаем все запросы для аутентифицированных пользователей
        return request.user and request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        return bool((obj.id == request.user.id) or request.user.is_staff)