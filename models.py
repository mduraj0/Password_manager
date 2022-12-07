from sqlalchemy import create_engine, Integer, String, Column, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, backref

Base = declarative_base()
engine = create_engine('sqlite:///database.db', future=True)


class Portal(Base):
    __tablename__ = 'portals'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))


class Credentials(Base):
    __tablename__ = 'credentials'
    login = Column(String(30), primary_key=True)
    password = Column(String(30))
    portal_id = Column(Integer, ForeignKey('portals.id'))
    portal = relationship('Portal', backref=backref('credentials', uselist=False))
