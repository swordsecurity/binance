import pymongo
import binance
import time
from random import randint

MONGODB_PORT = 27017
MONGODB_HOST = "localhost"
client = pymongo.MongoClient(MONGODB_HOST, MONGODB_PORT)
db = client.crypto

while True:
    prices =binance.prices()
    print prices
    sleeptime = randint(10,100)
    print "saving prices..."
    db.prices.insert_one(prices)
    print "prices saved"
    print "sleeping for %s" % sleeptime
    time.sleep(sleeptime)
    
