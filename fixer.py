# import pandas as pd

# # Load CSV and convert to JSON
# df = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vTViltvCJg8TywJBukt7W3dYZG0G2HBdylAA7VuG1bJOAxuM23gJxIRt8RiZif5-IAK7YoecFvFYjOR/pub?output=csv")  # Replace with your CSV file
# df.to_json("Oceania.json", orient="records")

# print("CSV converted to JSON!") 

# import pandas as pd
# from pymongo import MongoClient

# # Connect to MongoDB Atlas
# client = MongoClient("mongodb+srv://anandmadarapu05:fsvwhpgir1OEYiq7@plants.hqrr8.mongodb.net/?retryWrites=true&w=majority&tls=true")

# db = client["FloraTheExplorer"]
# collection = db["plants"]

# # Load and insert CSV data
# df = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vTViltvCJg8TywJBukt7W3dYZG0G2HBdylAA7VuG1bJOAxuM23gJxIRt8RiZif5-IAK7YoecFvFYjOR/pub?output=csv")  # Change to your CSV file
# data = df.to_dict(orient="records")  # Convert to JSON format
# collection.insert_many(data)

# print("Data inserted successfully!")

import pandas as pd

# Load CSV from Google Sheets
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTWx9QyOcw3LrGb5RSQoOM7-d7rgIC-KUJrM0WVMaB8KyzMQddcokdQH5IZ8PU6hR0QzZnQ9W-Dma1f/pub?output=csv"
df = pd.read_csv(url)

df_trimmed = df.iloc[:20000]

df_trimmed.to_csv("trimmed_USA.csv", index=False)

print("✅")