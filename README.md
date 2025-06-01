# Mars Weather Data System Overview
The Mars Weather Data System is a web-based application designed to collect, store, and present a variety of Mars-related data from multiple authoritative sources. This document provides a comprehensive overview of the system's architecture, components, and data flow.
## Purpose and Scope
The Mars Weather Data System serves the following purposes:
- Automate collection of Mars data from various NASA and space-related websites
- Consolidate diverse Mars information (news, images, weather, facts) into a single database
- Present this information through an interactive web interface
- Allow users to refresh the data on demand
The system collects several types of Mars data:
- Latest Mars news from NASA
- Featured Mars images from JPL
- Mars weather updates from Twitter
- Detailed hemisphere images from USGS
- Mars planetary facts from Space Facts

## System Architecture
The Mars Weather Data System follows a three-tier architecture consisting of data acquisition, storage, and presentation layers.
### Architecture Diagram
<img width="1147" alt="Screenshot 2025-06-01 at 4 13 48 PM" src="https://github.com/user-attachments/assets/a347ddc8-d782-4a9c-8132-5b8d9270bdef" />

## Key Components
### Web Application
The web application is built using Flask and serves as the interface between users and the system. It handles HTTP requests and responses, manages the database connection, and triggers the data scraping process.

Key features:

- Home route (/) that displays Mars data
- Scrape route (/scrape) that refreshes the data
- MongoDB integration for data persistence

### Scraping Module
The scraping module (scrape_mars.py) is responsible for collecting Mars data from various web sources. It uses Splinter for browser automation and BeautifulSoup for HTML parsing.

Key components:

- init_browser(): Initializes a Chrome browser instance
- scrape_info(): The main function that coordinates all scraping activities

### Data Storage
The system uses MongoDB, a NoSQL database, to store the scraped Mars data. The data is stored as a document in a collection, making it easy to update and retrieve.

## Data Flow
The following diagram illustrates the data flow within the system:
<img width="1361" alt="Screenshot 2025-06-01 at 4 17 34 PM" src="https://github.com/user-attachments/assets/decdb469-2daf-4cb3-8bb3-6414a74a2ff9" />

## Code Organization
The codebase is organized into three main files:
<img width="721" alt="Screenshot 2025-06-01 at 4 18 40 PM" src="https://github.com/user-attachments/assets/e9a80482-2672-48cc-a20c-64f547af8238" />

<img width="739" alt="Screenshot 2025-06-01 at 4 19 54 PM" src="https://github.com/user-attachments/assets/708c4f5a-638c-49ac-84dc-9c704c8a9408" />

### Development Components and Dependencies
<img width="1129" alt="Screenshot 2025-06-01 at 4 20 58 PM" src="https://github.com/user-attachments/assets/4fd86c22-6146-464e-8fea-90f4d2b1a2a6" />

## Summary
The Mars Weather Data System is a comprehensive web application that collects, stores, and displays various types of Mars data. The system's modular architecture separates concerns between data acquisition, storage, and presentation, making it easy to maintain and extend. Users can access the latest Mars information through a simple web interface and refresh the data on demand.

The system demonstrates the use of web scraping techniques to extract data from multiple sources and consolidate it into a single, user-friendly application.
