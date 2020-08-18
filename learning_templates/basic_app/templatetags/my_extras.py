from django import template


register = template.Library()

@register.filter(name='cut1')
def cut1(value, arg):
    """
    cuts args off value
    """

    return value.replace(arg, '')


#register.filter('cut1', cut1)