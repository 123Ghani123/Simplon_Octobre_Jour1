import requests


if __name__ == '__main__':
    url = "https://icanhazdadjoke.com/"
    headers = {"Accept": "application/json"}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        print(response.json())
    except requests.exceptions.HTTPError as errh:
        print("HTTPError--> " + str(errh))
    except requests.exceptions.ConnectionError as errc:
        print("ConnectionError--> " + str(errc))
    except requests.exceptions.Timeout as errt:
        print("TimeoutError--> " + str(errt))
    except requests.exceptions.RequestException as err:
        print("RequestExceptionError--> " + str(err))

