🌐 Overview
AETHER is a high-performance, modular web browser designed for the 2026 digital ecosystem. 
It features a unique Hybrid Sync Architecture, combining the speed of local SQLite caching with the robustness of MariaDB cloud synchronization. Unlike traditional browsers, 
Nexus focuses on deep visual customization and a clean, decoupled code structure based on Clean Code principles.

🚀 Key Features
1. Hybrid Cloud Synchronization
Real-time Sync: Seamlessly upload history and bookmarks to a MariaDB server.
Local Persistence: Even without an internet connection, your browsing data is cached using a local SQLite database.
Account-Based Access: Separate Login and Registration modules allow multiple users to sync their data to individual profiles.
2. Advanced Appearance Engine (6 Presets)
AETHER ships with six professionally tuned visual themes, accessible via the Settings Dashboard:
Standard Dark: Optimized for low-light productivity.
Arctic White: High-contrast, clean professional look.
Gold Horizon: Premium aesthetics with deep amber accents.
Matrix Legacy: Classic hacker-style green on black.
Sakura Pink: Soft, elegant pastel tones.
Midnight Blue: Calming navy shades for extended browsing sessions.
3. Smart Navigation UI
Unified Search/URL Bar: Automatically detects if the input is a direct URL or a search query (integrated with Google).
Tab Management: Fully closable, document-mode tabs with dynamic favicon/title updates.
Quick Actions: Dedicated buttons for Bookmarking, Settings, Refresh, and History navigation.

🏗 System Architecture
The project follows a Modular Design Pattern to ensure scalability and ease of maintenance:
main.py: The central controller. Orchestrates the UI life cycle and tab management.
database.py: The data layer. Handles SQL query generation and thread-safe connections.
ui_elements.py: The management UI. Contains profile logic and data visualization.
styles.py: The design system. Stores QSS (Qt Style Sheets) for the theme engine.
utils.py: The logic layer. Handles URL parsing and local configuration I/O.

🛠 Installation & Setup
Prerequisites
Python 3.12+
MariaDB/MySQL Server (Running on localhost or a remote server)
1. Database Configuration
Execute the following SQL commands to prepare your cloud environment:
sql
CREATE DATABASE nexus_browser_2026;
USE nexus_browser_2026;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    title VARCHAR(255),
    url TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE bookmarks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    title VARCHAR(255),
    url TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

2. Install Dependencies
pip install PyQt6 PyQt6-WebEngine mysql-connector-python

3. Launching the Browser
python main.py

📖 Usage Guide
Surfing: Enter a query in the top bar. Press Enter to navigate.
Saving Data: To sync bookmarks, open Settings, go to Profile, and Register or Login. Once logged in, click the ⭐ icon on the main bar.
Viewing History: Open Settings, go to the History or Bookmarks tab. Double-click any item to open it instantly in a new tab.
Customizing: Switch to the Appearance tab in Settings to change the theme instantly.
🛡 Security & Best Practices
Decoupled Logic: UI and Business logic are separated to prevent spaghetti code.
Thread Safety: Database connections are handled with try...finally blocks to ensure resources are released.
Input Sanitization: URL parsing logic prevents malformed requests and handles missing protocols (http/https) automatically.
