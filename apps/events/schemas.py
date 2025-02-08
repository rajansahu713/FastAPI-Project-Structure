from datetime import datetime

from pydantic import BaseModel


class VenueCreate(BaseModel):
    VenueName: str
    Address: str
    Capacity: int


class VenueResponse(BaseModel):
    VenueID: int
    VenueName: str
    Address: str
    Capacity: int

    class Config:
        orm_mode = True


class EventCreate(BaseModel):
    EventName: str
    Description: str
    StartDate: datetime
    EndDate: datetime
    VenueID: int


class EventResponse(BaseModel):
    EventID: int
    EventName: str
    Description: str
    StartDate: datetime
    EndDate: datetime
    VenueID: int

    class Config:
        orm_mode = True


class TicketCreate(BaseModel):
    EventID: int
    Price: float
    Quantity: int


class TicketResponse(BaseModel):
    TicketID: int
    EventID: int
    Price: float
    Quantity: int

    class Config:
        orm_mode = True


class RegistrationCreate(BaseModel):
    EventID: int
    UserID: int


class RegistrationResponse(BaseModel):
    RegistrationID: int
    EventID: int
    UserID: int
    Timestamp: datetime

    class Config:
        orm_mode = True
