# Django Project Real Estate Website

A Django project for building a real estate website that allows users to browse, buy, and rent properties. This platform enables property listings, search filters, and property detail pages, along with user authentication for listing properties.

## Features

- **Property Listings**: View properties available for rent or sale.
- **Property Search**: Filter properties based on price, location, and type.
- **User Registration and Login**: Allows users to create an account, log in, and manage their properties.
- **Admin Panel**: Admin can manage users, properties, and listings.
- **Interactive Maps**: View properties on an interactive map with location pins.
- **Property Detail Pages**: Each property has a detail page with images, description, and contact information.

## Requirements

- **Python 3.x**
- **Django**: A high-level Python web framework.
- **PostgreSQL** (or other database systems): The database to store property listings and user data.
- **Django Allauth**: For handling user authentication and registration.
- **Django Crispy Forms**: For better form styling.
- **Leaflet.js** (optional): For displaying interactive maps (with markers for properties).
- **Django REST Framework** (optional): For API integration (if needed).

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/shahramsamar/Django_Project_Real_Estate_website.git
    cd Django_Project_Real_Estate_website
    ```

2. **Install Dependencies:**

    If you're using `pip`, run:

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up the Database**:

    Modify the `settings.py` file to configure the database connection. By default, Django uses SQLite, but you can switch to PostgreSQL or any other database by modifying the database settings.

    Example configuration for PostgreSQL:
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'real_estate_db',
            'USER': 'your_db_user',
            'PASSWORD': 'your_db_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

4. **Apply Migrations**:

    Run the following command to apply database migrations:

    ```bash
    python manage.py migrate
    ```

5. **Create a Superuser (Admin)**:

    To create an admin user for accessing the Django admin dashboard, run:

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the Development Server**:

    To start the server, use the following command:

    ```bash
    python manage.py runserver
    ```

    The website will be available at `http://127.0.0.1:8000/`.

### How to Use

1. **User Registration**:
   - Navigate to the registration page and create a new user account with a valid email and password.

2. **Login**:
   - After registration, log in to your account to access the dashboard and listing features.

3. **Browse Properties**:
   - Browse available properties, filtering by type, price, and location.

4. **Add a Listing**:
   - If you are a logged-in user, you can list your own properties for rent or sale.

5. **View Property Details**:
   - Click on a property to view more details, including images, description, price, and contact information.

6. **Admin Panel**:
   - Access the Django admin panel at `http://127.0.0.1:8000/admin/` to manage properties, users, and listings.

### Project Structure

- `real_estate/`: Main project folder.
    - `settings.py`: Django settings file.
    - `urls.py`: URL routing for the project.
    - `wsgi.py`: WSGI configuration for deployment.
    - `asgi.py`: ASGI configuration for deployment.
- `properties/`: Application handling property listings and user accounts.
    - `models.py`: Contains models for properties and users.
    - `views.py`: Contains views for displaying properties and handling searches.
    - `forms.py`: Contains forms for user registration and property listing.
    - `urls.py`: Routing for the properties application.
    - `templates/`: HTML files for rendering property listings and user views.
        - `property_list.html`: Displays a list of properties.
        - `property_detail.html`: Displays details of a single property.
        - `index.html`: The homepage of the real estate website.
    - `static/`: CSS, JavaScript, and image files.
        - `css/`: Stylesheets for the website.
        - `images/`: Image resources for the website.
- `templates/`: Global templates for the website (e.g., header, footer).
- `requirements.txt`: Lists necessary Python libraries for the project.

### Contributing

Feel free to fork the project and submit pull requests for new features, improvements, or bug fixes.

### License

This project is open-source and available for educational purposes.

### API Documentation

For developers looking to expose property listings or other data via an API, Django REST Framework can be integrated to expose endpoints for properties, users, and listings.

For example, you can set up these API endpoints:
- **GET /api/properties/** - List available properties.
- **POST /api/properties/** - Add a new property listing (for logged-in users).
- **GET /api/properties/{id}/** - Get details of a specific property.

---

This `README.md` provides detailed installation, usage, and project structure instructions for the Real Estate website built with Django. It highlights the main features such as property listings, user authentication, and the admin panel while explaining how to set up the project, database, and server.

