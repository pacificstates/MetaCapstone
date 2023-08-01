The Menu and Booking API's are Token Authenticated, so:

First you will need to create a user at:
http://127.0.0.1:8000/auth/users/

Then, make a post request to the following endpoint using insomnia:
http://127.0.0.1:8000/restaurant/api-token-auth/

This will provide you with a Token.

You will then be able to make GET requests to:

http://127.0.0.1:8000/restaurant/menu --> for a list of menu items

http://127.0.0.1:8000/restaurant/booking/tables --> for a list of booked tables

Static HTML content can be found at:

http://127.0.0.1:8000/restaurant/

The unit tests are located in the app folder (restauarnt) within test_models.py