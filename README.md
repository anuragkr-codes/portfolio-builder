# Portfolio Generator

A Django web application that allows users to create professional portfolios by selecting templates and customizing them with personal information, projects, skills, experiences, and education.

## Features

- Select from multiple portfolio templates with preview images
- Create personalized portfolios with customizable sections:
  - Personal information and contact details
  - Projects showcase with descriptions and links
  - Skills categorized by type and proficiency
  - Work experience timeline
  - Educational background
- Unique URL generation for each portfolio
- Mobile-responsive design

## Prerequisites

- Python 3.10+
- pip (Python package manager)
- Virtual environment (recommended)

## Installation

1. Clone the repository

   ```bash
   git clone https://github.com/yourusername/portfolio-generator.git
   cd portfolio-generator
   ```

2. Create and activate a virtual environment (recommended)

   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations

   ```bash
   python manage.py migrate
   ```

5. Create a superuser (for admin access)

   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server

   ```bash
   python manage.py runserver
   ```

7. Access the application at http://127.0.0.1:8000/

## Usage

1. Visit the homepage and browse available templates
2. Select a template you like
3. Fill in your personal information, projects, skills, experience, and education
4. Submit the form to generate your portfolio
5. Use the provided unique URL to view and share your portfolio

## Admin Access

1. Navigate to http://127.0.0.1:8000/admin/
2. Login with your superuser credentials
3. Manage templates, portfolios, and other data

## Running Template Creation Command

This project includes a management command to create default templates:

```bash
python manage.py create_templates
```

## Technologies Used

- Django 5.2 - Web framework
- Pillow 11.2.1 - Image processing library
- SQLite - Database (default)
- HTML/CSS - Frontend
- JavaScript - Interactive elements

## Project Structure

- `generator/` - Main application with models, views, and templates
- `media/` - User uploaded content like project images and template previews
- `static/` - Static files (CSS, JavaScript, images)
- `portfolio_generator/` - Project settings and configuration

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
