from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    """
    A class representing a user with attributes: id, name, mail, and password.

    Attributes:
    id (Optional[int]): The unique identifier of the user.
    name (str): The name of the user.
    mail (str): The email address of the user.
    password (str): The password of the user.
    """
    id: Optional[int]
    name: str
    mail: str
    password: str