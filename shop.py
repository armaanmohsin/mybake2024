import pandas as pd
import json

# Load the JSON data from the file
with open("shop.json", "r") as file:
    data = json.load(file)

# Prepare a list to hold the data rows
rows = []

# Iterate through each shop in the JSON data
for shop_id, details in data.items():
    row = details  # Each detail dict represents a row
    row["ShopID"] = shop_id  # Add the ShopID to the row
    rows.append(row)

# Convert the list of dictionaries to a pandas DataFrame
df = pd.DataFrame(rows)

# Specify the order of columns if necessary, or remove this line to keep pandas default ordering
column_order = ["ShopID", "ShopName", "ShopCode", "OwnerName", "ContactPerson", "Phone1", "Phone2", "Address", "City", "State", "GPSLatitude", "GPSLongitude", "ShopDiscount", "Trn"]
df = df[column_order]

# Save the DataFrame to a CSV file
df.to_csv("shop.csv", index=False)

print("The JSON data has been successfully converted to 'shop.csv'.")
