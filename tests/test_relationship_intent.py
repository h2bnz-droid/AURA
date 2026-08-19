from core.domain.relationship_intent import RelationshipIntent


def test_relationship_intent_values():
    assert RelationshipIntent.CREATE
    assert RelationshipIntent.SHOW
    assert RelationshipIntent.UPDATE
    assert RelationshipIntent.UNKNOWN_INTENT