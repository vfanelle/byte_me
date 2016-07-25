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
from google.appengine.ext import ndb
import jinja2
import logging
import os
import urllib
import urllib2
import webapp2

class User(webapp2.RequestHandler):
        zip_code = ndb.IntegerProperty(required=True)
        country_code = ndb.IntegerProperty(required=True)
        gender = ndb.BooleanProperty(required=True)
        body_temp = ndb.BooleanProperty(required=True)

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(template_dir))

#handler for main page
class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('input.html')
        self.response.write(template.render())

    
class OutputHandler(webapp2.RequestHandler):
    def post(self):
        user_zip = self.request.get('zip_code') #change info in quotes to correspond to input.html input variables
        user_country = self.request.get('country_code')
        user_gender =   self.request.get('gender')
        user_temp = self.request.get('average_feel')
        user = User(zip_code=user_zip, country_code=user_country, gender=user_gener, body_temp=user_temp)
        key = user.put()

        template = jinja_environment.get_template('output.html')
        self.response.write(template.render({explanation}))

        #setting up the weather api, used meme example
        #API key = d18790d3f622ff63af5b3fc8902387db
        req = "http://api.openweathermap.org/data/2.5/weather?zip="+user.zip_code+",us&appid=d18790d3f622ff63af5b3fc8902387db"
        response = urllib2.urlopen(req)
        response_text = response.read()
        response_data = json.loads(response_text)
        outside_avg_temp = response_data['main']['temp']
        outside_humidity = response_data['main']['humidity']
        outside_min_temp = response_data['main']['temp_min']
        outside_max_temp = response_data['main']['temp_max']
        wind_speed = response_data['wind']['speed']

        template = jinja_environment.get_template('output.html')
        html = template.render({'output_weather_img':weather_img})

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/outfit', OutputHandler)
], debug=True)
