# -*- coding: utf-8 -*-
"""
Markdown regex_replace filter for pelican
"""
from pelican import signals
import re

# Custom filter method
def regex_replace(s, find, replace):
    return re.sub(find, replace, s)

def add_filter(pelican):
    """Add filter to Pelican."""
    pelican.env.filters.update({'regex_replace': regex_replace})

def register():
    """Plugin registration."""
    signals.generator_init.connect(add_filter)
