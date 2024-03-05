import pandas as pd
import json

# Load the JSON data from the file
with open("category.json", "r") as file:
    data = json.load(file)

# Prepare a list to hold the data rows
rows = []

# Iterate through each category in the JSON data
for category_id, details in data.items():
    rows.append({
        "Categoryid": category_id,
        "CategoryName": details["categoryName"],
        "PostKey": details["postKey"]
    })

# Convert the list of dictionaries to a pandas DataFrame
df = pd.DataFrame(rows)

# Save the DataFrame to a CSV file
df.to_csv("category.csv", index=False)

print("The JSON data has been successfully converted to 'category.csv'.")
