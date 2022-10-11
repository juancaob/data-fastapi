from fastapi import status, HTTPException, Depends, APIRouter
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import database, models
from ..schemas import UserLogin, Token
from ..utils import verify
from ..oauth2 import create_acces_token

router = APIRouter(tags=["Authentication"])


@router.post("/login", response_model=Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):

    # The OAuthPassWordRequestForm will return dic:
    # {
    #     "usernama": "jacinto", instead of email so we need to use username
    #     "password": "12345"
    # }

    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials")
    if not verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials")
    # create a token
    access_token = create_acces_token(data={"user_id": user.id})
    return {"access_token": access_token, "token_type": "bearer"}


