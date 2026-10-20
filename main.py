import requests

def show_user(username):
    response = requests.get(f"https://api.github.com/users/{username}")
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