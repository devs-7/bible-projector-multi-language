import re
from contextlib import suppress
from typing import Any, Dict, List

from sqlalchemy.sql.expression import func, or_
from sqlalchemy.util.langhelpers import NoneType
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
    def search(self, search_text: str, version: str = None, limit: int = None) -> List[Text]:
        with suppress(AttributeError):
            regex = r'^(.+)\s+(\d+)[\s|:]+(\d+)$'
            book, chapter_number, verse_number = re.search(
                regex, search_text).groups()
            filter_dict = {
                'book': book,
                'chapter': chapter_number,
                'verse': verse_number
            }
            if version is not None:
                filter_dict['version'] = version
            return self.filter(filter_dict, limit=limit)

        filter_dict = {'q': search_text}
        if version is not None:
            filter_dict['version'] = version
        return self.filter(filter_dict, limit=limit)

    def filter(self, filter_dict: Dict[str, Any], limit: int = None) -> List[Text]:
        text_filter = query_filter_to_sql_filter_list(
            query_filter, filter_dict)
        query = db.session.query(Text)\
            .join(Version)\
            .join(Book)\
            .filter(*text_filter)
        return query.all() if limit is None else query[:limit]
