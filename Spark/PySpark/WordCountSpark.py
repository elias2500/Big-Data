from pyspark import SparkContext, SparkConf

#Startin spark conf with some configuration
conf = SparkConf().setAppName('test')\
    .setMaster('spark://ilias-A320M-S2H:7077')

#Creating spark context
sc = SparkContext(conf=conf)
sc

#Opening the file
file = sc.textFile("/home/ilias/Downloads/sample-2mb-text-file.txt")
#Running it through different edits
result = file.flatMap(lambda x: x.split(" "))\
    .map(lambda x: (x,1))\
        .reduceByKey(lambda x, y: x+y)

#Saving the result in a directory 
result.sortBy(lambda x: x[1], ascending=False).saveAsTextFile('/home/ilias/Desktop/result')
