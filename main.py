import extract_data
import transform_data
import load_data
import pandas as pd

print("extracting raw data...")
raw_data = extract_data()
print("data extracted.")

print("converting to structured data with fact table...")
data = transform_data.to_data_frame(raw_data)
project_details = transform_data.get_project_details(data)
client = transform_data.get_client(data)
milestones = transform_data.get_milestones(data)
teams = transform_data.get_teams(data)
fact = transform_data.get_fact_table(project=project_details, client=client, teams=teams, milestones=milestones)
print("conversion completed.")

print("loading all the tables to database in ssms...")
load_data.connect(project_details, 'project_details')
load_data.connect(client, 'client')
load_data.connect(milestones,'milestones')
load_data.connect(teams,'teams')
load_data.connect(fact,'fact')
print("loaded to database.")
