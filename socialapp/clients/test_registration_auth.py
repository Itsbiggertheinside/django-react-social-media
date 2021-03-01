import requests


def client():
    credentials = {
        'username': 'oylesinebirhesap3',
        'email': 'oylesinebir3@hesap.com',
        'password1': '6DsPG55gK',
        'password2': '6DsPG55gK'
    }

    response = requests.post(
        url = 'http://127.0.0.1:8000/api/rest-auth/registration/',
        data = credentials
    )

    print('Status Code:', response.status_code)

    data = response.json()

    print(data)


if __name__ == '__main__':
    client()