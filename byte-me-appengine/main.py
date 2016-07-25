from google.appengine.ext import ndb
import jinja2
import json
import logging
import os
import urllib
import urllib2
import webapp2

#creates a user
class User(ndb.Model):
        zip_code = ndb.IntegerProperty(required=True)
        gender = ndb.StringProperty(required=True)
        body_temp = ndb.StringProperty(required=True)

#tells jinja2 where to look for future files
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(template_dir))

#handler for main page to display input.html
class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('input.html')
        self.response.write(template.render())

#handler to display output page and save user's input into a user object
class OutputHandler(webapp2.RequestHandler):

    def get(self):
        user_city = self.request.get('city_code')
        user_state = self.request.get('state_code')
        user_gender = self.request.get('gender')
        user_temp = self.request.get('average_feel')
        user = User(zip_code=int(user_zip), gender=user_gender,
            body_temp=user_temp)
        key = user.put()

        # template = jinja_environment.get_template('output.html')
        # self.response.write(template.render())

        #grabs weather information for user from API and stores into
        #variables referenced in output.html
        #setting up the weather api, used meme example
        #API key = d18790d3f622ff63af5b3fc8902387db
        #new API key = a7117aaeea209774c2669ef696152f31
        req = ("http://api.wunderground.com/api/417c24aae230083b/forecast/q/CA/San_Francisco.json
        response = urllib2.urlopen(req)
        response_text = response.read()
        response_data = json.loads(response_text)
        outside_avg_temp = response_data['main']['temp']
        outside_avg_temp = temperature(outside_avg_temp)
        outside_humidity = response_data['main']['humidity']
        outside_min_temp = response_data['main']['temp_min']
        outside_min_temp = temperature(outside_min_temp)
        outside_max_temp = response_data['main']['temp_max']
        outside_max_temp = temperature(outside_max_temp)
        wind_speed = response_data['wind']['speed']
        wind_speed = mph(wind_speed)

        #tells jinja2 to get output.html from the "templates"
        #directory and render it with the given variables
        template = jinja_environment.get_template('output.html')
        html = template.render({'outside_max_temp':outside_max_temp,
            'outside_min_temp':outside_min_temp,
            'outside_avg_temp':outside_avg_temp,
            'outside_humidity':outside_humidity, 'wind_speed':wind_speed})
        self.response.write(html)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/outfit', OutputHandler)
], debug=True)

def temperature(Kelvin):
     return Kelvin

def mph(meters_per_sec):
    mph = meters_per_sec*2.25
    return mph
