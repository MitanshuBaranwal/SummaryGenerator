# Summary Generator API
This is a Django-based API that leverages OpenAI's GPT-3.5-turbo model to generate summaries and bullet points from provided text. The API is secured using JWT (JSON Web Tokens) for authentication.

Features
## Generate Summary: 
Accepts a text input and returns a summarized version of the text using an API endpoint /generate-summary/ that accepts text input and uses OpenAI to generate a summary.

## Generate Bullet Points: 
Accepts a text input and returns bullet points summarizing the text using an API endpoint /generate-bullet-points/ that accepts a text input and uses OPenAI API to generate bullet points.

## Authentication: 
Uses JWT for secure access to the API endpoints for token-based authentication for the API endpoints, ensuring that only authenticated users can access the endpoints.

## Database Storage: 
Additionally, it saves the original text and the generated summary or bullet points in a SQLite database.
## Testing
Unit tests have also been implemented for the API endpoints ensuring that the API handles different edge cases gracefully.

## Requirements
Python 3.8+

Django 4.2+

Django REST Framework

OpenAI Python Client

python-dotenv

## Installation
Clone the repository

```
git clone https://github.com/yourusername/summary-generator.git
cd summary-generator
```

Create a virtual environment

```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Install dependencies

```
pip install -r requirements.txt
Set up environment variables
```

Create a .env file in the root directory and add your OpenAI API key:

```
OPENAI_API_KEY=your_openai_api_key_here
```
Run migrations

```
python manage.py migrate
```

Run the server

```
python manage.py runserver
```
API Endpoints
Authentication
Obtain JWT Token: POST /token/

Request Body:

```
{
  "username": "your_username",
  "password": "your_password"
}
```
Response:

```
{
  "refresh": "your_refresh_token",
  "access": "your_access_token"
}
```
Refresh JWT Token: POST /token/refresh/

Request Body:

```
{
  "refresh": "your_refresh_token"
}
```
Response:

```
{
  "access": "your_new_access_token"
}
```

Text Processing
Generate Summary: POST /generate-summary/

Request Body:

```
{
  "text": "Your long text here..."
}
```
Response:

```
{
  "id": 1,
  "original_text": "Your long text here...",
  "summary": "Generated summary...",
  "bullet_points": null,
  "created_at": "2023-10-01T12:34:56Z"
}
```
Generate Bullet Points: POST /generate-bullet-points/

Request Body:

```
{
  "text": "Your long text here..."
}
```
Response:

```
{
  "id": 2,
  "original_text": "Your long text here...",
  "summary": null,
  "bullet_points": "• Point 1\n• Point 2\n• Point 3",
  "created_at": "2023-10-01T12:34:56Z"
}
```
## Models
TextData
### original_text: 
The original text provided by the user.

### summary: 
The generated summary of the text.

### bullet_points: 
The generated bullet points of the text.

### created_at: 
The timestamp when the record was created.

## Settings
### DEBUG: 
Set to True for development. Set to False in production.

### ALLOWED_HOSTS: 
List of allowed hosts. Update this for production.

### OPENAI_API_KEY: Your OpenAI API key, loaded from the .env file.

### SECRET_KEY: Django secret key. Keep this secure in production.
