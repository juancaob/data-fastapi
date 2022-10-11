from fastapi import status, HTTPException, Depends, APIRouter
from .. import models
from ..schemas import Vote
from ..database import get_db
from ..oauth2 import get_current_user
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/vote",
    tags=["Vote"]
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(vote: Vote, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    # Check if post_id exists:
    post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {vote.post_id} does not exist")
    # Check if the vote already exists
    # Step 1: check if there's a vote for the specific post
    # Setep 2: since multiple users can vote on same post
    # we have to include a second conditionafter the ","
    # if user_id of the posts is equal to the current user id
    vote_query = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id, models.Vote.user_id == current_user.id)
    found_vote = vote_query.first()
    if (vote.dir == 1):
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"User {current_user.id} has already voted on post {vote.post_id}")
        new_vote = models.Vote(post_id=vote.post_id, user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        return {"message": "Successfully added vote"}
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vote does not exists")
        vote_query.delete(synchronize_session=False)
        db.commit()
        return {"message": "Successfully deleted vote"}
