# Hotel Listings Website Documentation

## Members  
Project was completed by
|name|Reg number|
|---|---|
|Mark Victor Kithinji||
|Samuel Gicheha||

## Project Overview
This documentation provides a comprehensive guide to the hotel listings website project. The website aims to list major hotels, making it easier for users to find their next vacation destination.

### Distinctiveness and Complexity
The uniqueness of this project lies in its utilization of Django, a high-level Python web framework, for efficient web development. The complexities involved include managing data retrieval from the database upon page load and manipulating this data dynamically to present various hotel listings without redundant database queries.

### Design Approach
The project adopts the Model-View-Template (MVT) architecture, a variation of the Model-View-Controller (MVC) pattern. This choice aligns with Django's framework, facilitating modular development, code organization, and scalability. Django's robust built-in features, such as its ORM (Object-Relational Mapping) system, authentication, and routing mechanisms, further enhance development efficiency and maintainability.

### File Contents

#### views.py
This file contains the view functions responsible for processing HTTP requests and returning appropriate responses. Views interact with models to retrieve data, perform logic, and render templates.

#### urls.py
The URL configuration file maps URLs to view functions, facilitating navigation within the website. It defines the URL patterns and corresponding view functions to handle incoming requests.

#### models.py
Models.py defines the data models used in the application. These models represent entities such as hotels, users, and reservations, defining their attributes and relationships. Django's ORM simplifies database interactions by abstracting SQL queries into Python objects.

#### Templates
- **home.html**: The homepage template serves as the backbone of the site, providing the layout and structure using HTML and CSS. It loads data dynamically upon page load.
- **card_component.html**: This template contains a card component used to display summarized hotel information dynamically. It is utilized for concise previews of hotel listings.
- **listing_component.html**: The listing component offers a more detailed view of hotel information, accommodating comprehensive details for each hotel dynamically.
- **nav.html**: The navigation bar template ensures consistent navigation across the website, containing links and navigation elements.
- **star.html**: This template includes a component for displaying star ratings dynamically, enhancing the presentation of hotel ratings.

#### Static Files
- **beach_resort_listing/funct.js**: This JavaScript file contains client-side logic, enhancing the interactivity and functionality of the website.

### How to Run the Application
To run the application:
1. Ensure Python and Django are installed on your system.
2. Clone the project repository from [GitHub](https://github.com/example/project).
3. Navigate to the project directory in your terminal.
4. Run the following command to start the Django development server:
   ```
   python manage.py runserver
   ```
5. Access the website through your preferred web browser at `http://localhost:8000`.

### Additional Information
- The project leverages Django's built-in admin interface for convenient management of hotel listings and user data.
- Authentication and authorization mechanisms can be implemented to secure user access and data integrity.
- Continuous integration and deployment (CI/CD) pipelines can be set up to automate testing and deployment processes for smoother development workflows.