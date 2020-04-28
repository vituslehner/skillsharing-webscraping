import requests

url = "https://de.wikipedia.org/wiki/Service-Level-Agreement"
response = requests.get(url)

with open("wikipedia.html", "wb") as file:
    file.write(response.content)
