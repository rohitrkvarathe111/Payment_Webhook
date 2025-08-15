# import hmac, hashlib

# SECRET = "test_secret"
# with open("mock_payloads/payment_authorized.json", "rb") as f:
#     body = f.read()

# signature = hmac.new(SECRET.encode(), body, hashlib.sha256).hexdigest()
# print(signature)

import hmac, hashlib, sys

SECRET = "test_secret"

# file_path = sys.argv[1]  # path to json file
with open(sys.argv[1], "rb") as f:
    body = f.read()
sig = hmac.new(SECRET.encode(), body, hashlib.sha256).hexdigest()
print(sig)


