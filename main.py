# Import necessary libraries
import os
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from dotenv import load_dotenv
import motor.motor_asyncio

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# Connect to MongoDB Atlas
MONGO_URI = "mongodb+srv://hailieformosae22027_db_user:eZDyarcysXaHQI3y@databasedeployments.glu6ktw.mongodb.net/event_management_db?appName=DatabaseDeployments"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = client["event_management_db"]

# Data Models
class Event(BaseModel):
    name: str
    description: str
    date: str
    venue_id: str
    max_attendees: int

class Attendee(BaseModel):
    name: str
    email: str
    phone: Optional[str] = None

class Venue(BaseModel):
    name: str
    address: str
    capacity: int

class Booking(BaseModel):
    event_id: str
    attendee_id: str
    ticket_type: str
    quantity: int

# Event Endpoints
@app.post("/events")
async def create_event(event: Event):
    event_doc = event.dict()
    result = await db.events.insert_one(event_doc)
    return {"message": "Event created", "id": str(result.inserted_id)}

@app.get("/events")
async def get_events():
    events = await db.events.find().to_list(100)
    for event in events:
        event["_id"] = str(event["_id"])
    return events

# Get single event by ID
from bson import ObjectId

@app.get("/events/{event_id}")
async def get_event(event_id: str):
    event = await db.events.find_one({"_id": ObjectId(event_id)})
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    event["_id"] = str(event["_id"])
    return event

# Update event by ID
@app.put("/events/{event_id}")
async def update_event(event_id: str, event: Event):
    result = await db.events.update_one({"_id": ObjectId(event_id)}, {"$set": event.dict()})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Event not found")
    return {"message": "Event updated"}

# Delete event by ID
@app.delete("/events/{event_id}")
async def delete_event(event_id: str):
    result = await db.events.delete_one({"_id": ObjectId(event_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Event not found")
    return {"message": "Event deleted"}

# Attendee Endpoints
@app.post("/attendees")
async def create_attendee(attendee: Attendee):
    attendee_doc = attendee.dict()
    result = await db.attendees.insert_one(attendee_doc)
    return {"message": "Attendee created", "id": str(result.inserted_id)}

# Get all attendees
@app.get("/attendees")
async def get_attendees():
    attendees = await db.attendees.find().to_list(100)
    for attendee in attendees:
        attendee["_id"] = str(attendee["_id"])
    return attendees

# Get single attendee by ID
@app.get("/attendees/{attendee_id}")
async def get_attendee(attendee_id: str):
    attendee = await db.attendees.find_one({"_id": ObjectId(attendee_id)})
    if not attendee:
        raise HTTPException(status_code=404, detail="Attendee not found")
    attendee["_id"] = str(attendee["_id"])
    return attendee

# Update attendee by ID
@app.put("/attendees/{attendee_id}")
async def update_attendee(attendee_id: str, attendee: Attendee):
    result = await db.attendees.update_one({"_id": ObjectId(attendee_id)}, {"$set": attendee.dict()})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Attendee not found")
    return {"message": "Attendee updated"}

# Delete attendee by ID
@app.delete("/attendees/{attendee_id}")
async def delete_attendee(attendee_id: str):
    result = await db.attendees.delete_one({"_id": ObjectId(attendee_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Attendee not found")
    return {"message": "Attendee deleted"}

# Venue Endpoints
@app.post("/venues")
async def create_venue(venue: Venue):
    venue_doc = venue.dict()
    result = await db.venues.insert_one(venue_doc)
    return {"message": "Venue created", "id": str(result.inserted_id)}

# Get all venues
@app.get("/venues")
async def get_venues():
    venues = await db.venues.find().to_list(100)
    for venue in venues:
        venue["_id"] = str(venue["_id"])
    return venues

# Get single venue by ID
@app.get("/venues/{venue_id}")
async def get_venue(venue_id: str):
    venue = await db.venues.find_one({"_id": ObjectId(venue_id)})
    if not venue:
        raise HTTPException(status_code=404, detail="Venue not found")
    venue["_id"] = str(venue["_id"])
    return venue

# Update venue by ID
@app.put("/venues/{venue_id}")
async def update_venue(venue_id: str, venue: Venue):
    result = await db.venues.update_one({"_id": ObjectId(venue_id)}, {"$set": venue.dict()})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Venue not found")
    return {"message": "Venue updated"}

# Delete venue by ID
@app.delete("/venues/{venue_id}")
async def delete_venue(venue_id: str):
    result = await db.venues.delete_one({"_id": ObjectId(venue_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Venue not found")
    return {"message": "Venue deleted"}

# Booking Endpoints
@app.post("/bookings")
async def create_booking(booking: Booking):
    booking_doc = booking.dict()
    result = await db.bookings.insert_one(booking_doc)
    return {"message": "Booking created", "id": str(result.inserted_id)}

# Get all bookings
@app.get("/bookings")
async def get_bookings():
    bookings = await db.bookings.find().to_list(100)
    for booking in bookings:
        booking["_id"] = str(booking["_id"])
    return bookings

# Get single booking by ID
@app.get("/bookings/{booking_id}")
async def get_booking(booking_id: str):
    booking = await db.bookings.find_one({"_id": ObjectId(booking_id)})
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    booking["_id"] = str(booking["_id"])
    return booking

# Update booking by ID
@app.put("/bookings/{booking_id}")
async def update_booking(booking_id: str, booking: Booking):
    result = await db.bookings.update_one({"_id": ObjectId(booking_id)}, {"$set": booking.dict()})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Booking not found")
    return {"message": "Booking updated"}

# Delete booking by ID
@app.delete("/bookings/{booking_id}")
async def delete_booking(booking_id: str):
    result = await db.bookings.delete_one({"_id": ObjectId(booking_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Booking not found")
    return {"message": "Booking deleted"}

# Upload Event Poster (Image)
@app.post("/upload_event_poster/{event_id}")
async def upload_event_poster(event_id: str, file: UploadFile = File(...)):
    content = await file.read()
    poster_doc = {
        "event_id": event_id,
        "filename": file.filename,
        "content_type": file.content_type,
        "content": content,
        "uploaded_at": datetime.utcnow()
    }
    result = await db.event_posters.insert_one(poster_doc)
    return {"message": "Event poster uploaded", "id": str(result.inserted_id)}

# Get all event posters
@app.get("/event_posters")
async def get_event_posters():
    posters = await db.event_posters.find().to_list(100)
    for poster in posters:
        poster["_id"] = str(poster["_id"])
    return posters

# Get single event poster by ID
@app.get("/event_posters/{poster_id}")
async def get_event_poster(poster_id: str):
    poster = await db.event_posters.find_one({"_id": ObjectId(poster_id)})
    if not poster:
        raise HTTPException(status_code=404, detail="Event poster not found")
    poster["_id"] = str(poster["_id"])
    return poster


# Upload Promotional Video
@app.post("/upload_promo_video/{event_id}")
async def upload_promo_video(event_id: str, file: UploadFile = File(...)):
    content = await file.read()
    video_doc = {
        "event_id": event_id,
        "filename": file.filename,
        "content_type": file.content_type,
        "content": content,
        "uploaded_at": datetime.utcnow()
    }
    result = await db.promo_videos.insert_one(video_doc)
    return {"message": "Promotional video uploaded", "id": str(result.inserted_id)}

# Get all promotional videos
@app.get("/promo_videos")
async def get_promo_videos():
    videos = await db.promo_videos.find().to_list(100)
    for video in videos:
        video["_id"] = str(video["_id"])
    return videos

# Get single promotional video by ID
@app.get("/promo_videos/{video_id}")
async def get_promo_video(video_id: str):
    video = await db.promo_videos.find_one({"_id": ObjectId(video_id)})
    if not video:
        raise HTTPException(status_code=404, detail="Promotional video not found")
    video["_id"] = str(video["_id"])
    return video

# Upload Venue Photo
@app.post("/upload_venue_photo/{venue_id}")
async def upload_venue_photo(venue_id: str, file: UploadFile = File(...)):
    content = await file.read()
    photo_doc = {
        "venue_id": venue_id,
        "filename": file.filename,
        "content_type": file.content_type,
        "content": content,
        "uploaded_at": datetime.utcnow()
    }
    result = await db.venue_photos.insert_one(photo_doc)
    return {"message": "Venue photo uploaded", "id": str(result.inserted_id)}

# Get all venue photos
@app.get("/venue_photos")
async def get_venue_photos():
    photos = await db.venue_photos.find().to_list(100)
    for photo in photos:
        photo["_id"] = str(photo["_id"])
    return photos

# Get single venue photo by ID
@app.get("/venue_photos/{photo_id}")
async def get_venue_photo(photo_id: str):
    photo = await db.venue_photos.find_one({"_id": ObjectId(photo_id)})
    if not photo:
        raise HTTPException(status_code=404, detail="Venue photo not found")
    photo["_id"] = str(photo["_id"])
    return photo

@app.get("/")
def read_root():
    return {"message": "Event Management API"}
