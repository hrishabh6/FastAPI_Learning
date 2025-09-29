
#These imports are for connecting to the database
from sqlalchemy import Column, Integer, String, Boolean
from config.Database import Base, engine

# SQLAlchemy model
class Task(Base):   
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(255), index=True, nullable=False)
    description = Column(String(255), index=True, nullable=False)
    isCompleted = Column(Boolean, default=False)  

Base.metadata.create_all(bind=engine)