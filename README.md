# Makers Profile

## Overview

**Makers Profile** is a **Django-based, database-driven portfolio platform** designed to store, organize, and present my academic and technical projects in a structured, scalable, and visually appealing way. This project serves as my **CS50W final project** and is intended to be my long-term personal portfolio, which I plan to submit for university applications in 2026, including MIT, Harvard, Stanford, and Princeton.

Unlike static portfolio websites, Makers Profile is a **dynamic system** where projects, images, descriptions, and navigation are fully managed through the backend. The project emphasizes **maintainable architecture, modular design, and extensibility**, allowing it to grow as my skills and projects evolve.

---

## Distinctiveness and Complexity

### Distinctiveness

Makers Profile stands out from typical CS50W projects in both **purpose** and **design approach**:

- **Purpose-driven:** Unlike many projects that focus on user interaction or specific features, this platform emphasizes **representation, structured content, and long-term usability**. Every project displayed reflects real work I have completed.
- **Design prototyping and layout decision-making:** Determining where images, descriptions, and modular sections (like carousels) should appear required iterative experimentation.
- **Dynamic and data-driven:** Projects are rendered from the database, enabling scalability and future growth without hardcoding layouts.
- **Mobile responsiveness:** The interface adapts seamlessly to desktops, tablets, and mobile devices using **Bootstrap and Flexbox**, ensuring consistent user experience.
- **PDF download feature:** Each project can be exported as a PDF using **WeasyPrint**, which includes the project title, description, images, and other details.

---

### Complexity

The project’s complexity lies primarily in **architecture, template design, and dynamic rendering**, rather than heavy JavaScript. Key sources of complexity include:

- **Flexible Django models:** Supports multiple projects with different layouts, images, and content requirements.
- **Slug-based dynamic routing:** Each project has a unique URL and detail page without duplicating templates.
- **Modular templates:** Uses Django template inheritance and `{% include %}` for reusable components while allowing project-specific customization.
- **Media management:** Proper handling of uploaded images with Django’s `MEDIA_ROOT` and `MEDIA_URL`.
- **PDF generation:** Dynamic HTML templates rendered as PDFs, integrating server-side logic with styling.
- **Scalable architecture:** Designed for maintainability, clarity, and long-term usability.

Although minimal JavaScript is used, this was intentional, prioritizing **server-side rendering, maintainability, and clean architecture**.

---

## File Structure 
- `manage.py` – Django command-line utility

- `makers_portfolio`/ – Project settings and configuration

- `portfolios`/ – Main application
    - `models.py` – Database models for projects
    - `views.py` – View logic for pages
    - `urls.py` – URL routing
    - `templates/` – HTML templates and components
    - `static/` – CSS and assets
- `media/` – Uploaded project images
- `requirements.txt` – Python dependencies
- `README.md` – Project documentation

## How to Run the Application

1. Clone the repository

1. **Clone the repository**
   ```bash
    git clone https://github.com/Gias-uddin-vuiya/capstone.git
    ```

2. Create and activate a virtual environment
    ```bash 
    python -m venv .venv
    source .venv/bin/activate      # Linux/macOS
    .venv\Scripts\activate         # Windows
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run migrations:
    ```bash
    python manage.py migrate
    ```

5. Run migrations:
    ```bash
    python manage.py runserver
    ```
6. Visit http://127.0.0.1:8000/

## Additional Information 
Makers Profile reflects not only my technical skills, but also my ability to plan, iterate, and build systems with long-term goals in mind. This project will continue to evolve as I add new work and refine how my projects are presented academically and professionally.