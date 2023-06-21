import datetime
from jose import jwt

SECRET_KEY = '39a467cefcf4e6c089497704c20df96ebfd1e40dc0890cb8874a03b6ef4f8ffe'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE = 30
REFRESH_TOKEN_EXPIRE = 60 * 24 * 30


def create_access_token(data: dict):
    payload = data.copy()
    expire = datetime.datetime.now() + datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE)

    payload.update({'exp': expire})
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def create_refresh_token(data: dict):
    payload = data.copy()
    expire = datetime.datetime.now() + datetime.timedelta(minutes=REFRESH_TOKEN_EXPIRE)

    payload.update({'exp': expire})
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def jwt_decode(encoded_jwt):
    return jwt.decode(encoded_jwt, SECRET_KEY, algorithms=[ALGORITHM])


def get_access_refresh(data: dict):
    return {
        'access': create_access_token(data),
        'refresh': create_refresh_token(data)
    }


# задание 1
name = input('Enter your name: ')
encoded_jwt = create_access_token({'name': name})
print(encoded_jwt)

# задание 2
print(jwt_decode(encoded_jwt))

# задание 3
print(get_access_refresh({'name': name}))
