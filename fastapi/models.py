from datetime import datetime
from sqlalchemy import Integer, String, Text, JSON, DateTime, ForeignKey, CheckConstraint, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Category(Base):
    __tablename__ = 'categories'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(String(255))

    subcategories: Mapped[list['Subcategory']] = relationship('Subcategory', back_populates='category')

    def __str__(self) -> str:
        return self.name

class Subcategory(Base):
    __tablename__ = 'subcategories'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(255))
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey('categories.id'), nullable=True)
    
    category: Mapped['Category'] = relationship('Category', back_populates='subcategories')
    problems: Mapped[list['Problem']] = relationship('Problem', back_populates='subcategory')

    def __str__(self) -> str:
        return self.name

class Problem(Base):
    __tablename__ = 'problems'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    difficulty: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    example: Mapped[dict] = mapped_column(JSON, nullable=False)
    constraints: Mapped[str] = mapped_column(String, nullable=False)
    subcategory_id: Mapped[int] = mapped_column(Integer, ForeignKey('subcategories.id'), nullable=False)

    subcategory: Mapped['Subcategory'] = relationship('Subcategory', back_populates='problems')
    submissions: Mapped[list['Submission']] = relationship('Submission', back_populates='problem')

    __table_args__ = (
        CheckConstraint('difficulty IN (1, 2, 3)', name='check_difficulty'),
    )

    def __str__(self) -> str:
        return self.title

class Submission(Base):
    __tablename__ = 'submissions'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    content: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    user_id: Mapped[int] = mapped_column(Integer, nullable=False)
    problem_id: Mapped[int] = mapped_column(Integer, ForeignKey('problems.id'), nullable=False)
    
    problem: Mapped['Problem'] = relationship('Problem', back_populates='submissions')

    def __str__(self) -> str:
        return f'Submission ID: {self.id}, Problem ID: {self.problem.id}, User ID: {self.user_id}'
