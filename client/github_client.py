from client.secret import Token_Value

API_URL = "https://api.github.com"
GITHUB_TOKEN = Token_Value
headers = {
    "Authorization": "Bearer " + GITHUB_TOKEN,
    "Accept": "application/vnd.github.inertia-preview+json",
}
