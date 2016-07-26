from google.appengine.ext import ndb
import jinja2
import json
import logging
import os
import urllib
import urllib2
import webapp2

#tells jinja2 where to look for future files
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(template_dir))

#should I connect OutputHandler to outfits.py to display an outfit?

class FemaleTop(ndb.Model):
    shirt =
    min_temp = ndb.StringProperty(required=True)
    max_temp = ndb.StringProperty(required=True)

class FemaleBottom(ndb.Model):
    bottom =
    min_temp = ndb.StringProperty(required=True)
    max_temp = ndb.StringProperty(required=True)

class FemaleShoes(ndb.Model):
    shoes =
    min_temp = ndb.StringProperty(required=True)
    max_temp = ndb.StringProperty(required=True)

class MaleTop()
