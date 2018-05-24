import sys , operator
import csv
import string
import nltk

from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.feature import IndexToString, StringIndexer, VectorIndexer
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

nltk.download('stopwords')
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from pyspark.sql import SparkSession
from nltk.corpus import stopwords

if __name__ == "__main__":

  # create Spark context with Spark configuration
  spark = SparkSession.builder.appName("SimpleApp").getOrCreate()
  sc = spark.sparkContext
  stop_words = set(stopwords.words('english'))
  # create a spark session , y le pido que me devuelva el context

  # read in text file and split each document into words
  # df = spark.read.format("csv").option("header", "true").load("Learning1.csv")

  # the empty arrays with the important information to train the model
  calification = []
  review = []

 # getting the important information for us that is the review and our calification
  with open('Learning1.csv', 'r') as f:
    f.readline()  # ignoring the first row that have the csv information
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        review.append(row[8])
        calification.append(row[9])

  calification = list(map(int, calification))

  # cleaning the data
  review = list(map(lambda x: x.lower(), review))  # coverting all the text to lower
  review = [''.join(c for c in s if c not in string.punctuation) for s in review] # removing all the punctuation
  review = list(map(lambda x: x.translate(str.maketrans('','', string.digits)), review)) # removing  Deleting Numbers

  print(review)

  #filtered_sentence = [w for w in review if not w in stop_words]
  filtered_sentence = []
  final = ""
  for sentence in review:
    word_tokens = word_tokenize(sentence)
    for w in word_tokens:
      if w not in stop_words:
        final = final + " " + w
    filtered_sentence.append(final)
    final = ""
 
  print("\n \n -----------------------------------------------------------------------------------------------------: \n " +  str(filtered_sentence))
  
  
  # review = list(map(lambda x: x.strip(), review) #
  # review = list (lambda x: x.translate(None, string.digits))
  #print(review)  # just to test what does the array have


 # spark-submit --master yarn --deploy-mode cluster *.py
 # si tengo alguna depencia, y cuando ejecute spark , pyenv,
 # spark uno le puede mandar un zip , con lo que nececitemos
 # ejecutar en un cluster. subirlo hdfs , se pone la ruta dfs, recibir lo que vamos a cargar y el archivo
 # de salida como argumentos

 # spark-submit --master local[1] proyecto.py # como correrlo localmente
