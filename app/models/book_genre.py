from app import db

class BookGenre(db.Model):
    __tablename__ = 'book_genre'
    book_id = Column(Integer, ForeignKey('books.id'), primary_key=True)
    genre_id = Column(Integer, ForeignKey('genres.id'), primary_key=True)
    book = relationship("Book", back_populates="genres")
    genre = relationship("Genre", back_populates="books")

    def to_dict(self):
        return {
            'book_id': self.book_id,
            'genre_id': self.genre_id
        }   

    @classmethod
    def from_dict(cls, book_genre_dict):
        if not book_id or not genre_id:
            raise ValueError("Book ID and genre ID are required.")
        
        return cls(
            book_id=book_id,
            genre_id=genre_id
        )