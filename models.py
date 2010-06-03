from google.appengine.ext import db

class pdxhash_polygon(db.Model):
    # pdxhash_x fields are actual pdxhash strings
    pdxhash_4 = db.StringProperty()
    pdxhash_5 = db.StringProperty()
    pdxhash_6 = db.StringProperty()
    pdxhash_7 = db.StringProperty()
    
    # pdxhash polyons
    pdxhash_4_poly = db.StringProperty()
    pdxhash_5_poly = db.StringProperty()
    pdxhash_6_poly = db.StringProperty()
    pdxhash_7_poly = db.StringProperty()

    # pdxhash polygon centroids
    pdxhash_4_centroid = db.GeoPtProperty()
    pdxhash_5_centroid = db.GeoPtProperty()
    pdxhash_6_centroid = db.GeoPtProperty()
    pdxhash_7_centroid = db.GeoPtProperty()
