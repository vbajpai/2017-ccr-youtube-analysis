import pandas as pd

def group(df, column='endpoint'):
  """accepts a pandas DataFrame, sorts it by endpoints, groups the rows by 
     endpoint and returns the DataFrameGroupBy object"""

  # sort the DataFrame by endpoint
  df = df.sort_values(by=column)

  # group the rows by endpoint
  df = df.groupby(column)

  return df

def aggregate(dfgroupby, value, function):
  """accepts a DataFrameGroupBy object, aggregates the column (value)
     specified by the aggregation functions passed as list argument, returns 
     the DataFrame"""

  # aggregate the values
  df = dfgroupby[value].agg(function)

  return df

def merge(df1, df2, column='endpoint'):
  """accepts two DataFrame objects, merges them by endpoint,
     and returns the DataFrame"""

  # merge on endpoint
  df = pd.merge(df1, df2, left_on=column, right_index=True)

  return df

def reducedim(df, cols):
  """accepts a DataFrame object and list of columns, deletes the columns from
     the DataFrame and returns the reduced DataFrame"""

  # reduce dimensionality
  for col in cols: del df[col]

  return df

def uniq(df):
  """accepts a DataFrame object, remove duplicates and returns DataFrame"""

  # remove duplicates
  df = df.drop_duplicates()

  return df
