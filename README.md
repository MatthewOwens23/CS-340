# CS 340 Project Two

<img width="2558" height="1303" alt="Screenshot 2026-08-12 121000" src="https://github.com/user-attachments/assets/eaa682bf-b8c6-4c06-bed7-8d925334b60c" />

## Project Overview

This project is a Python-based interactive dashboard created for Grazioso Salvare. The purpose of the dashboard is to make it easier to identify animals that meet specific rescue criteria and view their information in one place.
The dashboard connects to a MongoDB database through a Python CRUD module. Users can select different rescue types, and the dashboard updates the data table, breed chart, and map based on the selected criteria.


## Project Artifacts

- Project Two dashboard
- CRUD Python module
- Project Two README

## Module Eight Journal Reflection

### Maintainable, Readable, and Adaptable Programs

I write programs that are maintainable, readable, and adaptable by organizing code into smaller sections that each have a specific purpose. In Project One, I created a CRUD Python module that handled the database operations for the animal records. I was then able to reuse that module in Project Two when connecting the database to the dashboard. This approach made the code easier to understand because the database operations were separated from the dashboard code instead of having all of the functionality placed in one program.

One advantage of working this way was that I could make changes to the database functionality without having to completely rewrite the dashboard. The CRUD module could also be reused in future applications that need to create, read, update, or delete records from a MongoDB database. For example, the same basic structure could be adapted for another organization's database while changing the collection and fields being used.

### Approaching Problems as a Computer Scientist

I approach problems as a computer scientist by first breaking a larger problem into smaller requirements that can be tested and solved individually. For the Grazioso Salvare project, I first needed to understand what information the organization needed from its animal database. I then worked with the MongoDB database and CRUD functionality before connecting the database to the dashboard widgets. This allowed me to work through the database requirements separately from the user interface requirements.

This approach was different from some of my previous assignments because the project required me to think about how multiple parts of an application work together rather than focusing on only one program or concept. I had to consider the database structure, Python code, queries, and dashboard functionality as parts of the same system. In the future, I would use a similar process by first gathering the client's requirements, identifying the data that needs to be stored and retrieved, designing the database structure, developing reusable functions, and then testing the system to make sure it meets the client's needs.

### What Computer Scientists Do and Why It Matters

Computer scientists use technology and problem-solving skills to develop solutions that help organizations work more effectively. In the Grazioso Salvare project, my work with MongoDB, Python, and the dashboard provided a way for the organization to interact with its animal data more efficiently. Instead of requiring users to manually search through database records, the dashboard provides a more accessible way to view and analyze the information.

This type of project can help a company like Grazioso Salvare save time and make better use of its data. The database stores the information, the CRUD module provides a way to interact with that data, and the dashboard gives users a visual way to access the results. Together, these components demonstrate how computer science can turn an organization's data and requirements into a practical tool that supports its daily work and decision-making.
