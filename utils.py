import hmac
import hashlib

SECRET = "test_secret"

def verify_signature(body: bytes, signature: str) -> bool:
    expected_signature = hmac.new(
        SECRET.encode(), body, hashlib.sha256
    ).hexdigest()
    print("SERVER BODY BYTES:", repr(body))
    print("EXPECTED SIG:", expected_signature)
    print("CLIENT SIG:", signature)
    return hmac.compare_digest(expected_signature, signature)
