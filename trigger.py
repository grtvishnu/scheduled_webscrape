import requests

ngrok_url = 'http://4eab58c6824b.ngrok.io'
endpoint = f'{ngrok_url}/ '

r = requests.post(endpoint, json={})
print(r.json()['data'])
