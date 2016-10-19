from django import template


register = template.Library()


@register.filter(name='has_group')
def has_group(user, group_name):
    return True if user.groups.filter(name=group_name).exists() else False