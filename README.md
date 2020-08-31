# Change multiple sites' IP addresses in Cloudflare
All Domain in CloudFlare

## Config
In `define.py` change:
- `DOMAINS` : list domain need change IP addresses, none HTTP / HTTPS
- `AUTH` : Email Cloudflare, token get `Global API Key` in `https://dash.cloudflare.com/profile/api-tokens`
- `CURRENT_IP` : current IP addresses of DNS record type A
- `NEW_IP` : new IP addresses want to change
- `BASE_URL` : not change
- `HEADERS` : not change

## Run
Install Packages
```python
$ pip install -r requirements.txt
```

Run
```python
$ python main.py
```