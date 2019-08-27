from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://user:pass@db:5432/queens_solutions')

Session = sessionmaker(bind=engine)

Base = declarative_base()
