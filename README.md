# GroceryChatBot
UTK COSC 401 Project

## chat-box
Contains files for the default dark-mode [Flutter Chat UI](https://pub.dev/packages/flutter_chat_ui) chat box web app.   
View it displayed on [volweb](https://volweb.utk.edu/~swalla16/)  



## dataset
Contains files for the store inventory data set:
* **costco-data-full.csv:**
  * full dataset of costco inventory from kaggle.
* **small-subset-raw.csv:**
  * Small subset of items.
  * 9 categories with about 5 items each
  * Mix of made up items and items pulled from the coscto set
  * Added columns "Tags" (relevant keywords for the item) and "Brand" (the item's brand name)
* **dataset-gen.py:**
  * python script that processes the subset of inventory
  * Adds columns for SKU, Quantity, Aisle, and Bay numbers
  * Outputs to small-subset-processed.csv
* **small-subset-processed.csv:**
  * complete data set with the added columns
