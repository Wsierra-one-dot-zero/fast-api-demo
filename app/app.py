from fastapi import FastAPI
from routes.user import user
from mangum import Mangum
"""
This module includes the FastAPI application configuration and router inclusion.

Attributes:
----------
app : FastAPI
    The FastAPI application instance.

Functions:
----------
None

Classes:
--------
None
"""
app = FastAPI()
# Include the user router in the FastAPI application
#
# Parameters:
# ----------
# user : Router
#     The router object containing the user-related endpoints.
#
# Returns:
# -------
# None
#
# Note:
# The user router is included in the FastAPI application to make the user-related endpoints accessible.
app.include_router(user)

handler = Mangum(app)