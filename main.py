import requests

def show_user(username):
    try:
        response = requests.get(f"https://api.github.com/users/{username}", timeout=10)
    except requests.exceptions.RequestException:
        print("Нет связи с сервером. Проверьте интернет и адрес")
        return

    if response.status_code == 200:
        data = response.json()
        print("Логин:", data["login"])
        print("Репозиториев:", data["public_repos"])
    elif response.status_code == 404:
        print("Пользователь не найден")
    else:
        print("Что-то пошло не так, код:", response.status_code)

name = input("Введите имя пользователя GitHub: ")
show_user(name)