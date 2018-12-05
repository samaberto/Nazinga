from django import template
import datetime

register = template.Library()

def hora_actual(format_string):
    return datetime.datetime.now().strftime(format_string)

register.simple_tag(hora_actual)