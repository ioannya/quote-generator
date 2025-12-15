from dataclasses import dataclass
from typing import Optional


@dataclass
class Quote:
    id: Optional[int] = None
    text: str = ""
    category: str = ""

    def __str__(self) -> str:
        return f"[{self.category}] {self.text}"
