from typing import Any, Dict, List

from sqlalchemy.sql.expression import func, or_
from src.database import db
from src.models import Book, Text, Version
from src.models.version import Version
from src.utils.query_filter import QueryFilter, query_filter_to_sql_filter_list

query_filter: QueryFilter = {
    'version': lambda q: Version.version == q if q else True,
    'book': lambda q: or_(
        func.lower(Book.name) == func.lower(q),
        func.lower(Book._name) == func.lower(q),
        func.lower(Book._initials) == func.lower(q),
    ),
    'chapter': lambda q: Text.chapter_number == q,
    'verse': lambda q: Text.verse_number == q,
    'q': lambda q: Text.text.like(f'%{q}%'),
}


class TextDAO:
    def search(self, filter_dict: Dict[str, Any]) -> List[Text]:
        text_filter = query_filter_to_sql_filter_list(
            query_filter, filter_dict)
        texts = db.session.query(Text)\
            .join(Version)\
            .join(Book)\
            .filter(*text_filter).all()
        return texts
