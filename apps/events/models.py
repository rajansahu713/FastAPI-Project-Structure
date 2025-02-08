from sqlalchemy import (
    DECIMAL,
    TIMESTAMP,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
    func,
)
from database.db import Base


class Venue(Base):
    __tablename__ = "venues"
    VenueID = Column(Integer, primary_key=True, index=True)
    VenueName = Column(String(100), nullable=False)
    Address = Column(String(255), nullable=False)
    Capacity = Column(Integer, nullable=False)


class Event(Base):
    __tablename__ = "events"
    EventID = Column(Integer, primary_key=True, index=True)
    EventName = Column(String(100), nullable=False)
    Description = Column(Text)
    StartDate = Column(DateTime, nullable=False)
    EndDate = Column(DateTime, nullable=False)
    VenueID = Column(Integer, ForeignKey("venues.VenueID"))
    CreatedBy = Column(Integer, ForeignKey("users.id"))
    CreatedAt = Column(TIMESTAMP, server_default=func.now())


class Ticket(Base):
    __tablename__ = "tickets"
    TicketID = Column(Integer, primary_key=True, index=True)
    EventID = Column(Integer, ForeignKey("events.EventID"))
    TicketType = Column(String(50), nullable=False)
    Price = Column(DECIMAL(10, 2), nullable=False)
    Quantity = Column(Integer, nullable=False)


class Registration(Base):
    __tablename__ = "registrations"
    RegistrationID = Column(Integer, primary_key=True, index=True)
    UserID = Column(Integer, ForeignKey("users.id"))
    EventID = Column(Integer, ForeignKey("events.EventID"))
    TicketID = Column(Integer, ForeignKey("tickets.TicketID"))
    RegistrationDate = Column(TIMESTAMP, server_default=func.now())
