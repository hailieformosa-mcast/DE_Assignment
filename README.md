


# Event Management API – Assignment Submission

Hi! My name is Hailie Formosa and this is my submission for the Event Management REST API assignment. I built this project using FastAPI and MongoDB Atlas as part of my coursework. The process helped me learn a lot about backend development, APIs, and working with cloud databases.

**Date submitted:** January 15, 2026  
**Assignment:** Event Management REST API with FastAPI & MongoDB Atlas

---

## Overview
This project is a RESTful API for managing events, attendees, venues, ticket bookings, and multimedia assets (posters, videos, photos). It is built with FastAPI, uses MongoDB Atlas for data storage, and is ready for cloud deployment (Vercel).

---

## Features
- Full CRUD for:
  - Events
  - Attendees
  - Venues
  - Bookings
- Upload & retrieve:
  - Event posters (images)
  - Promotional videos
  - Venue photos
- Input validation with Pydantic
- Secure credentials with `.env`
- Deployed to Vercel (cloud hosting)

---


## Project Structure

DE_Assignment/
   main.py              (FastAPI app with all endpoints)
   requirements.txt     (Python dependencies)
   README.md            (Project documentation)
   .env                 (MongoDB Atlas credentials, not committed)
   .gitignore           (Ignores .env, .venv, __pycache__)
   vercel.json          (Vercel deployment config)
   poster_music.jpg     (Example event poster)
   promo_music.mp4      (Example promo video)
   venue_music.jpg      (Example venue photo)
   test_mongo.py        (MongoDB Atlas connection test script)
   __pycache__/

---

## Setup Instructions

1. **Clone the repository**
   git clone <your-github-repo-url>
   cd DE_Assignment
2. **Create a virtual environment**
   python -m venv .venv
   .venv\Scripts\activate
3. **Install dependencies**
   python -m pip install -r requirements.txt
4. **Configure MongoDB Atlas**
   - Create a cluster and database in MongoDB Atlas.
   - Whitelist your IP address in Atlas security settings.
   - Create a `.env` file in the project root:
   MONGO_URI=mongodb+srv://<username>:<password>@<cluster>.mongodb.net/<dbname>
   - Ensure `.env` is listed in `.gitignore`.
5. **Test MongoDB connection (optional)**
   python test_mongo.py
6. **Run the API locally**
   uvicorn main:app --reload
   - Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for Swagger UI.

---

## How to Run the API on Vercel

1. **Install Vercel CLI and login:**
   npm i -g vercel
   vercel login
2. **Deploy:**
   vercel --prod
3. **Add your `.env` variables** in the Vercel dashboard (Environment Variables section)
4. **Access your public API:**
   - Your API will be live at: https://your-vercel-project-url.vercel.app

---

## API Endpoints

- **Events:** `/events` (POST, GET), `/events/{id}` (GET, PUT, DELETE)
- **Attendees:** `/attendees` (POST, GET), `/attendees/{id}` (GET, PUT, DELETE)
- **Venues:** `/venues` (POST, GET), `/venues/{id}` (GET, PUT, DELETE)
- **Bookings:** `/bookings` (POST, GET), `/bookings/{id}` (GET, PUT, DELETE)
- **Upload Poster:** `/upload_event_poster/{event_id}` (POST)
- **Upload Promo Video:** `/upload_promo_video/{event_id}` (POST)
- **Upload Venue Photo:** `/upload_venue_photo/{venue_id}` (POST)
- **Get Posters/Videos/Photos:** `/event_posters`, `/promo_videos`, `/venue_photos` (GET)

See [main.py](main.py) for full details and request/response formats.

---

## Example Requests & Responses

### Create Event (POST /events)
Request:
// JSON
{
  "name": "Music Festival",
  "description": "A fun music event",
  "date": "2026-02-01",
  "venue_id": "abc123",
  "max_attendees": 500
}
```
Response:
// JSON
{
  "message": "Event created",
  "id": "65a1b2c3d4e5f6a7b8c9d0e1"
}
```

### Get All Events (GET /events)
Response:
// JSON
[
  {
    "_id": "65a1b2c3d4e5f6a7b8c9d0e1",
    "name": "Music Festival",
    "description": "A fun music event",
    "date": "2026-02-01",
    "venue_id": "abc123",
    "max_attendees": 500
  }
]
```

### Upload Event Poster (POST /upload_event_poster/{event_id})
Request: Multipart form-data with file upload (image)
Response:
// JSON
{
  "message": "Event poster uploaded",
  "id": "65a1b2c3d4e5f6a7b8c9d0e2"
}
```

---

## GitHub Repository

Repo URL: https://github.com/your-username/DE_Assignment

## Public API URL

Live API: https://your-vercel-project-url.vercel.app

---

## Security & Best Practices
- **Credentials:** All sensitive info is stored in `.env` (never committed to git)
- **IP Whitelisting:** Only allowed IPs can access MongoDB Atlas
- **Validation:** All input is validated using Pydantic models

---

## Testing
- Use Swagger UI ([/docs](http://127.0.0.1:8000/docs)) for interactive API testing
- Use Postman or curl for manual endpoint testing
- Example test script: `test_mongo.py` (checks Atlas connection)

---

## Screenshots & Documentation
- VS Code: Project structure, code open
- Terminal: venv activation, pip freeze, uvicorn run, git status
- MongoDB Atlas: Collections, IP whitelist
- DataGrip: DB connection, collections
- Swagger UI: API docs
- Example validation error

---

## Assignment Notes
- All requirements from the assignment brief are covered

---

