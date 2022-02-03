# Databricks notebook source
dbutils.widgets.removeAll()
dbutils.widgets.text('dataset','')
dataset = dbutils.widgets.get('dataset')

# COMMAND ----------

print('Processing dataset {}'.format(dataset))

# COMMAND ----------

print("Processing completed")