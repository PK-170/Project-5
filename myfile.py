#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 16:40:08 2024

@author: mount
"""

#Importing the packages
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType
import pyspark.sql.functions as func


def add(a, b):
    c = a * b
    print(c)

add(500, 77777)    

i = 0
while(i < 10):
    print("This is while loop")
    i = i+1