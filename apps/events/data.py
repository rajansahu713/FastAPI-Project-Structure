from sqlalchemy.orm import Session

from apps.events.models import Event, Registration, Ticket, Venue
from apps.events.schemas import (
    EventCreate,
    RegistrationCreate,
    TicketCreate,
    VenueCreate,
)


# Event CRUD operations
async def create_event(db: Session, event: EventCreate, user_id: int):
    db_item = Event(**event.dict(), CreatedBy=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


async def get_all_events(db: Session, event_id: int):
    if event_id:
        return db.query(Event).filter(Event.EventID == event_id).all()
    return db.query(Event).all()


async def update_event(db: Session, event_id: int, event: EventCreate):
    db_item = db.query(Event).filter(Event.EventID == event_id).first()
    db_item.EventName = event.EventName
    db_item.Description = event.Description
    db_item.StartDate = event.StartDate
    db_item.EndDate = event.EndDate
    db_item.VenueID = event.VenueID
    db.commit()
    db.refresh(db_item)
    return db_item


async def delete_event(db: Session, event_id: int):
    db_item = db.query(Event).filter(Event.EventID == event_id).first()
    db.delete(db_item)
    db.commit()
    return db_item


# Venue CRUD operations
async def create_venue(db: Session, venue: VenueCreate):
    db_item = Venue(**venue.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


async def get_all_venues(db: Session, venue_id: int):
    if venue_id:
        return db.query(Venue).filter(Venue.VenueID == venue_id).first()
    return db.query(Venue).all()


async def update_venue(db: Session, venue_id: int, venue: VenueCreate):
    db_item = db.query(Venue).filter(Venue.VenueID == venue_id).first()
    db_item.VenueName = venue.VenueName
    db_item.Address = venue.Address
    db_item.Capacity = venue.Capacity
    db.commit()
    db.refresh(db_item)
    return db_item


async def delete_venue(db: Session, venue_id: int):
    db_item = db.query(Venue).filter(Venue.VenueID == venue_id).first()
    db.delete(db_item)
    db.commit()
    return db_item


# Ticket CRUD operations
async def create_ticket(db: Session, ticket: TicketCreate):
    db_item = Ticket(**ticket.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


async def get_ticket(db: Session, ticket_id: int):
    return db.query(Ticket).filter(Ticket.TicketID == ticket_id).first()


async def get_all_tickets(db: Session):
    return db.query(Ticket).all()


async def update_ticket(db: Session, ticket_id: int, ticket: TicketCreate):
    db_item = db.query(Ticket).filter(Ticket.TicketID == ticket_id).first()
    db_item.EventID = ticket.EventID
    db_item.Price = ticket.Price
    db_item.Quantity = ticket.Quantity
    db.commit()
    db.refresh(db_item)
    return db_item


async def delete_ticket(db: Session, ticket_id: int):
    db_item = db.query(Ticket).filter(Ticket.TicketID == ticket_id).first()
    db.delete(db_item)
    db.commit()
    return db_item


# Registration CRUD operations
async def create_registration(db: Session, registration: RegistrationCreate):
    db_item = Registration(**registration.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


async def get_registration(db: Session, registration_id: int):
    return (
        db.query(Registration)
        .filter(Registration.RegistrationID == registration_id)
        .first()
    )


async def get_all_registrations(db: Session):
    return db.query(Registration).all()


async def update_registration(
    db: Session, registration_id: int, registration: RegistrationCreate
):
    db_item = (
        db.query(Registration)
        .filter(Registration.RegistrationID == registration_id)
        .first()
    )
    db_item.EventID = registration.EventID
    db_item.UserID = registration.UserID
    db.commit()
    db.refresh(db_item)
    return db_item


async def delete_registration(db: Session, registration_id: int):
    db_item = (
        db.query(Registration)
        .filter(Registration.RegistrationID == registration_id)
        .first()
    )
    db.delete(db_item)
    db.commit()
    return db_item
