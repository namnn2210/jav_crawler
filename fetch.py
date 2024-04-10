import requests


def fetch_data(page_number):
    url = f"https://avdbapi.com/api.php/provide/vod/?ac=detail&pg={page_number}"
    print("Fetching data url: ", url)
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching data from API:", response.status_code)
        return None
