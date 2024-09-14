# IGScraper

# Instagram Scraper Script with CSV File Outputs

This script performs an API call to scrape Instagram data, converts it to a CSV, and then transposes the CSV content to create a second output file.
Here's an explanation of the script:

---

### Script Overview:

This Python script automates the process of retrieving Instagram data via an API, organizing it into a CSV file, and then transposing the data to create a second CSV file. It uses the `requests` library to make an API call and `pandas` for data manipulation and exporting.

---

### Steps Explained:

#### 1. **API Call to Instagram Scraper**

The first part of the script makes a GET request to an Instagram scraper API using the `requests` library. Here’s how it works:

- **URL**: The script targets the `https://instagram-scraper-api2.p.rapidapi.com/v1/info` endpoint to gather information about the Instagram account with the handle `xrlab.io`.
  
- **Query Parameters**: 
  - `username_or_id_or_url`: Specifies the target Instagram username or URL.
  - `include_about`: Includes the "about" information of the Instagram account.
  - `url_embed_safe`: Requests data that is safe for embedding (this might refer to image or media URL formats).

- **Headers**: The script includes an API key (`x-rapidapi-key`) and the host information (`x-rapidapi-host`) required for authentication.

- **Response**: The API returns data in JSON format, which is printed to the console using `print(response.json())`. This JSON contains various details about the Instagram account, such as the bio, number of followers, posts, and other relevant information.

#### 2. **Converting JSON to DataFrame**

After receiving the API response:

- The JSON data is converted into a Pandas DataFrame (`df = pd.json_normalize(data)`), which is a table-like structure that makes it easier to manipulate and analyze the data.
- The DataFrame is printed to the console to display the organized data.

#### 3. **Exporting Data to CSV File**

Once the data is converted into a DataFrame, it is saved to a CSV file:

- **File Name**: `instagram_data.csv`.
- **Reason**: Saving the data in a CSV file makes it easier to store, share, and analyze further using tools like Excel, Google Sheets, or other data manipulation programs.

#### 4. **Loading and Transposing the Data**

Next, the script assumes the `instagram_data.csv` file was created and loads it back into a DataFrame:

- **Transposition**: It transposes the DataFrame, which means it switches the rows and columns. This is useful in situations where you'd prefer to see the data attributes as rows and each Instagram account or item as a column.
  
- **Displaying the Transposed Data**: The script prints the transposed DataFrame for verification.

#### 5. **Exporting the Transposed Data to a New CSV File**

Finally, the transposed DataFrame is saved to a new CSV file:

- **File Name**: `instagram_data_transposed.csv`.
- **Purpose**: This file contains the same data but with rows and columns flipped, offering a different view of the information.

---

### Summary:

- **Input**: Instagram username or URL.
- **Process**: 
  - Make an API request to get Instagram data.
  - Store it in a DataFrame, save as a CSV.
  - Transpose the data and save it as a second CSV file.
- **Output**: Two CSV files (`instagram_data.csv` and `instagram_data_transposed.csv`).

This script helps automate the process of collecting data from Instagram and exporting it in a format that is easy to analyze.

### Code Block:

```python
import requests
import pandas as pd

# API call 1
url = "https://instagram-scraper-api2.p.rapidapi.com/v1/info"
querystring = {
    "username_or_id_or_url": "xrlab.io",
    "include_about": "true",
    "url_embed_safe": "true"
}
headers = {
    "x-rapidapi-key": "5b987145bdmshd0cd597231ccf87p180d92jsn99fd5ca2c2c8",
    "x-rapidapi-host": "instagram-scraper-api2.p.rapidapi.com"
}
response = requests.get(url, headers=headers, params=querystring)

# Print the JSON results
print(response.json())

# Convert JSON to a DataFrame
data = response.json()
df = pd.json_normalize(data)

# Display the DataFrame
print(df)

# Export the DataFrame to a CSV file
df.to_csv('instagram_data.csv', index=False)

# Assuming 'instagram_data.csv' exists from the previous code
df = pd.read_csv('instagram_data.csv')

# Transpose the DataFrame
df_transposed = df.transpose()

# Display the transposed DataFrame
print(df_transposed)

# Export the transposed DataFrame to a new CSV file
df_transposed.to_csv('instagram_data_transposed.csv', index=True)
