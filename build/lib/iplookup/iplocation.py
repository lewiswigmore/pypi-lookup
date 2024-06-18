import requests

def lookup_ip(ip: str) -> dict:
    url = f"https://api.iplocation.net/?ip={ip}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.status_code, "message": response.text}
