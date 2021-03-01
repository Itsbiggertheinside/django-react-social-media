import requests


def client():
    credentials = {
        'username': 'anothermayk',
        'password': '6DsPG55gK'
    }

    response = requests.post(
        url = 'http://127.0.0.1:8000/api/rest-auth/login/',
        data = credentials
    )

    print('Status Code:', response.status_code)

    data = response.json()

    print(data)


if __name__ == '__main__':
    client()