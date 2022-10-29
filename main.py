import requests

response = requests.post("https://petstore.swagger.io/v2/pet", json={
  "id": 30,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "tubik",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})
print(response.text)
