from typing import List, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from apps.events.schemas import EventCreate, TicketResponse, VenueCreate
from apps.events.service import (
    create_event_service,
    create_venue_service,
    delete_event_service,
    delete_venue_service,
    get_all_events_service,
    get_all_tickets_service,
    get_all_venues_service,
    get_ticket_service,
    update_event_service,
    update_venue_service,
)
from auth.auth import AuthHandler
from common.common_response import common_response
from database.db import get_db

event_router = APIRouter()
auth_handle = AuthHandler()


# Event endpoints
@event_router.get("/events/")
async def get_all_events(
    _=Depends(auth_handle.auth_wrapper),
    event_id: Optional[int] = 0,
    db: Session = Depends(get_db),
):
    try:
        data = await get_all_events_service(db, event_id)
        return common_response(
            message="Events fetched successfully",
            status=True,
            data=data,
            status_code=200,
        )
    except Exception as err:
        return common_response(
            message=f"Due to this error {err}", status=False, status_code=500
        )


@event_router.post("/events/")
async def create_event(
    event: EventCreate,
    user=Depends(auth_handle.auth_wrapper),
    db: Session = Depends(get_db),
):
    try:
        data = await create_event_service(db, event, user.id)
        return common_response(
            message="Event created successfully",
            status=True,
            data=data,
            status_code=201,
        )
    except Exception as err:
        return common_response(
            message=f"Due to this error {err}", status=False, status_code=500
        )


@event_router.put("/events/")
async def update_event(
    event_id: int,
    event: EventCreate,
    user=Depends(auth_handle.auth_wrapper),
    db: Session = Depends(get_db),
):
    try:
        data = await update_event_service(db, event_id, event)
        return common_response(
            message="Event updated successfully",
            status=True,
            data=data,
            status_code=200,
        )
    except Exception as err:
        return common_response(
            message=f"Due to this error {err}", status=False, status_code=500
        )


@event_router.delete("/events/")
async def delete_event(
    event_id: int, user=Depends(auth_handle.auth_wrapper), db: Session = Depends(get_db)
):
    try:
        data = await delete_event_service(db, event_id)
        return common_response(
            message="Event deleted successfully",
            status=True,
            data=data,
            status_code=200,
        )
    except Exception as err:
        return common_response(
            message=f"Due to this error {err}", status=False, status_code=500
        )


# Venue endpoints
@event_router.get("/venues/")
async def get_all_venues(
    venue_id: Optional[int] = 0,
    _=Depends(auth_handle.auth_wrapper),
    db: Session = Depends(get_db),
):
    try:
        data = await get_all_venues_service(db, venue_id)
        return common_response(
            message="Venues fetched successfully",
            status=True,
            data=data,
            status_code=200,
        )
    except Exception as err:
        return common_response(
            message=f"Due to this error {err}", status=False, status_code=500
        )


@event_router.post("/venues/")
async def create_venue(
    venue: VenueCreate,
    user=Depends(auth_handle.auth_wrapper),
    db: Session = Depends(get_db),
):
    try:
        data = await create_venue_service(db, venue)
        return common_response(
            message="Venue created successfully",
            status=True,
            data=data,
            status_code=201,
        )
    except Exception as err:
        return common_response(
            message=f"Due to this error {err}", status=False, status_code=500
        )


@event_router.put("/venues/")
async def update_venue(
    venue_id: int,
    venue: VenueCreate,
    user=Depends(auth_handle.auth_wrapper),
    db: Session = Depends(get_db),
):
    try:
        data = await update_venue_service(db, venue_id, venue)
        return common_response(
            message="Venue updated successfully",
            status=True,
            data=data,
            status_code=200,
        )
    except Exception as err:
        return common_response(
            message=f"Due to this error {err}", status=False, status_code=500
        )


@event_router.delete("/venues/")
async def delete_venue(
    venue_id: int, user=Depends(auth_handle.auth_wrapper), db: Session = Depends(get_db)
):
    try:
        data = await delete_venue_service(db, venue_id)
        return common_response(
            message="Venue deleted successfully",
            status=True,
            data=data,
            status_code=200,
        )
    except Exception as err:
        return common_response(
            message=f"Due to this error {err}", status=False, status_code=500
        )


# Ticket endpoints
@event_router.get("/tickets", response_model=List[TicketResponse])
async def get_all_tickets(
    _=Depends(auth_handle.auth_wrapper),
    db: Session = Depends(get_db),
):
    try:
        data = await get_all_tickets_service(db)
        return common_response(
            message="Tickets fetched successfully",
            status=True,
            data=data,
            status_code=200,
        )
    except Exception as err:
        return common_response(
            message=f"Due to this error {err}", status=False, status_code=500
        )


@event_router.get("/tickets/{ticket_id}", response_model=TicketResponse)
async def get_ticket(
    ticket_id: int,
    _=Depends(auth_handle.auth_wrapper),
    db: Session = Depends(get_db),
):
    try:
        data = await get_ticket_service(db, ticket_id)
        return common_response(
            message="Ticket fetched successfully",
            status=True,
            data=data,
            status_code=200,
        )
    except Exception as err:
        return common_response(
            message=f"Due to this error {err}", status=False, status_code=500
        )
