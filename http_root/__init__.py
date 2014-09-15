#!/usr/bin/env python
# coding: utf-8

import os
import cherrypy
from mako.template import Template

# Namespace imports
import aaa
import bbb
import ccc

THISDIR = os.path.dirname(os.path.abspath(__file__))


@cherrypy.expose
def index(*args, **kwargs):

    # Template
    template_path = os.path.join(THISDIR, "index.mako")
    template = Template(filename = template_path)

    # Render
    rendered = template.render_unicode(
        a_simple_text = u"I am 'the root'!"
    )

    # Finished
    return rendered

