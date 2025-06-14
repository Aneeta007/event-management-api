from fastapi import APIRouter, HTTPException
from schemas.user import UserCreate, User
from data.store import users, user_id_seq

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=User)
def create_user(user: UserCreate):
    global user_id_seq
    new_user = user.dict()
    new_user.update({"id": user_id_seq, "is_active": True})
    users[user_id_seq] = new_user
    user_id_seq += 1
    return new_user

@router.get("/", response_model=list[User])
def get_users():
    return list(users.values())

@router.put("/{user_id}", response_model=User)
def update_user(user_id: int, updated: UserCreate):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    users[user_id].update(updated.dict())
    return users[user_id]

@router.delete("/{user_id}")
def delete_user(user_id: int):
    if user_id in users:
        del users[user_id]
        return {"detail": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")

@router.patch("/{user_id}/deactivate")
def deactivate_user(user_id: int):
    if user_id in users:
        users[user_id]["is_active"] = False
        return {"detail": "User deactivated"}
    raise HTTPException(status_code=404, detail="User not found")
