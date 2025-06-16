import requests

response = requests.get("https://api.github.com")
print("Status code:", response.status_code)
print("Content:", response.text[:100])  # Only print first 100 characters
