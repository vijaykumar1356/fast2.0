from fastapi.routing import APIRouter

api_router = APIRouter()


@api_router.get('/')
def say_hell():
    return {'msg': 'hello world!'}
