
## ⚙️ Installation

bash
git clone https://github.com/yourusername/drf-shop-api.git
cd drf-shop-api
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt



---

## ▶️ Run Migrations

bash
python manage.py migrate
python manage.py createsuperuser


---

## 🏃 Run Server

bash
python manage.py runserver


---

## 🔐 Authentication (JWT)

1. Get Token

   http
   POST /api/token/
   {
     "username": "youruser",
     "password": "yourpassword"
   }
   

   Response:

   json
   {
     "access": "eyJ0eXAiOiJKV1QiLCJhbGci...",
     "refresh": "eyJ0eXAiOiJKV1QiLCJhbGci..."
   }
   

2. Use Token in Swagger

   * Click *Authorize* in Swagger UI
   * Enter:

     
     Bearer your_access_token
     

---

## 📖 API Endpoints

### 🔹 Categories

* GET /api/categories/ → List categories
* POST /api/categories/ → Create category

### 🔹 Products

* GET /api/products/ → List products
* POST /api/products/ → Create product
* GET /api/products/export/csv/ → Export products to CSV
* GET /api/products/export/excel/ → Export products to Excel
* POST /api/products/bulk/?count=5 → Create bulk products with threads

---

## 🔒 Response Encryption (Optional)

You can enable *encrypted responses* for specific views by overriding list() / create() methods:

Example (Base64):

python
def list(self, request, *args, **kwargs):
    response = super().list(request, *args, **kwargs)
    encrypted = base64.b64encode(json.dumps(response.data).encode()).decode()
    return Response({"data": encrypted})


---

## 📚 API Docs (Swagger)

* Swagger UI: http://127.0.0.1:8000/swagger/
* ReDoc: http://127.0.0.1:8000/redoc/

---

## 🛠️ Tech Stack

* Python 3.10+
* Django 4+
* Django REST Framework
* SimpleJWT
* drf-yasg (or drf-spectacular)

---

## 👨‍💻 Development Notes

* All APIs require JWT authentication.
* Superuser can access Django admin at /admin/.
* Response encryption is optional and can be enabled per view.

---
