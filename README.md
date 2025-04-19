# ServiceBuddy - Django Rest Framework Backend

ServiceBuddy is a Django Rest Framework (DRF) based backend that provides APIs for managing various services.

## Installation Guide

### Prerequisites
Ensure you have the following installed:
- Python (>= 3.8)
- pip
- virtualenv (optional but recommended)

### Steps to Install and Run the Project

1. **Clone the Repository:**
   ```sh
   git clone <repository-url>
   cd serviceBuddy
   ```

2. **Create and Activate Virtual Environment (Optional but Recommended):**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```sh
   pip install -r req.txt
   ```

4. **Apply Migrations:**
   ```sh
   python manage.py migrate
   ```

5. **Run the Development Server:**
   ```sh
   python manage.py runserver
   ```

Now, the backend is running and accessible at `http://127.0.0.1:8000/`.

## API Documentation (Swagger)

You can access the API documentation using Swagger by visiting:
   ```sh
   http://127.0.0.1:8000/swagger/
   ```

## Adding Data from Admin Panel Using Excel File

1. **Access the Admin Panel:**
   - Open `http://127.0.0.1:8000/admin/`
   - Login with:
     - **Username:** admin
     - **Password:** 1234

2. **Upload Excel File:**
   - Go to the relevant model section.
   - Use the "Import" option to upload an Excel file.
   - Make sure the file format matches the required fields.

### Attached Sample Excel File
A sample Excel file (`sample_data.xlsx`) is provided to help you format the data correctly before uploading.

---

Now your ServiceBuddy backend is set up and ready to use!

