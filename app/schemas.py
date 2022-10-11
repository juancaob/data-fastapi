# This file stores all the pydantic models to validate user input
from pydantic import BaseModel, EmailStr, conint
from typing import Optional, List
from datetime import datetime


class UserCreate(BaseModel):
    email: EmailStr
    password: str


# Response model for the user
class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True


# Request model for user authentication
class UserLogin(BaseModel):
    email: EmailStr
    password: str


class BatchPosts(BaseModel):
    posts: List


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


# Request model
class PostCreate(PostBase):
    pass


# Response model for the posts
class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    # This class is added so that pydantic knows is working que an sqlalchemy object
    class Config:
        orm_mode = True


class PostOut(BaseModel):
    Post: Post
    votes: int

    # This class is added so that pydantic knows is working que an sqlalchemy object
    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)
