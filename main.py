import requests

url = 'https://api.bag.kadaster.nl/lvbag/individuelebevragingen/v2/'
#key= '936fdb7b-147f-4726-b4be-95d8c7b64c38'

response = requests.get(url,
	params={'X-Api-Key' : '936fdb7b-147f-4726-b4be-95d8c7b64c38'}
)
print(response.status_code)
