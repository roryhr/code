Title: Approach to Python
Date: 2019-08-15
Category: Python
Tags: python

Note:

I like to phrase things as punchy commands but it's all just my preference.
My personal style is constantly evolving.

My motto is a twist on the Zen of Python
```
If the implementation is hard to understand, it's bad.
If the implementation is easy to understand, it may be good.
```

# Style Guide

List comprehensions are your bread and butter. Structure them like a SQL query.
```python
cleaned_emails = [
    email.strip()
    for email
    in emails
    if '@test.com' not in email
]
```

Give the [The Numpy docstring style](https://numpydoc.readthedocs.io/en/latest/format.html) a try.

```python
def clean_emails(emails):
    """Clean up emails from source database

    Parameters
    ----------
    emails : list
        Raw email addresses

    Returns
    -------
    cleaned_emails : list
        Cleaned email addresses
    """
    cleaned_emails = [
        email.strip()
        for email
        in emails
        if '@test.com' not in email
    ]
    return cleaned_emails
```

Naming things is hard. Do it well! 
Conserve your colleagues' brainpower: if a function has a good name and docstring then they don't have to understand *how it works* to understand *what it does*. 


Use SQL where possible, it's more readable than the PySpark equivalent.
```python
user_df = spark.sql("""
SELECT id,
       created_at,
       dt AS partition
  FROM users
 WHERE updated_at IS NOT NULL
""")
```

Distinguish between Spark DataFrames and Pandas DataFrames when mixing the two. 
```python
user_pdf = user_df.toPandas()
```

Other Spark preferences:
Distinguish between Spark DataFrames and Pandas DataFrames when mixing the two.
```python
import pyspark
import pyspark.sql.types as T 
import pyspark.sql.functions as F
```

As the [documentation](http://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.SparkSession) says, the preferred entry point for Spark is through `spark`.
```python
# Yes
df = spark.read.parquet()
rdd = spark.sparkContext.sequenceFile()
df = spark.sql("""SELECT * FROM users""")
# No
df = sc.read.parquet()
sparkContext
df = sqlContext.sql("""SELECT * FROM users""")
df = hiveContext.sql("""SELECT * FROM users""")
```

# Writing Scripts

Start with functions.
If you find yourself passing several parameters between functions then make a class.


Let's say you have a PySpark script called `anonymize_emails.py` which needs a date and a database. 
```python
import sys
import pyspark

if __name__ == '__main__':
    _, database, date = sys.argv

    spark = pyspark.sql.SparkSession.builder\
        .appName('Anonymize Emails for {}'.format(date))\
        .getOrCreate()

    anonymize_emails(spark, database, date)
```

Explicitly ignore extra parameters if you want.
```
_, database, date, *_ = sys.argv

```

I'm not a huge fan of the trailing backslash for new lines but it's common in Spark and growing on me. 
For Pandas I still prefer to use parentheses. 
In any case put each operation on new line. 
```python
(df[['user_id', 'time_on_page']]
    .groupby('user_id')
    .mean()
    .to_csv('average_time_on_page.csv')
)
```

Jupyter Notebooks are your friend. 
Especially for data science you'll want to iterate: see what's in the data, check the processing did what you think it did, and see how long each chunk of code takes to run. 
Super helpful for development! 
What's a natural chunk of code?
A function, of course. 

Once everything is working clean up the notebook and add some nice comments and descriptive text.
Now you're ready to transfer this code to a proper script and deploy it.


