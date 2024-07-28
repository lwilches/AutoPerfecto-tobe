import requests

class ServicioAuthUser:
    def __init__(self, base_url):
        self.base_url = base_url
        self.token = None
        self.success = None
        self.user_id = None

    def authenticate(self, user_name, pwd):
        url = f"{self.base_url}/login"
        payload = {
            "user_name": user_name,
            "pwd": pwd
        }
        headers = {
            "Content-Type": "application/json"
        }

        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            data = response.json()
            self.token = data.get("access_token")
            self.success = data.get("success")
            self.user_id = data.get("user_id")
        else:
            print(f"Failed to authenticate: {response.status_code} - {response.text}")

# Ejemplo de uso
if __name__ == "__main__":
    auth_service = ServicioAuthUser("http://127.0.0.1:5000")
    auth_service.authenticate("lwilches", "123")

    print(f"Token: {auth_service.token}")
    print(f"Success: {auth_service.success}")
    print(f"User ID: {auth_service.user_id}")
