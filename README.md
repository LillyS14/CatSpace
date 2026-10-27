# CatSpace App

The foundation of an app for finding an experience with saved cats where customers are also able to
share their memories of this dream space with others. Besides having a great time they can adopt a new friend.

## Environment variables & credentials

No environment variables are required.
The project runs locally with the settings in `catspace/settings.py` (development `SECRET_KEY`, `DEBUG = True`, SQLite).

The database (`db.sqlite3`) and uploaded images (`media/`) are included, so the site starts with demo data.

## How to install and run

1. Clone the repo
2. Virtual environment: python -m venv .venv
3. Activate the environment: .venv\Scripts\activate on Windows, source .venv/bin/activate on macOS/Linux.
4. Install dependencies: pip install -r requirements.txt
5. Run: python manage.py runserver, (use the default port 8000, since the demo images are linked to it).
6. Open http://127.0.0.1:8000/
7. Admin login (optional): admin / CatSpace2026!
8. To preview the custom 404 page, set `DEBUG = False` in catspace/settings.py and run
   `python manage.py runserver --insecure`. Set it back to True afterwards.

## Apps

1. cats - used for managing CRUD operations with cats. CUD will be restricted to authorized users.
2. experiences - used for managing CRUD operations with experiences. CUD will be restricted to authorized users.
3. memories - used for managing CRUD operations with memories. CUD will be restricted to authors of the post and admin.
4. teammates - used for managing CRUD operations with teammates. CUD will be restricted to authorized users.

## Features
CBV, models, forms, validations, template tags, filters, search functionality, pagination, etc.

## Extra Features

Phone Number Validation: Implemented international phone number validation using `django-phonenumber-field` to ensure
that the submitted phone numbers follow valid numbering formats and are stored consistently.

Google Maps Integration: Embedded Google Maps using an iframe to display the location and help customers find the
address
easily.

## Disclaimer

There are no users and login/authentication logic. 2 of the images and part of the CSS are generated with AI help.

## Credits

Special thanks to _Mena_ and _Georgi_ for the encouragement and support.
