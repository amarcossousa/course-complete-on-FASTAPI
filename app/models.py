from database import Base
from sqlalchemy import Column, Integer, String, Boolean

class Posts(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, nullabel=False)
    title = Column(String, nullabel=False)
    content = Column(String, nullabel=False)
    published = Column(Boolean, default=True)