from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


url_database = 'mysql+pymysql://root:kanyisola892@localhost:3306/tiktak' 

engine = create_engine(url_database)

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()









