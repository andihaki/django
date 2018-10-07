from django import template

register = template.Library()

# @register = decorator. menggantikan pemanggilan yang adaa di bawah
@register.filter(name='cut')
def cut(value, arg):
    """
    this cuts out all value of 'arg' from string
    """

    return value.replace(arg, '')

# # 'cut' = nama filternya
# # cut = function nya
# register.filter('cut', cut)