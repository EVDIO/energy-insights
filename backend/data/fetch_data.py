import requests
import json

# Base URL for the API
BASE_URL = "https://api.energidataservice.dk/dataset"

# Function to fetch data from the API
def fetch_data(dataset_name, start=None, end=None, columns=None, filter=None, sort=None, offset=None, limit=None):
    # Construct the URL
    url = f"{BASE_URL}/{dataset_name}?"
    params = []

    if start:
        params.append(f"start={start}")
    if end:
        params.append(f"end={end}")
    if columns:
        params.append(f"columns={columns}")
    if filter:
        params.append(f"filter={json.dumps(filter)}")
    if sort:
        params.append(f"sort={sort}")
    if offset:
        params.append(f"offset={offset}")
    if limit:
        params.append(f"limit={limit}")

    # Combine all parameters into the URL
    url += "&".join(params)
    
    # Make the GET request
    response = requests.get(url)
    
    # Check for successful response
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

# Function to download data in a specific format
def download_data(dataset_name, format, limit=None):
    # Construct the URL for downloading data
    url = f"{BASE_URL}/{dataset_name}/download?format={format}"
    if limit:
        url += f"&limit={limit}"
    
    # Make the GET request
    response = requests.get(url)
    
    # Check for successful response
    if response.status_code == 200:
        return response.content
    else:
        response.raise_for_status()

# Example usage
if __name__ == "__main__":

    dataset_name = "PowerSystemRightNow"
    # dataset_name = "ConsumptionIndustry"
    # dataset_name = "Forecasts_5Min"
    # dataset_name = "ConsumptionPerGridarea"

    # Example 1: Fetch data with specific parameters
    start = None
    end = None
    #columns = "Minutes5DK,PriceArea,CO2Emission"
    columns = None
    #filter_params = {"PriceArea": ["DK1"]}
    filter_params = None
    #sort = "CO2Emission desc"
    sort = None
    limit = 4
    
    data = fetch_data(dataset_name, start=start, end=end, columns=columns, filter=filter_params, sort=sort, limit=limit)
    print(json.dumps(data, indent=2))
    
    # # Example 2: Download data as CSV
    # csv_data = download_data(dataset_name, format="csv", limit=10)
    # with open("data.csv", "wb") as file:
    #     file.write(csv_data)
    
    # # Example 3: Download data as Excel
    # excel_data = download_data(dataset_name, format="XL", limit=10)
    # with open("data.xlsx", "wb") as file:
    #     file.write(excel_data)
    
    # # Example 4: Download data as JSON
    # json_data = download_data(dataset_name, format="json", limit=10)
    # with open("data.json", "wb") as file:
    #     file.write(json_data)
