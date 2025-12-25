from dataclasses import dataclass
from typing import Optional


@dataclass
class QuoteEntity:
    id: Optional[int] = None
    text: str = ""
    category: str = ""
