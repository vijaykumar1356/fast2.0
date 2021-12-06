from fastapi.routing import APIRouter
from .user import user_router as user

api_router = APIRouter()
api_router.include_router(user)


@api_router.get('/')
def say_hell():
    apis = {
        'users': {
            'REGISTER': '/api/v1/user/register',
            'LOGIN': '/api/v1/user/login',
            'LOGOUT': '/api/v1/user/logout',
            'GET ALL': '/api/v1/user',
            'GET': '/api/v1/user/uuid',
            'PUT': '/api/v1/user/uuid',
            'DELETE': '/api/v1/user/uuid'
        }
    }
    return apis
