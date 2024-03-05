import pandas as pd
import json

# Function to convert the nested JSON to a flat table
def json_to_csv(json_file, csv_file):
    # Load JSON data from a file
    with open(json_file, 'r') as file:
        data = json.load(file)
    
    rows = []  # A list to store rows
    
    # Iterate through each category and product
    for category_id, products in data.items():
        for product_id, product_details in products.items():
            row = {
                "Categoryid": category_id,
                "Productid": product_id,
                "Productname": product_details.get("name", ""),
                "Productprice": product_details.get("price", "")
            }
            rows.append(row)
    
    # Convert list of dicts to DataFrame
    df = pd.DataFrame(rows)
    
    # Save DataFrame to CSV
    df.to_csv(csv_file, index=False)

# Specify your JSON file path and the desired CSV output file path
json_file_path = 'product.json'  # Update this to your JSON file path
csv_file_path = 'product.csv'   # Update this to your desired CSV file path

# Call the function with your file paths
json_to_csv(json_file_path, csv_file_path)
