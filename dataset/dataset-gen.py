# Simple Dataset Generator for Shoppy Chat Bot
# COSC 401 Senior Design Project
#
# Input data:
# * small-subset-raw.csv
# * CSV file containing info for a small set of grocery items.  
# * Some items are made up, and others are real products sourced from a dataset of Costco inventory [on Kaggle](https://www.kaggle.com/datasets/bhavikjikadara/grocery-store-dataset).  
# * 9 categories with about 5 items per category
# * Columns:
#     * Sub Category
#     * Price
#     * Title
#     * Product Description
#     * Brand
#     * Tags
#
# Data Processing:
# * Rename columns
# * Give each item an SKU / Item number (index + 10,000) 
# * Give each item a random quantity between 0 and 25
# * Add Aisle and Bay numbers to designate the item's location in the store: 
#     * Aisle: Give each category its own aisle
#     * Bay: All aisles will have the same number of bays for now (NUM_BAYS). Assign each item a bay number between 1 and NUM_BAYS
# * Re-order columns and write the processed output to CSV file small-subset-processed.csv

import numpy as np
import pandas as pd

# Number of bays per aisle. 
NUM_BAYS = 3

# Read in the data csv
grocery_data = pd.read_csv("small-subset-raw.csv")

# Rename columns
grocery_data = grocery_data.rename(columns={"Product Description": "Description", "Title": "Product Name", "Sub Category": "Category"})

# Assign a random item quantity between 0 and 25
grocery_data["Quantity"] = np.random.randint(low = 0,high=25,size=grocery_data.shape[0])

# Give it an SKU / Item Number - just index + 10,000 for now
grocery_data["SKU"] = grocery_data.index+10000

# For now just assign each category its own aisle
# Make a list of the categories then assign the index that corresponds
# to that category to the item's Aisle column (+1 so starts at Aisle 1) 
categories = grocery_data["Category"].unique().tolist()
grocery_data["Aisle"] = grocery_data["Category"].apply(lambda x: categories.index(x) + 1)

# Give it a Bay number between 1 and num_bays
grocery_data["Bay"] = (grocery_data["SKU"] % NUM_BAYS) + 1

# Reorder the columns and output to new csv
inventory = grocery_data[["SKU", "Brand", "Product Name", "Price", "Quantity", "Category", "Description", "Tags", "Aisle", "Bay"]]
print(inventory)

inventory.to_csv('small-subset-processed.csv', index=False) 