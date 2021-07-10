from typing import List
from src.models import Text
from src.database import db


class TextDAO:
    def search(self, q: str) -> List[Text]:
        texts = db.session.query(Text).filter(Text.text.like(f'%{q}%')).all()
        return texts
