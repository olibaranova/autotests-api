import httpx


response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")

print(response.json())
print(response.status_code)

data = {
    "title": "completed false",
    "completed": False,
    "userId": 1
}
response = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)
print(response.status_code)
print(response.json())


data = {
    "username": "testik", "password": "12345"
}

response = httpx.post("https://httpbin.org/post", data=data)
print(response.status_code)
print(response.json())

headers = {
    "Authorization": "Bearer my_secret_token
}