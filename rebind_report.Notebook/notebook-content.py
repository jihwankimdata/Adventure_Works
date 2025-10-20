# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import sempy_labs as labs
import requests

workspace_name = None # Update this to the workspace in which you want to save the notebooks
api_url = "https://api.github.com/repos/microsoft/semantic-link-labs/contents/notebooks"
response = requests.get(api_url)
files = response.json()
notebook_files = {file['name'][:-6]: file['html_url'] for file in files if file['name'].endswith('.ipynb')}

for file_name, file_url in notebook_files.items():
    labs.import_notebook_from_web(notebook_name=file_name, url=file_url, workspace=workspace_name)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

%pip install semantic-link-labs

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import sempy_labs as labs
import sempy_labs.lakehouse as lake
import sempy_labs.report as rep
from sempy_labs import migration, directlake, admin, graph, theme, mirrored_azure_databricks_catalog, ml_model, variable_library
from sempy_labs.tom import connect_semantic_model
from sempy_labs.report import connect_report

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Rebind report to the Direct Lake semantic model

import sempy_labs.report as rep

report = 'import_adventure_works' # Name or ID of the report
dataset = 'direct_lake_factinternetsales' # Name or ID of the semantic model to bind to the report
report_workspace = None # Name or ID of the workspace in which the report resides
dataset_workspace = None # Name or ID of the workspace in which the semantic model resides

rep.report_rebind(report=report, dataset=dataset, report_workspace=report_workspace, dataset_workspace=dataset_workspace)



# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
