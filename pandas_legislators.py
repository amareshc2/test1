
from io import StringIO
import pandas as pd
import boto3

bucket = "fundamentalsbucket"
file_name = "fundamentals_dataset.csv"

s3 = boto3.client('s3') 


obj = s3.get_object(Bucket= bucket, Key= file_name) 
# get object and file (key) from bucket

df = pd.read_csv(obj['Body']) 
#dtypes = {
    #"period": "category",
   # "company": "category",
   # "tickers": "category",
   # "indicator": "category",
   ## "unit": "category",
#}
#df = pd.read_csv(
   # "#fundamentals_dataset.csv",
   # dtype=dtypes,
  #
#)

from pandas_legislators import df  #make data adjustments
df.groupby(["period","company"])


df = df[df.indicator == "Final Revenue"]
#####
csv_buffer = StringIO()    #send back to s3
df.to_csv(csv_buffer)
s3_resource = boto3.resource('s3')
s3_resource.Object(bucket, 'df.csv').put(Body=csv_buffer.getvalue())
