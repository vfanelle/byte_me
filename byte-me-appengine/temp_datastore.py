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

        outfits.Clothing(article="shirt", name="Long-sleeve Sweater", temp=40,
        gender="male", url="http://static.hellyhansen.com/img/hh/catalog/large/51719_949_main_large.png"),
        outfits.Clothing(article="shirt", name="Long Sleeve T-shirt", temp=50,
        gender="male", url="https://image.spreadshirtmedia.com/image-server/v1/productTypes/23/views/1/appearances/4,width=378,height=378/Men-s-Long-Sleeve-T-Shirt.png"),
        outfits.Clothing(article="shirt", name="Button down", temp=60,
        gender="male", url="https://www.riversendtrading.com/prod/WAMHigh/1514235_1.png"),
        outfits.Clothing(article="shirt", name="Button down", temp=70,
        gender="male", url="http://sierrasummitgear.com/product_images/q/127/S12-Peakline-Shirt-SS-Riptide__58630.png"),
        outfits.Clothing(article="shirt", name="T-Shirt", temp=80,
        gender="male", url="https://image.spreadshirtmedia.net/image-server/v1/productTypes/6/views/1/appearances/4,width=378,height=378/Men-s-T-Shirt.png"),
        outfits.Clothing(article="shirt", name="T-Shirt", temp=90,
        gender="male", url="https://image.spreadshirtmedia.net/image-server/v1/productTypes/6/views/1/appearances/4,width=378,height=378/Men-s-T-Shirt.png"),
        outfits.Clothing(article="shirt", name="T-Shirt", temp=100,
        gender="male", url="https://image.spreadshirtmedia.net/image-server/v1/productTypes/6/views/1/appearances/4,width=378,height=378/Men-s-T-Shirt.png"),
        outfits.Clothing(article="shirt", name="T-Shirt", temp=110,
        gender="male", url="https://image.spreadshirtmedia.net/image-server/v1/productTypes/6/views/1/appearances/4,width=378,height=378/Men-s-T-Shirt.png"),

        outfits.Clothing(article="bottom", name="Jeans", temp=40,
        gender="male", url="http://cdn.shopify.com/s/files/1/0284/2118/products/20031_F.png?v=1389386884"),
        outfits.Clothing(article="bottom", name="Jeans", temp=50,
        gender="male", url="http://pngimg.com/upload/jeans_PNG5778.png"),
        outfits.Clothing(article="bottom", name="Jeans", temp=60,
        gender="male", url="http://pngimg.com/upload/jeans_PNG5745.png"),
        outfits.Clothing(article="bottom", name="Shorts", temp=70,
        gender="male", url="http://www.jjsoftwear.com/wp-content/uploads/2011/10/2.png"),
        outfits.Clothing(article="bottom", name="Shorts", temp=80,
        gender="male", url="http://www.jjsoftwear.com/wp-content/uploads/2011/10/2.png"),
        outfits.Clothing(article="bottom", name="Shorts", temp=90,
        gender="male", url="http://www.jjsoftwear.com/wp-content/uploads/2011/10/2.png"),
        outfits.Clothing(article="bottom", name="Shorts", temp=100,
        gender="male", url="http://www.jjsoftwear.com/wp-content/uploads/2011/10/2.png"),
        outfits.Clothing(article="bottom", name="Shorts", temp=110,
        gender="male", url="http://www.jjsoftwear.com/wp-content/uploads/2011/10/2.png"),


        outfits.Clothing(article="shoes", name="Vans", temp=40,
        gender="male", url="http://images.footlocker.com/pi/34274001/zoom/jordan-retro-2-mens"),
        outfits.Clothing(article="shoes", name="Vans", temp=50,
        gender="male", url="http://www.merkatoexpress.com/media/wysiwyg/superstore/product-1.png"),
        outfits.Clothing(article="shoes", name="Vans", temp=60,
        gender="male", url="https://cdn1.thehunt.com/app/public/system/note_images/1255271/original/83af6749c33b4eaddbb0e996db9c9503.png"),
        outfits.Clothing(article="shoes", name="Vans", temp=70,
        gender="male", url="http://images.nike.com/is/image/DotCom/144587C_001_A?$AFI$"),
        outfits.Clothing(article="shoes", name="Sandals", temp=80,
        gender="male", url="http://images.lacrosseunlimited.com/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/R/a/Rainbow_Sandals_Premier_Leathers_dark_brown_mocha_301ALTS0_dkbr_42.png"),
        outfits.Clothing(article="shoes", name="Vans", temp=90,
        gender="male", url="http://idboardshop.com/media/catalog/product/cache/1/image/510x/602f0fa2c1f0d1ba5e241f914e856ff9/0/7/077916.png"),
        outfits.Clothing(article="shoes", name="Sandals", temp=100,
        gender="male", url="http://images.lacrosseunlimited.com/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/R/a/Rainbow_Sandals_Premier_Leathers_dark_brown_mocha_301ALTS0_dkbr_42.png"),
        outfits.Clothing(article="shoes", name="Sandals", temp=110,
        gender="male", url="http://images.lacrosseunlimited.com/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/R/a/Rainbow_Sandals_Premier_Leathers_dark_brown_mocha_301ALTS0_dkbr_42.png"),


        outfits.Clothing(article="shirt", name="V-neck T-shirt", temp=75,
        gender="female", url="http://images.footlocker.com/pi/84683100/large/nike-shortsleeve-legend-v-neck-t-shirt-2.0-womens"),
        outfits.Clothing(article="shirt", name="Tank-top", temp=95,
        gender="female", url="http://www.nakfashionbd.com/img_upload/product_2015_06_27_01_45_33_Nak_Ladies_17.png"),
        outfits.Clothing(article="shirt", name="half-long sleeve", temp=65,
        gender="female", url="http://cdn.shopify.com/s/files/1/0097/5692/products/American_Apparel_AA_BB453_Baseball_Raglan_Truffle_large.png?v=1407187216"),
        outfits.Clothing(article="shirt", name="cami", temp=105,
        gender="female", url="http://dbdapps.co.uk/packinglists/sites/default/files/cami-top.png"),
        outfits.Clothing(article="shirt", name="light sweater", temp=55,
        gender="female", url="http://g.nordstromimage.com/ImageGallery/store/product/Zoom/18/_11600118.jpg"),
        outfits.Clothing(article="shirt", name="jacket", temp=45,
        gender="female", url="http://3.bp.blogspot.com/-gDdoKSV3FGs/UFYhLydU2OI/AAAAAAAABhs/PjFI-oAUO08/s1600/7122147_Sandy_coat_plum_jacket_A.png.png"),
        outfits.Clothing(article="shirt", name="V-neck T-shirt", temp=85,
        gender="female", url="http://images.footlocker.com/pi/84683100/large/nike-shortsleeve-legend-v-neck-t-shirt-2.0-womens"),

        outfits.Clothing(article="bottom", name="Skinny Jeans", temp=40,
        gender="female", url="http://www.jeans.ch/out/pictures/master/product/1/sol_nudie-jeans-skinny-lin-jeans-women-light-blue-skinny-lin-111818_f_1.png"),
        outfits.Clothing(article="bottom", name="Skinny Jeans", temp=50,
        gender="female", url="http://www.jeans.ch/out/pictures/master/product/1/sol_nudie-jeans-skinny-lin-jeans-women-light-blue-skinny-lin-111818_f_1.png"),
        outfits.Clothing(article="bottom", name="Skinny Jeans", temp=60,
        gender="female", url="http://www.jeans.ch/out/pictures/master/product/1/sol_nudie-jeans-skinny-lin-jeans-women-light-blue-skinny-lin-111818_f_1.png"),
        outfits.Clothing(article="bottom", name="Skinny Jeans", temp=70,
        gender="female", url="http://www.jeans.ch/out/pictures/master/product/1/sol_nudie-jeans-skinny-lin-jeans-women-light-blue-skinny-lin-111818_f_1.png"),
        outfits.Clothing(article="bottom", name="Shorts", temp=80,
        gender="female", url="https://wakeeffects.com/wp-content/uploads/2015/06/pool-375x374.png"),
        outfits.Clothing(article="bottom", name="Shorts", temp=90,
        gender="female", url="https://wakeeffects.com/wp-content/uploads/2015/06/pool-375x374.png"),
        outfits.Clothing(article="bottom", name="Shorts", temp=100,
        gender="female", url="https://wakeeffects.com/wp-content/uploads/2015/06/pool-375x374.png"),
        outfits.Clothing(article="bottom", name="Shorts", temp=110,
        gender="female", url="https://wakeeffects.com/wp-content/uploads/2015/06/pool-375x374.png"),


        outfits.Clothing(article="shoes", name="Uggs", temp=40,
        gender="female", url="http://31.sqrbear.com/wp-content/uploads/2014/05/UGG-Bailey-Button-Triplet-chestnut-Womens.png"),
        outfits.Clothing(article="shoes", name="Uggs", temp=50,
        gender="female", url="http://31.sqrbear.com/wp-content/uploads/2014/05/UGG-Bailey-Button-Triplet-chestnut-Womens.png"),
        outfits.Clothing(article="shoes", name="Vans", temp=60,
        gender="female", url="http://essentiallymom.com/wp-content/uploads/2014/02/Womens-Flat-Rain-Boots.png"),
        outfits.Clothing(article="shoes", name="Vans", temp=70,
        gender="female", url="http://www.gliks.com/Assets/ProductImages/M9166_shot1.png"),
        outfits.Clothing(article="shoes", name="Flats", temp=80,
        gender="female", url="https://i6.govx.io/images/136895_olukai_womens_pueo_womens_pueo_bronzekona_coffee_5_t300.png?v=GiE4OnoXIVuE8cfm5KlU2w=="),
        outfits.Clothing(article="shoes", name="Sandals", temp=90,
        gender="female", url="http://cdn.shopify.com/s/files/1/0219/5414/products/SIDE_BAXLEY2_PLATINUM_GOLD_METALLIC_NAPPA_large.png?v=1451439229"),
        outfits.Clothing(article="shoes", name="Sandals", temp=100,
        gender="female", url="http://cdn.shopify.com/s/files/1/0219/5414/products/SIDE_BAXLEY2_PLATINUM_GOLD_METALLIC_NAPPA_large.png?v=1451439229"),
        outfits.Clothing(article="shoes", name="Sandals", temp=110,
        gender="female", url="http://cdn.shopify.com/s/files/1/0219/5414/products/SIDE_BAXLEY2_PLATINUM_GOLD_METALLIC_NAPPA_large.png?v=1451439229")

        ]
        for clothing in clothing_list:
          num_matching = outfits.Clothing.query().filter(outfits.Clothing.url == clothing.url).count()
          if not num_matching:
              clothing.put()
        self.response.write("Done")
