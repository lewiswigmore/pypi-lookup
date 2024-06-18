import vt

API_KEY = 'YOUR_API_KEY'

def lookup_ip(ip: str) -> dict:
    client = vt.Client(API_KEY)
    try:
        result = client.get_object(f"/ip_addresses/{ip}")
        return result.to_dict()
    except vt.error.APIError as e:
        return {"error": e.code, "message": e.message}
    finally:
        client.close()
