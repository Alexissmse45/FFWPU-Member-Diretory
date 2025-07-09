# directory/permissions.py
from rest_framework import permissions

class IsSuperAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow superadmins to create, edit, or delete.
    Regular admins can only read.
    """
    
    def has_permission(self, request, view):
        # Allow access to authenticated users
        if not request.user.is_authenticated:
            return False
        
        # Read permissions are allowed to any authenticated user
        if request.method in permissions.READONLY_METHODS:
            return True
        
        # Write permissions only for superadmins
        return hasattr(request.user, 'is_superadmin') and request.user.is_superadmin