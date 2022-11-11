#!/usr/bin/env python
# coding: utf-8

# In[1]:


import boto3
import pandas as pd
import io


# In[2]:


REGION = 'us-west-2'
ACCESS_KEY_ID = 'AKIA47RGEI7IZZKD2PXX'
SECRET_ACCESS_KEY = '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'


# In[12]:


BUCKET_NAME = 'fundamentalsbucket'
KEY = 'fundamentals_dataset.csv' # file path in S3 


# In[13]:


s3c = boto3.client(
        's3', 
        region_name = REGION,
        aws_access_key_id = ACCESS_KEY_ID,
        aws_secret_access_key = SECRET_ACCESS_KEY
    )


# In[15]:


obj = s3c.get_object(Bucket= BUCKET_NAME , Key = KEY)


# In[16]:


df = pd.read_csv(io.BytesIO(obj['Body'].read()), encoding='utf8')
df


# In[ ]:




