import requests
import json

url = "https://rickandmortyapi.com/graphql"
query_template = """
query {
  characters(page: %d) {
    results {
      id
      name
      status
      image
    }
  }
}
"""

for page in range(1, 5):
    query = query_template % page
    response = requests.post(url, json={"query": query})
    data = response.json()
    with open(f"characters-page-{page}-output.json", "w") as f:
        json.dump(data, f, indent=2)
    print(f"characters-page-{page}-output.json saved.")
