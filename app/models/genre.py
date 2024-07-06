from app import db

class Genre(db.Model):
    __tablename__ = 'genres'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    books = relationship("BookGenre", back_populates="genre")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'books': [book.to_dict() for book in self.books]
        }

    @classmethod
    def from_dict(cls, genre_dict):
        if not name:
            raise ValueError("Name is required.")
        
        return cls(
            name=name
        )