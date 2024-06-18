import vt

API_KEY = '6ed83c1c5dbf8c5ebcf49dc936bb995a0f16f1c47143963596322c1f606257b1'

def lookup_ip(ip: str) -> dict:
    client = vt.Client(API_KEY)
    try:
        result = client.get_object(f"/ip_addresses/{ip}")
        return result.to_dict()
    except vt.error.APIError as e:
        return {"error": e.code, "message": e.message}
    finally:
        client.close()
