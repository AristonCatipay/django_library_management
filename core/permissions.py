from rest_framework.permissions import BasePermission

class IsStaffOrReadOnly(BasePermission):
    """
    Custom permission to only allow staff members and members of the staff group to create, update, or delete courses.
    """

    def has_permission(self, request, view):
        # Allow read-only permissions for GET, HEAD, or OPTIONS requests.
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        
        # Check if the user is staff or belongs to the 'staff' group for other request methods.
        return request.user.is_staff or 'staff' in [group.name for group in request.user.groups.all()]

class UnauthenticatedOnly(BasePermission):
    def has_permission(self, request, view):
        return not request.user.is_authenticated