from django.shortcuts import render
from django import template

register = template.Library();

@register.inclusion_tag('info_box.html')
def info_box(value):
    return {'value': value};