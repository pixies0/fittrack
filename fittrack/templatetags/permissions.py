from django import template

from fittrack.permissions import SIDEBAR_PERMISSIONS

register = template.Library()


@register.filter
def can_access(user, modulo):

    if not user.is_authenticated:
        return False

    if user.is_superuser:
        return True

    grupos = SIDEBAR_PERMISSIONS.get(modulo, [])

    return user.groups.filter(name__in=grupos).exists()


@register.filter
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()
