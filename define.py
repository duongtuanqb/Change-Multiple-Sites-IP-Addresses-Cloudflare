DOMAINS = []

AUTH = {
    'email': '<email>',
    'token': '<token>',
}

CURRENT_IP = '<current_IP>'
NEW_IP = '<new_IP>'

BASE_URL = 'https://api.cloudflare.com/client/v4'

HEADERS = {
    'Content-Type': 'application/json',
    'X-Auth-Email': AUTH['email'],
    'X-Auth-Key': AUTH['token']
}