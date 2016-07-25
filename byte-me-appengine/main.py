#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
<<<<<<< HEAD
import webapp2
import jinja2
import os

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(template_dir)
)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
=======
from google.appengine.ext import ndb
import jinja2
import logging
import os
import urllib2
import urllib2
import webapp2

class User(webapp2.RequestHandler):
        zip_code = ndb.IntegerProperty(required=True)
        gender = ndb.BooleanProperty(required=True)
        body_temp = ndb.BooleanProperty(required=True)

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(template_dir))

#handler for main page
class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Welcome to Induviae!')
        # template = jinja_environment.get_template('main.html')
        # self.response.write(template.render())


    # def post(self):
        #template = jinja_environment.get_template('input.html')
        #how do I transition the main page to the input page? Do I need a separate handler?
        #self.response.write(template.render())
        # user_location = self.request.get('') #change info in quotes to correspond to input.html input variables
        # user_gender = self.request.get('')
        # user_temp = self.request.get('')
        # user = User(zip_code=user_location, gender=user_gener, body_temp=user_temp)
        # key = user.put()


class OutputHandler(webapp2.RequestHandler):
    def get(self):
        # template = jinja_environment.get_template('output.html')
        # self.response.write(template.render({explanation}))

        #setting up the weather api, used meme example
        #API key = d18790d3f622ff63af5b3fc8902387db
        req = "http://api.openweathermap.org/data/2.5/weather?zip="+user.zip_code+",us&appid=d18790d3f622ff63af5b3fc8902387db"
        response = urllib2.urlopen(req)
        response_text = response.read()
        response_data = json.loads(response_text)
        outside_avg_temp = response_data['main']['temp'])
        outside_humidity = response_data['main']['humidity']
        outside_min_temp = response_data['main']['temp_min']
        outside_max_temp = response_data['main']['temp_max']
        wind_speed = response_data['wind']['speed']



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/outfit', OutputHandler)
>>>>>>> dc55d159d17910bd6a0789587d94d5b755087a68
], debug=True)
