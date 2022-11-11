import json
import pandas as pd
import numpy as np
import requests
import glob
import time
import os
from datetime import datetime
from csv import reader
import boto3
import io


s3_client = boto3.client('s3')

def lambda_handler(event, context):
    try:
            
        bucket = event["Records"][0]["s3"]["bucket"]["name"]
        key = event["Records"][0]["s3"]["object"]["key"]
        obj = s3_client.get_object(Bucket=bucket, Key= key)
        df = pd.read_csv(obj['Body']) # read csv into pd dataframe
        
        df.groupby(["period","company"])  #make data adjustments
        df = df[df.indicator == "Final Revenue"]
      

        
        print(df)

    except Exception as err:
        print(err)
        
   