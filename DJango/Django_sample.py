import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("pandas to spark").getOrCreate()

df = sns.load_dataset("iris")
#print("Hello World!")
print(df)
print(df.shape)
print(df.columns)
print(df.info())
#for x in ['sepal_length', 'sepal_width', 'petal_length', 'petal_width','species']:
#    sns.histplot(df[x])
#    plt.show()

df_spark = spark.createDataFrame(df,schema=df.columns.tolist())
print(df_spark.show())

