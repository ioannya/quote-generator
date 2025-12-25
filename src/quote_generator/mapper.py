from .entities import QuoteEntity
from .models import Quote


def entity_to_domain(entity: QuoteEntity) -> Quote:
    return Quote(id=entity.id, text=entity.text, category=entity.category)


def domain_to_entity(model: Quote) -> QuoteEntity:
    return QuoteEntity(id=model.id, text=model.text, category=model.category)
