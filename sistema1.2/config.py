
DB_CONFIG = {
    'database': 'my_database.db'  
}

SECRET_KEY = "my_super_secret_key"
DEBUG = True


DATABASE_URL = "sqlite:///my_database.db"

if DEBUG:
    print("Modo de depuración activado.")
    print(f"Conectando a la base de datos: {DATABASE_URL}")