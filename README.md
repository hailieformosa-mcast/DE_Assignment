# Event Management API

This project is a RESTful API for managing events, attendees, venues, ticket bookings, and multimedia assets (posters, videos, photos) using FastAPI and MongoDB Atlas.

## Setup Instructions

1. **Create a virtual environment**
   ```
   python -m venv .venv
   .venv\Scripts\activate
   ```
2. **Install dependencies**
   ```
   python -m pip install fastapi uvicorn motor pydantic python-dotenv requests
   ```
3. **Set up MongoDB Atlas**
   - Create a cluster and database.
   - Add your connection string to a `.env` file:
     ```
     MONGO_URI=mongodb+srv://<username>:<password>@<cluster>.mongodb.net/<dbname>
     ```
   - Add `.env` to `.gitignore`.

4. **Run the API**
   ```
   uvicorn main:app --reload
   ```
   Access docs at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Endpoints
- CRUD for events, attendees, venues, bookings
- Upload/retrieve event posters, promo videos, venue photos

## Security
- Credentials stored in `.env`
- IP whitelisting in MongoDB Atlas
- Input validation using Pydantic

## Project Structure
```
DE_Assignment/
├── main.py
├── requirements.txt
├── README.md
├── .env
```

## Testing
- Use Postman for endpoint testing
- See API docs for details

## Deployment
- Can be deployed to Vercel (see assignment brief)

---

**Replace `<username>`, `<password>`, `<cluster>`, `<dbname>` in `.env` with your actual MongoDB Atlas credentials.**
