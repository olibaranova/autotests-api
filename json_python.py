import json

json_data = '{"name": "Ivan", "age": 23, "is_student": false}'
parsed_data = json.loads(json_data)
print(parsed_data)

data = {
  "name": "Иван",
  "age": 23,
  "is_student": False
}
new_parsed = json.dumps(data)
print(new_parsed)

with open("json_example.json", "r", encoding="utf-8") as file:
    new_data = json.load(file)
    print(new_data)