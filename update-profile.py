import os
import random
import requests

# Fetch a new quote
quote_response = requests.get('https://api.quotable.io/random')
quote_data = quote_response.json()
quote = quote_data['content']
author = quote_data['author']

# Format the quote
formatted_quote = f'"{quote}" - {author}'

# Fetch a list of all countries
countries_response = requests.get('https://restcountries.com/v3.1/all')
countries_data = countries_response.json()

# Select a random country
country_data = random.choice(countries_data)
country_name = country_data['name']['common']

# Format the location
formatted_location = country_name

# Update GitHub profile description and location
github_token = os.getenv('GITHUB_TOKEN')
headers = {
    'Accept': 'application/vnd.github+json',
    'Authorization': f'Bearer {github_token}'
}

# Update description and location
profile_data = {'bio': formatted_quote, 'location': formatted_location}
profile_response = requests.patch('https://api.github.com/user', headers=headers, json=profile_data)

if profile_response.status_code != 200:
    raise Exception('An error occurred while updating the profile:', profile_response.content)

# # Update status emoji
# status_data = {
#     'query': 'mutation ChangeUserStatus($input: ChangeUserStatusInput!) { changeUserStatus(input: $input) { clientMutationId } }',
#     'variables': {
#         'input': {
#             'emoji': f':{country_name.lower().replace(" ", "_")}:',
#             'message': 'Travelling the world'
#         }
#     }
# }
# status_response = requests.post('https://api.github.com/graphql', headers=headers, json=status_data)

# if status_response.status_code != 200:
#     raise Exception('An error occurred while updating the status:', status_response.content)


print('Profile description and location updated successfully')