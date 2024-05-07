PASSWORD = 'your_pixela_password'
USERNAME =  'your_pixela_username'


import requests

from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"


# Creating a new user.
user_params = {
     'token': PASSWORD,
     'username': USERNAME,
     'notMinor':'yes',
     'agreeTermsOfService':'yes'
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)


# Creating a new graph.
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    'id':'graph1',
    'name':'Coding Graph',
    'unit':'min',
    'type':'int',
    'color':'kuro'
}

headers = {
    'X-USER-TOKEN':PASSWORD,
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

print(response.text)


# Posting a pixel.
posting_pixel_endpoint = f'{graph_endpoint}/{graph_config['id']}'

today = datetime.now()

posting_pixel_config = {
    'date':today.strftime('%Y%m%d'),
    'quantity':'your_quantity',
}

response = requests.post(url=posting_pixel_endpoint, json=posting_pixel_config, headers=headers)

print(response.text)


# Updating a pixel.
updating_pixel_endpoint = f'{posting_pixel_endpoint}/{posting_pixel_config['date']}'

updating_pixel_config = {'quantity':'modified_quantity'}

response = requests.put(url=updating_pixel_endpoint, json=updating_pixel_config, headers=headers)

print(response.text)


# Deleting a pixel.
response = requests.delete(url=updating_pixel_endpoint,headers=headers)

print(response.text)