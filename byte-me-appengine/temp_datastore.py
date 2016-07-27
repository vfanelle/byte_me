from google.appengine.ext import ndb
import jinja2
import json
import logging
import os
import urllib
import urllib2
import webapp2
import outfits

#tells jinja2 where to look for future files
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(template_dir))

class TempDatastoreHandler(webapp2.RequestHandler):
    def get(self):
        clothing_list= [
        outfits.Clothing(article="shirt", name="T-Shirt", temp=75,
        gender="male", url="http://esq.h-cdn.co/assets/cm/15/05/54cc9f1233f4b_-_esq-blue-crew-margiela-041812-mdn-79225964.jpg"),
        outfits.Clothing(article="bottom", name="Jeans", temp=75,
        gender="male", url="http://images.sportsdirect.com/images/imgzoom/64/64404990_xxl.jpg"),
        outfits.Clothing(article="shoes", name="Vans", temp=75,
        gender="male", url="http://images.vans.com/is/image/Vans/EE3BLK-HERO?$356x356$"),
        outfits.Clothing(article="shirt", name="V-neck T-shirt", temp=75,
        gender="female", url="http://www.polyvore.com/cgi/img-thing?.out=jpg&size=l&tid=135155157"),
        outfits.Clothing(article="bottom", name="Skinny Jeans", temp=75,
        gender="female", url="http://cdn.shopclues.net/images/detailed/14022/jeans_1426934506.jpg"),
        outfits.Clothing(article="shoes", name="Vans", temp=75,
        gender="female", url="https://asset1.surfcdn.com/vans-shoes-vans-authentic-lo-pro-womens-shoes-navy-true-white.jpg?w=1200&h=1200&r=4&q=80&o=cit4@K7Ju6AzmQMUdeZMd$26Tq4j&V=CVZ0"),
        ]
        for clothing in clothing_list:
          num_matching = outfits.Clothing.query().filter(outfits.Clothing.url == clothing.url).count()
          if not num_matching:
              clothing.put()
        self.response.write("Done")
