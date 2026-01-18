from .models import Role


def requiredGroups(permission):
    """Get required groups for a permission. Returns a callable class for use as permission class."""
    return _RequiredGroupsPermission(permission)


class _RequiredGroupsPermission:
    """Lazy-evaluated permission class that queries database only on request."""
    
    def __init__(self, permission):
        self.permission = permission
        self._groups = None
    
    @property
    def groups(self):
        """Lazily load groups from database."""
        if self._groups is None:
            roles = Role.objects.filter(permissions__icontains=self.permission)
            self._groups = ['admin']
            for role in roles:
                if role.name.lower() != 'admin':  # admin already added
                    self._groups.append(role.name)
        return self._groups
    
    def __iter__(self):
        """Make it iterable for backward compatibility."""
        return iter(self.groups)