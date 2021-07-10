from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from src.database import db
from src.models.book import Book
from src.models.version import Version


class Text(db.Base):
    __tablename__ = 'texts'

    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)
    chapter_number = Column(Integer, nullable=False)
    verse_number = Column(Integer, nullable=False)

    book_id = Column(Integer, ForeignKey('books.id'))
    version_id = Column(Integer, ForeignKey('versions.id'))

    book: Book = relationship(Book)
    version: Version = relationship(Version)

    def __init__(
        self, *,
        id: int,
        text: str,
        chapter_number: int,
        verse_number: int,
        book_id: int,
        version_id: int,
    ) -> None:
        self.id = id
        self.text = text
        self.chapter_number = chapter_number
        self.verse_number = verse_number
        self.book_id = book_id
        self.version_id = version_id

    @property
    def reference(self) -> str:
        return f'{self.book.name} {self.chapter_number}:{self.verse_number}'
