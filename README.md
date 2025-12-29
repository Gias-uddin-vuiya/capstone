# makers-portfolio

## Overview

**Makers Profile** is a Django-based, database-driven portfolio platform designed to store, organize, and present my academic and technical projects in a structured and extensible way. This project serves as my CS50W final project and is intended to be my long-term personal portfolio, which I plan to use during university applications in 2026, including submissions to institutions such as MIT, Harvard, Stanford, and Princeton.

Unlike static portfolio websites, Makers Profile is built as a dynamic system where projects, images, descriptions, and navigation are managed through the backend. The goal was not simply to display content, but to design a maintainable architecture that can evolve as my skills and projects grow.

## Distinctiveness and Complexity

### Distinctiveness

This project is distinct from typical CS50W projects in both **purpose** and **design approach**. While many projects in the course focus on implementing specific **features** (such as social networks, auctions, or messaging systems), Makers Profile focuses on **representation, structure, and long-term usability.**

The application is intentionally designed as a personal academic artifact rather than a generic web app. Every project displayed on the site represents real work I have completed, and the platform itself is meant to reflect how I think about organizing, presenting, and explaining technical work. This makes the project fundamentally different from other CS50W submissions that prioritize user interaction over structured content modeling.

Another distinguishing aspect is the emphasis on design **prototyping** and **layout decision-making**. A significant challenge was determining how projects should be visually presented: where images should appear, how much explanation should be shown on listing pages versus detail pages, and when components such as carousels or modular sections were appropriate. These decisions required iterative experimentation and are central to the project’s identity.

### Complexity

The complexity of Makers Profile lies primarily in architecture and data-driven rendering, rather than heavy JavaScript usage. This was a deliberate decision aligned with Django’s strengths and the academic nature of the project.

Key sources of complexity include:

- Designing flexible Django models that support multiple projects with different layouts and content needs.

- Implementing slug-based dynamic routing, allowing each project to have a unique detail page without duplicating logic. 

- Building a modular template system using Django’s template inheritance and `{% include %}` patterns to balance reuse and customization.

- Handling project-specific rendering, where different projects may require different structures, images, or styling.

- Properly managing media uploads using Django’s media configuration.

- Making architectural trade-offs to keep the system clean, scalable, and maintainable. 


Although JavaScript is used minimally, this was intentional. The project prioritizes clarity, server-side rendering, and maintainability over unnecessary client-side complexity.

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
2. Create and activate a virtual environment
3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

