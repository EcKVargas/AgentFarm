"""Normalize text into hyphen-separated slugs."""


def slugify(text: str) -> str:
    """Lowercase text and collapse runs of non-alphanumeric characters."""
    result = []
    separator_pending = False
    for character in text.lower().strip():
        if character.isalnum():
            if separator_pending and result:
                result.append("-")
            result.append(character)
            separator_pending = False
        else:
            separator_pending = True
    return "".join(result)
