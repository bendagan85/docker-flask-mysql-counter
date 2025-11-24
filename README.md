# Flask + MySQL Counter System (Dockerized)

This project demonstrates a fully Dockerized multi-container system where a Flask web application interacts with a MySQL database to store and update a persistent counter. The system includes automatic database initialization, a clean containerized backend, and a frontend page that displays a counter that increments on every refresh. This project showcases essential DevOps concepts including containerization, multi-service orchestration, persistent storage, and internal networking between services.

---

##  Features
- Multi-container setup using **Docker Compose**
- **MySQL database** with persistent Docker volume (data survives container deletion)
- Automatic schema/table creation using `init.sql`
- Flask backend that increments a counter stored in MySQL
- Clean, isolated Docker environment
- Fully reproducible setup on any machine with Docker installed

---

##  System Overview
The system includes two services:

1. **Flask App** — A Python/Flask server that increments and displays a counter  
2. **MySQL Database** — Stores the counter value persistently

Both services run inside the same Docker network. The Flask application connects to MySQL using the hostname `db`, provided automatically by Docker Compose’s internal DNS.

---

##  How It Works
1. When the MySQL container starts, it automatically executes `init.sql`, which creates the database and counter table.  
2. When a user loads the Flask app (port **5000**), Flask sends an SQL `UPDATE` to increment the counter and returns the new value.  
3. The counter is stored inside MySQL and persists thanks to the named Docker volume.  
4. Rebuilding or restarting containers will not reset the counter unless the volume is removed.

---

##  Project Structure
```
project/
│── app.py               # Flask application logic
│── templates/index.html # Frontend UI template
│── requirements.txt     # Python dependencies
│── init.sql             # Database initialization script
│── Dockerfile           # Flask image build instructions
└── docker-compose.yml   # Orchestrates Flask + MySQL services
```

---

## ▶️ Running the Project
1. Install **Docker** and **Docker Compose**  
2. Inside the project directory, run:
   ```
   docker-compose up --build
   ```
3. Open your browser at:  
   **http://localhost:5000**

Refreshing the page increments the counter stored inside MySQL.

To stop the system:
```
docker-compose down
```

To also remove the persisted counter:
```
docker-compose down -v
```

---

##  Summary
This project is a strong DevOps portfolio piece demonstrating multi-container orchestration, backend-database communication, persistent volumes, and fully automated environment setup. It reflects real-world patterns used in microservices, backend systems, and cloud-native infrastructure.


