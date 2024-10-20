from pydantic import BaseModel, Field

class User(BaseModel):
    username: str = Field(..., unique=True)
    email: str = Field(..., unique=True)
    password: str


class AuctionItem(BaseModel):
    name: str
    description: str
    starting_price: float