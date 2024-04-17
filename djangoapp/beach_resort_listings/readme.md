# Hotel Listings Website Documentation

## Members  
Project was completed by
|name|Reg number|
|---|---|
|Mark Victor Kithinji|SCT212-0105/2022|
|Samuel Gicheha|SCT212-0118/2022|  

## Project Overview
This documentation provides a comprehensive guide to the hotel listings website project. The website aims to list major hotels, making it easier for users to find their next vacation destination.

### Distinctiveness and Complexity
**Distinctiveness**  - The project's uniqueness stems from its emphasis on user interface (UI) design, prioritizing intuitive navigation and user experience. This focus on UI design sets it apart by ensuring that users can effortlessly navigate the website and access the desired information about hotels.   

**Complexity**   - The project's complexity is amplified by the strategic optimization of data retrieval from the database. By fetching necessary data upon page load and strategically manipulating it, the website minimizes redundant database queries, enhancing performance and user responsiveness. 
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
2. Clone the project repository from [GitHub](https://github.com/VictorCodebase/IAP-2.2/tree/main/djangoapp/beach_resort_listings.git).
3. Navigate to the project directory in your terminal.
4. Run the following command to start the Django development server:
   ```
   python manage.py runserver
   ```
5. Access the website through your preferred web browser at `http://localhost:8000`.

### Additional Information
- The project leverages Django's built-in admin interface for convenient management of hotel listings and user data.


## Project screenshots  

### Desktop view 
|Home Page| Hotel Clicked|
|---|---|
|![image](https://github.com/VictorCodebase/IAP-2.2/assets/135356007/1facb5ff-8255-4fa8-a3e2-1a5b9303b106)|![image](https://github.com/VictorCodebase/IAP-2.2/assets/135356007/6fecddb9-dffc-41b7-8d05-cef07694c5cb)|
|---|---|

|Searching for Hotel|
|---|
|![image](https://github.com/VictorCodebase/IAP-2.2/assets/135356007/1c6f8dd6-b552-4dc9-8fe0-def65a152ba6)|
|---|

### Mobile View
Home page:  
|Home page| Hotel Clicked| Searching for Hotel|
|---|---|---|
|![WhatsApp Image 2024-04-17 at 10 01 19_b322775b](https://github.com/VictorCodebase/IAP-2.2/assets/135356007/39e17710-a636-46cf-8e35-da02414c447e)| ![WhatsApp Image 2024-04-17 at 10 04 46_9459014c](https://github.com/VictorCodebase/IAP-2.2/assets/135356007/1bf5147f-4b1a-450a-aa84-092a7eb3cc16) | ![WhatsApp Image 2024-04-17 at 10 06 24_4525dbcf](https://github.com/VictorCodebase/IAP-2.2/assets/135356007/15213ec2-ce39-4207-ab81-1c63f60539b3) |


Project completed and compiled for Internet Application Programming class project. March 2024



