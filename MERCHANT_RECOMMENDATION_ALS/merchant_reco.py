import sys
from pyspark import SparkConf, SparkContext
from pyspark.mllib.recommendation import ALS, Rating
import csv
csv.register_dialect('myDialect',delimiter = ',',quoting = csv.QUOTE_ALL,skipinitialspace = True)
def loadMerchantNames():
 with open("merchant_id.csv",encoding='ascii', errors="ignore") as f:
    reader = csv.reader(f,dialect ='myDialect')
    merchantNames = {}
    for fields in reader:
        if fields:
        	merchantNames[int(fields[1])] = fields[0]
    return merchantNames
conf = SparkConf().setMaster("local[*]").setAppName("MovieRecommendationsALS")
sc = SparkContext(conf = conf)
sc.setCheckpointDir('checkpoint')

print("\nLoading merchant names...")
nameDict = loadMerchantNames()



data = sc.textFile("item_ID2.csv")
print("#############",data.take(5))

ratings = data.map(lambda l: l.split(",")).map(lambda l: Rating(int(l[0]), int(l[1]), float(l[2]))).cache()
print("----------",ratings.take(5))
rank = 10
# Lowered numIterations to ensure it works on lower-end systems
numIterations = 10
model = ALS.train(ratings, rank, numIterations)


userID = int(sys.argv[1])
#userID = 101

print("\n------------------------------Ratings for user ID " + str(userID) + ":")
userRatings = ratings.filter(lambda l: l[0] == userID)
for rating in userRatings.collect():
    print (nameDict[int(rating[1])] + ": " + str(rating[2]))

print("\nTop 10 recommendations:")
recommendations = model.recommendProducts(userID, 10)
for recommendation in recommendations:
    print (nameDict[int(recommendation[1])] + \
        " score " + str(recommendation[2]))


