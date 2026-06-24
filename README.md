# 🚀 FastAPI CRUD API

A backend-focused CRUD application built with **FastAPI**, **PostgreSQL**, and **SQLAlchemy**. The project exposes RESTful APIs for managing products and demonstrates database integration, API development, image handling, and CRUD operations.

A simple React frontend is included to interact with the APIs and visualize the data.

---

# ✨ Features

✅ RESTful API Development

✅ Create Products

✅ Retrieve Products

✅ Update Products

✅ Delete Products

✅ Upload & Retrieve Product Images

✅ PostgreSQL Database Integration

✅ SQLAlchemy ORM

✅ Environment Variable Configuration

✅ Interactive API Documentation (Swagger UI)

---

# 🛠️ Tech Stack

## Backend

* Python
* FastAPI
* SQLAlchemy
* PostgreSQL
* Pydantic
* Uvicorn
* python-dotenv

## Frontend

* React (Used as a client interface)

---

# 📁 Project Structure

```text
FASTAPI-PROJECT/
│
├── frontend/
│
├── database.py
├── database_models.py
├── main.py
├── models.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
│
└── screenshots/
```

---

# ⚙️ Installation & Setup

## 1. Clone the Repository

```bash
git clone https://github.com/PiyushGhadle/fastapi-postgresql-crud.git

cd fastapi-project
```

---

## 2. Create Virtual Environment

```bash
python -m venv myenv
```

### Windows

```bash
myenv\Scripts\activate
```

### Linux / macOS

```bash
source myenv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file.

```
DATABASE_URL=postgresql://username:password@localhost:5432/ecommerce_db
```

---

## 5. Run the Application

```bash
uvicorn main:app --reload
```

Backend runs on:

```
http://localhost:8000
```

Interactive API Documentation:

```
http://localhost:8000/docs
```

---

# 📡 API Endpoints

| Method | Endpoint              | Description                |
| ------ | --------------------- | -------------------------- |
| GET    | `/products`           | Retrieve all products      |
| GET    | `/product/{id}`       | Retrieve product by ID     |
| POST   | `/product`            | Create a new product       |
| PUT    | `/product/{id}`       | Update an existing product |
| DELETE | `/product/{id}`       | Delete a product           |
| GET    | `/product/{id}/image` | Retrieve product image     |

---

# 🗄️ Database

* PostgreSQL
* SQLAlchemy ORM
* Session Management
* Environment-based Database Configuration

---

# 📸 Screenshots

## 🏠 Home Page

![Home Page](screenshots/home.png)

## ➕ Add Product

![Add Product](screenshots/create.png)

## ✏️ Update Product

![Update Product](screenshots/update.png)

## 📦 Product Details

![Product Details](screenshots/product-details.png)

---

# 🚀 Future Improvements

* JWT Authentication & Authorization
* Pagination
* Search & Filtering
* Docker Support
* Unit Testing
* CI/CD Pipeline
* Cloud Deployment

---

# 👨‍💻 Author

**Piyush Ghadle**

Python Developer | FastAPI | PostgreSQL | Backend Enthusiast

GitHub: https://github.com/PiyushGhadle

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
