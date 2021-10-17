from enum import unique
from google.cloud.bigquery import dataset, query
import pandas as pd
from google.cloud import bigquery


gcp_project = 'playground-325606'
bq_dataset = 'testingBigQuery'


client = bigquery.Client(project=gcp_project)
dataset_ref = client.dataset(bq_dataset)


def gcp2df(sql):
    query = client.query(sql)
    results = query.result()
    return results.to_dataframe()

query = """
SELECT * FROM `playground-325606.testingBigQuery.DQ_UNIQUENESS_FINAL` LIMIT 100
"""
df = gcp2df(query)

print(df.head())


