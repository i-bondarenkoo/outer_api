import json
from pydantic import BaseModel
import aiohttp
from fastapi import FastAPI, HTTPException, Query, Path, status
import uvicorn
from typing import Annotated

app = FastAPI()


class ResponseUser(BaseModel):
    id: int
    name: str
    username: str
    city: str
    email: str
    street: str


class PostResponse(BaseModel):
    body: str
    id: int
    title: str
    userId: int


class CommentsResponse(BaseModel):
    postId: int
    id: int
    name: str
    email: str
    body: str


class CreatePostRequest(BaseModel):
    id: int
    title: str
    body: str
    userId: int


async def fetch_data(url: str):
    async with aiohttp.ClientSession() as session:
        response = await session.get(url)
        print(response.status)
        data = await response.json()
        return data


async def post_data(url: str, payload: dict):
    async with aiohttp.ClientSession() as session:
        request = await session.post(
            url,
            json=payload,
            headers={"Content-type": "application/json"},
        )
        return request


@app.get("/users", response_model=list[ResponseUser])
async def get_user_from_fakeapi():
    users = await fetch_data("https://jsonplaceholder.typicode.com/users")
    list_users = []
    for user in users:
        list_users.append(
            ResponseUser(
                id=user["id"],
                name=user["name"],
                username=user["username"],
                city=user["address"]["city"],
                email=user["email"],
                street=user["address"]["street"],
            )
        )
    return list_users


@app.get("/posts", response_model=list[PostResponse])
async def get_post_by_user_id(
    user_id: int = Query(1, gt=0, description="ID пользователя для просмотра постов")
):
    posts: list = await fetch_data(
        f"https://jsonplaceholder.typicode.com/posts?userId={user_id}"
    )
    if not posts:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Пользователь не найден",
        )
    print(posts)
    return posts


@app.get("/comments", response_model=list[CommentsResponse])
async def get_comments_by_user_id(
    post_id: int = Query(
        1, gt=0, description="ID пользователя для просмотра комментариев"
    )
):
    comments: list = await fetch_data(
        f"https://jsonplaceholder.typicode.com/comments?postId={post_id}"
    )
    return comments


@app.post("/create-post", response_model=CreatePostRequest)
async def create_post(post_in: CreatePostRequest):
    info = post_in.model_dump()
    return await post_data("https://jsonplaceholder.typicode.com/posts", info)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
