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

from pyspark.sql.functions import col, cast, round, trim
from pyspark.sql.utils import AnalysisException
df = spark.sql("SELECT * FROM treasury_lakehouse.bronze.treasure_data")
df_casted = df.select(
            round(col("avg_interest_rate_amt").cast('float'), 2).alias("avg_interest_rate_amt"),
            col("record_calendar_day").cast('int').alias("record_calendar_day"),
            col("record_calendar_month").cast('int').alias("record_calendar_month"),
            col("record_calendar_quarter").cast('int').alias("record_calendar_quarter"),
            col("record_calendar_year").cast('int').alias("record_calendar_year"),
            col("record_fiscal_quarter").cast('int').alias("record_fiscal_quarter"),
            col("record_fiscal_year").cast('int').alias("record_fiscal_year"),
            col("src_line_nbr").cast('int').alias("src_line_nbr"),
            trim(col("security_desc")).alias("security_desc"),
            trim(col("security_type_desc")).alias("security_type_desc"),
            trim(col("key")).alias("key")
)
try:
    df_casted\
            .write\
            .format('delta')\
            .option('mergeSchema', 'true')\
            .saveAsTable('silver.treasure_data')
except AnalysisException:
    df_casted.createOrReplaceTempView("vw_casted_data")
    spark.sql("""
            MERGE INTO silver.treasure_data target_data
            USING vw_casted_data source_data
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
