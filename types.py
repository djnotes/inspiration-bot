from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    addresses = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
    )
    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r})"

class Inspiration(Base):
    __tablename__ = "inspiration"
    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=True)
    user = relationship("User", back_populates="inspirations")
    def __repr__(self):
        return f"Inspiration(id={self.id!r}, tex={self.text!r})"


# Load credentials
userEnv = open("env/mariadb-user").read()
passwordEnv = open("env/mariadb-password").read()
databaseEnv = open("env/mariadb-database").read()


engine = create_engine(f"mysql+pymysql://{userEnv}:{passwordEnv}@db/{databaseEnv}", echo=True, future=True)