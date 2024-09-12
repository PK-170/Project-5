#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 20:50:02 2024

@author: mount
"""
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.\
builder.\
appName("sparksql").\
getOrCreate()

print(spark.version)


data = spark.read.format('csv').\
option('inferSchema','true').\
option('header', 'false').\
option('path','/Users/mount/SparkProject/NameOfFriends.csv').\
load()

data.show(5)

data.printSchema()