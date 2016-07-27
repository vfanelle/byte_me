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
        outfits.Clothing(article="shirt", name="T-Shirt", temp=80,
        gender="male", url="https://image.spreadshirtmedia.net/image-server/v1/productTypes/6/views/1/appearances/4,width=378,height=378/Men-s-T-Shirt.png"),
        outfits.Clothing(article="shirt", name="Button down", temp=75,
        gender="male", url="http://sierrasummitgear.com/product_images/q/127/S12-Peakline-Shirt-SS-Riptide__58630.png"),


        outfits.Clothing(article="bottom", name="Jeans", temp=60,
        gender="male", url="http://pngimg.com/upload/jeans_PNG5778.png"),
        outfits.Clothing(article="bottom", name="Jeans", temp=60,
        gender="male", url="http://pngimg.com/upload/jeans_PNG5745.png"),
        outfits.Clothing(article="bottom", name="Shorts", temp=82,
        gender="male", url="http://www.jjsoftwear.com/wp-content/uploads/2011/10/2.png"),


        outfits.Clothing(article="shoes", name="Vans", temp=60,
        gender="male", url="https://cdn1.thehunt.com/app/public/system/note_images/1255271/original/83af6749c33b4eaddbb0e996db9c9503.png"),
        outfits.Clothing(article="shoes", name="Vans", temp=40,
        gender="male", url="http://images.footlocker.com/pi/34274001/zoom/jordan-retro-2-mens"),
        outfits.Clothing(article="shoes", name="Vans", temp=92,
        gender="male", url="http://idboardshop.com/media/catalog/product/cache/1/image/510x/602f0fa2c1f0d1ba5e241f914e856ff9/0/7/077916.png"),
        outfits.Clothing(article="shoes", name="Sandals", temp=95,
        gender="male", url="http://images.lacrosseunlimited.com/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/R/a/Rainbow_Sandals_Premier_Leathers_dark_brown_mocha_301ALTS0_dkbr_42.png"),
        outfits.Clothing(article="shoes", name="Sandals", temp=82,
        gender="male", url="http://images.lacrosseunlimited.com/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/R/a/Rainbow_Sandals_Premier_Leathers_dark_brown_mocha_301ALTS0_dkbr_42.png"),


        outfits.Clothing(article="shirt", name="V-neck T-shirt", temp=75,
        gender="female", url="http://images.footlocker.com/pi/84683100/large/nike-shortsleeve-legend-v-neck-t-shirt-2.0-womens"),


        outfits.Clothing(article="bottom", name="Skinny Jeans", temp=75,
        gender="female", url="http://www.jeans.ch/out/pictures/master/product/1/sol_nudie-jeans-skinny-lin-jeans-women-light-blue-skinny-lin-111818_f_1.png"),


        outfits.Clothing(article="shoes", name="Vans", temp=75,
        gender="female", url="http://www.gliks.com/Assets/ProductImages/M9166_shot1.png"),
        ]
        for clothing in clothing_list:
          num_matching = outfits.Clothing.query().filter(outfits.Clothing.url == clothing.url).count()
          if not num_matching:
              clothing.put()
        self.response.write("Done")
