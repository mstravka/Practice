import bcrypt
import jwt
import datetime

password = b"my_secret_password"
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
print("Hashed password:", hashed)

check = bcrypt.checkpw(password, hashed)
print("Password correct?", check)

SECRET_KEY = "supersecretkey"
payload = {
    "user_id": 123,
    "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=30)
}
token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
print("JWT:", token)

decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
print("Decoded JWT:", decoded)

refresh_payload = {"user_id": 123}
refresh_token = jwt.encode(refresh_payload, SECRET_KEY, algorithm="HS256")
print("Refresh token:", refresh_token)
