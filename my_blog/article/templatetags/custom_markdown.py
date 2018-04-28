# !usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:dandan.zheng 
@file: custom_markdown.py 
@time: 2018/04/28 
"""
from django import template
from django.utils.safestring import mark_safe
from django.template.defaultfilters import stringfilter
import markdown

register = template.Library()


@register.filter(is_safe=True)
@stringfilter

def custom_markdown(value):
    return mark_safe(markdown.markdown(value,
                                       extentions=['markdown.extensions.fenced_code', 'markdown.extensions.codehilite'],
                                       safe_mode=True,
                                       enable_attributes=True))

