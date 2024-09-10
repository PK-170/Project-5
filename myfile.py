#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 16:40:08 2024

@author: mount
"""

#Importing the packages
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType
#import pyspark.sql.functions as func


#Creating the SparkSession
spark = SparkSession.builder.appName("FirstApp").getOrCreate()


#Defining schema for your DataFrame
myschema = StructType([\
                       StructField("userID", IntegerType(), True),
                       StructField("name", StringType(), True),
                       StructField("age",IntegerType(), True),
                       StructField("friends",IntegerType(), True),
                        ])

    
#Creating DataFrame on a CSV file
people = spark.read.format("csv")\
    .schema(myschema)\
    .option("path","/Users/mount/SparkProject/NameOfFriends.csv")\
    .load()
    
people.show(5)
   
print(people.count()) 




    
def add(a, b):
    c = a * b
    print(c)

add(500, 77777)    

i = 0
while(i < 5):
    print("This is while loop")
    i = i+1