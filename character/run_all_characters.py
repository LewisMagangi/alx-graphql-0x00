import requests
import json

url = "https://rickandmortyapi.com/graphql"
queries = {
    1: """query { character(id: 1) { id name status species type gender } }""",
    2: """query { character(id: 2) { id name status species type gender } }""",
    3: """query { character(id: 3) { id name status species type gender } }""",
    4: """query { character(id: 4) { id name status species type gender } }"""
}

for char_id, query in queries.items():
    response = requests.post(url, json={"query": query})
    data = response.json()
    with open(f"character-id-{char_id}-output.json", "w") as f:
        json.dump(data, f, indent=2)
    print(f"character-id-{char_id}-output.json saved.")
