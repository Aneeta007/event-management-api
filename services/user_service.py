from schemas.user import UserCreate, User
from typing import List

users: List[User] = []
user_id_counter = 1

def create_user(user_data: UserCreate) -> User:
    global user_id_counter
    new_user = User(id=user_id_counter, name=user_data.name, email=user_data.email, is_active=True)
    users.append(new_user)
    user_id_counter += 1
    return new_user

def get_users() -> List[User]:
    return users

def update_user(user_id: int, user_data: UserCreate):
    for user in users:
        if user.id == user_id:
            user.name = user_data.name
            user.email = user_data.email
            return user
    return None

def delete_user(user_id: int):
    global users
    users = [user for user in users if user.id != user_id]

def deactivate_user(user_id: int):
    for user in users:
        if user.id == user_id:
            user.is_active = False
            return user
    return None