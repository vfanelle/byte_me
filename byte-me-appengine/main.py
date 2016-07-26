from google.appengine.ext import ndb
import jinja2
import json
import logging
import os
import urllib
import urllib2
import webapp2
import outfits

#defines a user object
class User(ndb.Model):
        user_city = ndb.StringProperty(required=True)
        user_state = ndb.StringProperty(required=True)
        user_gender = ndb.StringProperty(required=True)
        user_temp = ndb.StringProperty(required=True)

#tells jinja2 where to look for future files
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(template_dir))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('main.html')
        self.response.write(template.render())

#handler for main page to display input.html
class InputHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('input.html')
        self.response.write(template.render())

#handler to display output page and save user's input into a user object
class OutputHandler(webapp2.RequestHandler):

    def get(self):
        #stores user's input into variables
        user_city = self.request.get('city_code')
        user_state = self.request.get('state_code')
        user_gender = self.request.get('gender')
        user_temp = self.request.get('average_feel')

        #stores user's input into a user object that is stored into a database
        user = User(user_city=user_city, user_state=user_state, user_gender=user_gender,
            user_temp=user_temp)
        key = user.put()

        #grabs weather information for user from API and stores into
        #variables referenced in output.html
        #used meme example to set up API
        #new API key = a7117aaeea209774c2669ef696152f31
        req = "http://api.wunderground.com/"
        city_words = user.user_city.split()
        # ["Chapel", "Hill"]
        city = "_".join(city_words)
        # "Chapel_Hill"
        path = "api/417c24aae230083b/forecast/q/" + user.user_state + "/" + city + ".json"
        req = req + path
        response = urllib2.urlopen(req)
        response_text = response.read()
        response_data = json.loads(response_text)
        day = response_data['forecast']['simpleforecast']['forecastday'][0]['period']
        outside_condition = response_data['forecast']['simpleforecast']['forecastday'][0]['conditions']
        outside_humidity = response_data['forecast']['simpleforecast']['forecastday'][0]['avehumidity']
        outside_min_temp = response_data['forecast']['simpleforecast']['forecastday'][0]['low']['fahrenheit']
        outside_max_temp = response_data['forecast']['simpleforecast']['forecastday'][0]['high']['fahrenheit']
        wind_speed = response_data['forecast']['simpleforecast']['forecastday'][0]['avewind']['mph']


        #tells jinja2 to get output.html from the "templates"
        #directory and render it with the given variables
        template = jinja_environment.get_template('output.html')
        html = template.render({'outside_max_temp':outside_max_temp,
            'outside_min_temp':outside_min_temp,
            'outside_condition':outside_condition,
            'outside_humidity':outside_humidity, 'wind_speed':wind_speed})
        self.response.write(html)

class AboutHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('about.html')
        self.response.write(template.render())

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/info', InputHandler),
    ('/outfit', OutputHandler),
    ('/about', AboutHandler),
    ('/admin', outfits.AdminHandler)

], debug=True)
