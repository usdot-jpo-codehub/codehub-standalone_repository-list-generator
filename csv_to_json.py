import pandas as pd
import json
import re
csv_file_path = "input_repository_list.csv"
out_file_path = "output_repository_list_codehub.json"

df = pd.read_csv(csv_file_path)
grouped = df.groupby("category")
category_dict_array = []

for group_name, group_df in grouped:
    repos_in_category = group_df.to_dict(orient='records')
    sorted_recs = sorted(repos_in_category, key=lambda x: x["name"].lower())
    alpha_recs = [i for i in sorted_recs if not re.match(r'^\d{1}', i["name"])]
    num_recs = [i for i in sorted_recs if re.match(r'^\d{1}', i["name"])]
    category_dict = {"category": group_name, "repos": alpha_recs+num_recs}
    if group_name == "Other":
        other_dict = category_dict
    else:
        category_dict_array.append(category_dict)
category_dict_array.append(other_dict)

with open(out_file_path, 'w') as outfile:
    outfile.write(json.dumps(category_dict_array))
