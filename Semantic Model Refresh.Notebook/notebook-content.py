# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   }
# META }

# MARKDOWN ********************

# ### Install the latest .whl package
# 
# Check [here](https://pypi.org/project/semantic-link-labs/) to see the latest version.

# CELL ********************

%pip install semantic-link-labs

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ### Import the library and set the initial parameters

# CELL ********************

import sempy.fabric as fabric
import sempy_labs as labs
dataset = '' # Enter your dataset name
workspace = None # Enter your workspace name (if set to None it will use the workspace in which the notebook is running)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ### Refresh a semantic model

# CELL ********************

labs.refresh_semantic_model(dataset=dataset, workspace=workspace)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# #### Visualize the refresh of a semantic model
# The resulting dataframe returns the trace logs capturing the details of the refresh operation

# CELL ********************

df = labs.refresh_semantic_model(dataset=dataset, workspace=workspace, visualize=True)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# #### Refresh specific tables

# CELL ********************

labs.refresh_semantic_model(dataset=dataset, workspace=workspace, tables=['Sales', 'Geography'])

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# #### Refresh specific partitions

# CELL ********************

labs.refresh_semantic_model(dataset=dataset, workspace=workspace, partitions=["'Sales'[Sales FY20]", "'Sales'[Sales FY21]"])

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# #### Refresh a combination of tables and partitions

# CELL ********************

labs.refresh_semantic_model(dataset=dataset, workspace=workspace, tables=['Geography', 'Calendar'], partitions=["'Sales'[Sales FY20]", "'Sales'[Sales FY21]"])

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# #### Clear the values of a table

# CELL ********************

labs.refresh_semantic_model(dataset=dataset, workspace=workspace, refresh_type='clearValues')

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ### View semantic model refreshes

# CELL ********************

fabric.list_refresh_requests(dataset=dataset, workspace=workspace)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ### Cancel a semantic model refresh

# CELL ********************

labs.cancel_dataset_refresh(dataset=dataset, workspace=workspace)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Specify the request_id based on a value from list_refresh_requests
labs.cancel_dataset_refresh(dataset=dataset, workspace=workspace, request_id='')

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ### View a semantic model's refresh history

# CELL ********************

labs.get_semantic_model_refresh_history(dataset=dataset, workspace=workspace)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ### View details of a specific semantic model refresh

# CELL ********************

labs.get_semantic_model_refresh_history(dataset=dataset, workspace=workspace, request_id='')

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
