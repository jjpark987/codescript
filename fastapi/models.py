from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base = declarative_base()

# Extend the FastAPI Users table
class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "users"
    
    username = Column(String, nullable=True)
    last_name = Column(String, nullable=True)

# Category Model
class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    description = Column(Text)

    subcategories = relationship('Subcategory', back_populates='category')
    problems = relationship('Problem', back_populates='category')

# Subcategory Model
class Subcategory(Base):
    __tablename__ = 'subcategories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    description = Column(Text)
    category_id = Column(Integer, ForeignKey('categories.id', ondelete='CASCADE'))

    category = relationship('Category', back_populates='subcategories')
    problems = relationship('Problem', back_populates='subcategory')

# Problem Model
class Problem(Base):
    __tablename__ = 'problems'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    constraints = Column(Text)
    difficulty = Column(Integer, nullable=False)  # 1: Easy, 2: Medium, 3: Hard
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    category_id = Column(Integer, ForeignKey('categories.id', ondelete='SET NULL'), nullable=True)
    subcategory_id = Column(Integer, ForeignKey('subcategories.id', ondelete='SET NULL'), nullable=True)

    category = relationship('Category', back_populates='problems')
    subcategory = relationship('Subcategory', back_populates='problems')
    examples = relationship('Example', back_populates='problem')
    submissions = relationship('Submission', back_populates='problem')

# Example Model
class Example(Base):
    __tablename__ = 'examples'

    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text, nullable=False)
    image_url = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    problem_id = Column(Integer, ForeignKey('problems.id', ondelete='CASCADE'))

    problem = relationship('Problem', back_populates='examples')

# Submission Model
class Submission(Base):
    __tablename__ = 'submissions'

    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    problem_id = Column(Integer, ForeignKey('problems.id', ondelete='CASCADE'))
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))  # Assuming user management elsewhere

    problem = relationship('Problem', back_populates='submissions')
    user = relationship('User', back_populates='submissions')  # Assuming user model exists