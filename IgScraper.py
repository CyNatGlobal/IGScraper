import requests
import pandas as pd

# API call 1
url = "https://instagram-scraper-api2.p.rapidapi.com/v1/info"
querystring = {"username_or_id_or_url":"inserturl","include_about":"true","url_embed_safe":"true"}
headers = {
	"x-rapidapi-key": "insertapikey",
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
