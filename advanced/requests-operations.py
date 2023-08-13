import requests

print("HTTP Requests")
print(requests.get("https://www.google.com.tr/"))
print(requests.get("https://www.google.com.tr/").content)
print(requests.get("https://www.google.com.tr/").text)
