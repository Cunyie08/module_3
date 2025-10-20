from sqlalchemy import create_engine
from sqlalchemy.orm import Sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

db_url = dialect+driver://dbuser;dbpassword;dbhost;dbport;dbname
db_url =f"mysql+pymysql://{os.getenv("dbuser")};{os.getenv("")}"