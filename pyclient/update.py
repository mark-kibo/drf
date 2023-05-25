import requests

endpoint="http://localhost:8000/api/products/1/update/"


data={
"title":"my old friend"
}

response=requests.put(endpoint,json=data)
print(response.json())