# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "2ad1b9fb-d253-443e-8632-d62f175e396b",
# META       "default_lakehouse_name": "treasury_lakehouse",
# META       "default_lakehouse_workspace_id": "7562a65e-687d-4691-bd5c-32c6273aeeb6",
# META       "known_lakehouses": [
# META         {
# META           "id": "2ad1b9fb-d253-443e-8632-d62f175e396b"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

#Read data from json file
df = spark.read.option("multiline", "true").json("Files/treasure_api_data.json").select("data")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from pyspark.sql.functions import explode, col, concat, lit
from pyspark.sql.types import StructField, StructType, StringType
# split data into rows
df_exploded = df\
                .select(
                        explode(df["data"]).alias("json_object")
                    )

# define schema
schema = StructType() \
    .add("security_desc", StringType()) \
    .add("record_fiscal_year", StringType()) \
    .add("src_line_nbr", StringType()) \
    .add("record_calendar_quarter", StringType()) \
    .add("security_type_desc", StringType()) \
    .add("record_calendar_month", StringType()) \
    .add("avg_interest_rate_amt", StringType()) \
    .add("record_calendar_day", StringType()) \
    .add("record_calendar_year", StringType()) \
    .add("record_fiscal_quarter", StringType()) \
    .add("record_date", StringType())

# parse data from json to table
df_parsed = df_exploded.select("json_object.*")
df_parsed = df_parsed.withColumn('key', concat(col("security_desc"), lit(" "),col("src_line_nbr"), lit(" "), col("record_date")))

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# write data back to lakehouse (with increamental load)
from pyspark.sql.utils import AnalysisException                         
try:
    df_parsed\
        .write\
        .format('delta')\
        .saveAsTable('bronze.treasure_data')
except AnalysisException:
    df_parsed.createOrReplaceTempView('vw_treasure_data')
    spark.sql("""
            MERGE INTO bronze.treasure_data target_data
            USING vw_treasure_data source_data
            ON source_data.key = target_data.key
            WHEN MATCHED THEN 
                UPDATE SET *
            WHEN NOT MATCHED THEN 
                INSERT *
    """)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
