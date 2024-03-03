import json

def parse_json(json_str):
    try:
        data = json.loads(json_str)
    except json.JSONDecodeError as e:
        print("Error with JSON:", e)
        return None
    def parse(data):
        if isinstance(data, dict):
            return {key: parse(value) for key, value in data.items()}
        elif isinstance(data, list):
            return [parse(item) for item in data]
        else:
            return data
    return parse(data)

json_string = '{"name": "John", "age": 30, "city": "New York", "pets": [{"name": "Fluffy", "type": "cat"}, {"name": "Fido", "type": "dog"}]}'
parsed_data = parse_json(json_string)
print(parsed_data)
