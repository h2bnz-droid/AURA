from core.domain.personal_cognitive_model import (
    CognitiveAttribute,
    PersonalCognitiveModel,
)


def test_cognitive_attribute_creation():
    attribute = CognitiveAttribute(
        attribute_name="skill",
        attribute_value="Python",
        category="skill",
        source="user_statement",
        confidence=1.0,
        created_at="2026-08-20T00:00:00",
        updated_at="2026-08-20T00:00:00",
    )

    assert attribute.attribute_name == "skill"
    assert attribute.attribute_value == "Python"
    assert attribute.category == "skill"
    assert attribute.source == "user_statement"
    assert attribute.confidence == 1.0


def test_personal_cognitive_model_creation():
    attribute = CognitiveAttribute(
        attribute_name="interest",
        attribute_value="robotics",
        category="interest",
        source="user_statement",
        confidence=1.0,
        created_at="2026-08-20T00:00:00",
        updated_at="2026-08-20T00:00:00",
    )

    model = PersonalCognitiveModel(
        attributes=[attribute]
    )

    assert len(model.attributes) == 1
    assert model.attributes[0].attribute_value == "robotics"