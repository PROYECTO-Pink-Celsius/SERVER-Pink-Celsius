from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from src import schemas
from src.data import sql_dao_users
from src.dependencies import get_db

router = APIRouter(
    prefix="",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.post("/register", response_model=schemas.Token)
async def register(
        user: schemas.User,
        db: Session = Depends(get_db)
):
    # raise HTTPException(status_code=400, detail="Not available")

    user_db = sql_dao_users.get_user(db, user.username)

    if user_db:
        raise HTTPException(status_code=400, detail="Username already registered")

    user_db = sql_dao_users.post_user(db, user.username, user.password)

    return {"access_token": user_db.token, "token_type": "bearer"}

@router.post("/token", response_model=schemas.Token)
async def login(
        form_data: OAuth2PasswordRequestForm = Depends(),
        db: Session = Depends(get_db)
):
    token = sql_dao_users.check_user(db, form_data.username, form_data.password)

    if not token:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    return {"access_token": token, "token_type": "bearer"}


@router.get("/user/me")
async def read_users_me(
        token: str = Depends(oauth2_scheme),
        db: Session = Depends(get_db)
):
    username = sql_dao_users.check_token(db, token)

    if not username:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")

    return {"username": username}
