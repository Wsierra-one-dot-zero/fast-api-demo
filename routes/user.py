from fastapi import APIRouter, HTTPException
#from sqlalchemy.exc import SQLAlchemyError
#from sqlalchemy import select
#from config.db import conn
#from models.user import users
from schemas.user import User

from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

user = APIRouter()

@user.get("/users")
def get_users():
    """ try:
        result = conn.execute(users.select()).fetchall()
        users_list = [dict(row._mapping) for row in result]  # Convert each row to a dictionary
        return users_list
    except SQLAlchemyError as e:
        print(str(e))
        raise HTTPException(status_code=500, detail="An error occurred while fetching users") """
    return {"message": "Metodo get, return users"}
    

@user.post("/users")
def create_user(user: User):
    """ try:
        new_user = {"name": user.name, "mail": user.mail}
        new_user["password"] = f.encrypt(user.password.encode("utf-8"))
        result = conn.execute(users.insert().values(new_user))
        conn.commit()  # Commit the transaction
        print(new_user)
        print(result.inserted_primary_key)  # Print the inserted primary key
        return {"message": f"User {user.name} created successfully"}  # Use f-string to include the user name
    except SQLAlchemyError as e:
        print(str(e))
        raise HTTPException(status_code=500, detail="An error occurred while creating the user") """
    return {"message": "Metodo post, create user"}
    

@user.get("/users/{user_id}")
def get_user_by_id(user_id: int):
    # try:
    #     result = conn.execute(users.select().where(users.c.id == user_id))
    #     users_list = [dict(row._mapping) for row in result]  # Convert each row to a dictionary
    #     return users_list
    # except SQLAlchemyError as e:
    #     print(str(e))
    #     raise HTTPException(status_code=500, detail="An error occurred while fetching users")
    #----------------------------------------------------------------
    # try:
    #     result = conn.execute(users.select().where(users.c.id == user_id)).fetchone()
    #     if result is None:
    #         raise HTTPException(status_code=404, detail="User not found")
    #     user_dict = dict(result._mapping)  # Convert the row to a dictionary
    #     user_name = user_dict["name"]  # Extract the 'name' field from the dictionary
    #     return {"name": user_name}
    # except SQLAlchemyError as e:
    #     print(str(e))
    #     raise HTTPException(status_code=500, detail="An error occurred while fetching the user")
    """ try:
        result = conn.execute(users.select().where(users.c.id == user_id)).first()
        if result is None:
            raise HTTPException(status_code=404, detail="User not found")
        user_dict = dict(result._mapping)  # Convert the row to a dictionary
        return user_dict
    except SQLAlchemyError as e:
        print(str(e))
        raise HTTPException(status_code=500, detail="An error occurred while fetching the user") """
    return {"message": f"Metodo get, return user by id {user_id}"}

@user.delete("/users/{user_id}")
def delete_user_by_id(user_id: int):
    """ try:
        result = conn.execute(users.delete().where(users.c.id == user_id))
        conn.commit() 
        print(result)
        return {"message": f"User delete successfully"}
    except SQLAlchemyError as e:
        print(str(e))
        raise HTTPException(status_code=500, detail="An error occurred while fetching users") """
    return {"message": f"Metodo delete, delete user by id {user_id}"}
    

@user.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    """ try:
        # Check if the user exists
        existing_user = conn.execute(users.select().where(users.c.id == user_id)).fetchone()
        if existing_user is None:
            raise HTTPException(status_code=404, detail="User not found")
        
        # Prepare new data
        updated_user = {
            "name": user.name,
            "mail": user.mail,
            "password": f.encrypt(user.password.encode("utf-8"))
        }
        
        # Performing the update
        conn.execute(users.update().where(users.c.id == user_id).values(updated_user))
        conn.commit()  # Commit the transaction

        return {"message": "User updated successfully"}
    except SQLAlchemyError as e:
        print(str(e))
        raise HTTPException(status_code=500, detail="An error occurred while updating the user") """
    return {"message": f"Metodo put, update user by id {user_id}"}