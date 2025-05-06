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

from mlflow import MlflowClient
client = MlflowClient()
client.create_model_version(
        name="predict_model",
        source=<"your-model-source-path">,
        run_id=<"your-run-id">
    )

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
