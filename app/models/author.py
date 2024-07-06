from app import db

class Author(db.Model):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    books = relationship("Book", back_populates="author")   

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'books': [book.to_dict() for book in self.books]
        }   

    @classmethod
    def from_dict(cls, author_dict):
        if not name:
            raise ValueError("Name is required.")
        
        return cls(
            name=name
        )   

