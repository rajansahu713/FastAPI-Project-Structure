from sqlalchemy.orm import Session

from apps.events.data import (
    create_event,
    create_registration,
    create_ticket,
    create_venue,
    delete_event,
    delete_registration,
    delete_ticket,
    delete_venue,
    get_all_events,
    get_all_registrations,
    get_all_tickets,
    get_all_venues,
    get_registration,
    get_ticket,
    update_event,
    update_registration,
    update_ticket,
    update_venue,
)
from apps.events.schemas import (
    EventCreate,
    RegistrationCreate,
    TicketCreate,
    VenueCreate,
)


# Event services
async def create_event_service(db: Session, event: EventCreate, user_id: int):
    return await create_event(db, event, user_id)


async def get_all_events_service(db: Session, event_id: int):
    return await get_all_events(db, event_id)


async def update_event_service(db: Session, event_id: int, event: EventCreate):
    return await update_event(db, event_id, event)


async def delete_event_service(db: Session, event_id: int):
    return await delete_event(db, event_id)


# Venue services
async def create_venue_service(db: Session, venue: VenueCreate):
    return await create_venue(db, venue)


async def get_all_venues_service(db: Session, venue_id: int):
    return await get_all_venues(db, venue_id)


async def update_venue_service(db: Session, venue_id: int, venue: VenueCreate):
    return await update_venue(db, venue_id, venue)


async def delete_venue_service(db: Session, venue_id: int):
    return await delete_venue(db, venue_id)


# Ticket services
async def create_ticket_service(db: Session, ticket: TicketCreate):
    return await create_ticket(db, ticket)


async def get_ticket_service(db: Session, ticket_id: int):
    return await get_ticket(db, ticket_id)


async def get_all_tickets_service(db: Session):
    return await get_all_tickets(db)


async def update_ticket_service(db: Session, ticket_id: int, ticket: TicketCreate):
    return await update_ticket(db, ticket_id, ticket)


async def delete_ticket_service(db: Session, ticket_id: int):
    return await delete_ticket(db, ticket_id)


# Registration services
async def create_registration_service(db: Session, registration: RegistrationCreate):
    return await create_registration(db, registration)


async def get_registration_service(db: Session, registration_id: int):
    return await get_registration(db, registration_id)


async def get_all_registrations_service(db: Session):
    return await get_all_registrations(db)


async def update_registration_service(
    db: Session, registration_id: int, registration: RegistrationCreate
):
    return await update_registration(db, registration_id, registration)


async def delete_registration_service(db: Session, registration_id: int):
    return await delete_registration(db, registration_id)
