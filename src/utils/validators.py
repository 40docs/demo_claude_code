"""Validation utilities for the Pet Adoption Center.

This module provides reusable validation functions for input data.
"""

from typing import Any, List, Optional


# List of valid dog breeds (AKC recognized breeds + common mixed breed terms)
VALID_DOG_BREEDS: List[str] = [
    # Sporting Group
    "labrador retriever", "golden retriever", "german shorthaired pointer",
    "brittany", "cocker spaniel", "english springer spaniel", "vizsla",
    "weimaraner", "irish setter", "english setter", "pointer",
    # Hound Group
    "beagle", "dachshund", "basset hound", "bloodhound", "greyhound",
    "whippet", "afghan hound", "rhodesian ridgeback", "basenji", "coonhound",
    # Working Group
    "rottweiler", "boxer", "doberman pinscher", "great dane", "mastiff",
    "siberian husky", "alaskan malamute", "saint bernard", "bernese mountain dog",
    "newfoundland", "samoyed", "akita", "portuguese water dog",
    # Terrier Group
    "bull terrier", "staffordshire bull terrier", "american staffordshire terrier",
    "west highland white terrier", "scottish terrier", "jack russell terrier",
    "airedale terrier", "miniature schnauzer", "yorkshire terrier", "cairn terrier",
    # Toy Group
    "chihuahua", "pomeranian", "pug", "shih tzu", "maltese", "pekingese",
    "cavalier king charles spaniel", "papillon", "havanese", "toy poodle",
    # Non-Sporting Group
    "bulldog", "french bulldog", "poodle", "boston terrier", "bichon frise",
    "dalmatian", "chow chow", "shiba inu", "lhasa apso", "chinese shar-pei",
    # Herding Group
    "german shepherd", "australian shepherd", "border collie", "pembroke welsh corgi",
    "cardigan welsh corgi", "shetland sheepdog", "collie", "belgian malinois",
    "australian cattle dog", "old english sheepdog",
    # Common variations and mixed breeds
    "labrador", "lab", "golden", "german shepherd dog", "gsd", "pit bull",
    "pitbull", "husky", "corgi", "poodle", "doodle", "goldendoodle",
    "labradoodle", "cockapoo", "schnoodle", "puggle", "mixed", "mixed breed",
    "mutt",
]


def validate_required(value: Any, field_name: str) -> Optional[str]:
    """Validate that a required field has a value.

    Args:
        value: The value to validate.
        field_name: Name of the field for error messages.

    Returns:
        str: Error message if validation fails, None if valid.

    Example:
        >>> validate_required("", "name")
        'name is required'
        >>> validate_required("Buddy", "name")
        None
    """
    if value is None:
        return f"{field_name} is required"

    if isinstance(value, str) and not value.strip():
        return f"{field_name} is required"

    return None


def validate_string_length(
    value: str,
    field_name: str,
    min_length: int = 0,
    max_length: int = 255,
) -> Optional[str]:
    """Validate string length is within bounds.

    Args:
        value: The string to validate.
        field_name: Name of the field for error messages.
        min_length: Minimum allowed length (default 0).
        max_length: Maximum allowed length (default 255).

    Returns:
        str: Error message if validation fails, None if valid.

    Example:
        >>> validate_string_length("Hi", "name", min_length=3)
        'name must be at least 3 characters'
    """
    if not isinstance(value, str):
        return f"{field_name} must be a string"

    if len(value) < min_length:
        return f"{field_name} must be at least {min_length} characters"

    if len(value) > max_length:
        return f"{field_name} must be at most {max_length} characters"

    return None


def validate_positive_number(
    value: Any,
    field_name: str,
    allow_zero: bool = True,
) -> Optional[str]:
    """Validate that a value is a positive number.

    Args:
        value: The value to validate.
        field_name: Name of the field for error messages.
        allow_zero: Whether zero is a valid value (default True).

    Returns:
        str: Error message if validation fails, None if valid.

    Example:
        >>> validate_positive_number(-5, "age")
        'age must be a positive number'
    """
    if value is None:
        return None  # Optional field

    try:
        num = float(value)
    except (TypeError, ValueError):
        return f"{field_name} must be a number"

    if allow_zero and num < 0:
        return f"{field_name} must be a positive number"

    if not allow_zero and num <= 0:
        return f"{field_name} must be greater than zero"

    return None


def validate_enum_value(
    value: Any,
    field_name: str,
    allowed_values: list,
) -> Optional[str]:
    """Validate that a value is in a list of allowed values.

    Args:
        value: The value to validate.
        field_name: Name of the field for error messages.
        allowed_values: List of valid values.

    Returns:
        str: Error message if validation fails, None if valid.

    Example:
        >>> validate_enum_value("dragon", "species", ["dog", "cat"])
        "species must be one of: dog, cat"
    """
    if value is None:
        return None  # Optional field

    # Case-insensitive comparison for strings
    if isinstance(value, str):
        lower_value = value.lower()
        lower_allowed = [v.lower() if isinstance(v, str) else v for v in allowed_values]
        if lower_value not in lower_allowed:
            return f"{field_name} must be one of: {', '.join(str(v) for v in allowed_values)}"
    elif value not in allowed_values:
        return f"{field_name} must be one of: {', '.join(str(v) for v in allowed_values)}"

    return None


def validate_dog_breed(breed: Any, species: str) -> Optional[str]:
    """Validate that a breed is a real dog breed when species is 'dog'.

    Args:
        breed: The breed value to validate.
        species: The species of the pet.

    Returns:
        str: Error message if validation fails, None if valid.

    Example:
        >>> validate_dog_breed("unicorn", "dog")
        "breed 'unicorn' is not a recognized dog breed"
        >>> validate_dog_breed("labrador", "dog")
        None
        >>> validate_dog_breed("tabby", "cat")
        None
    """
    if breed is None:
        return None  # Breed is optional

    if not isinstance(species, str) or species.lower() != "dog":
        return None  # Only validate breeds for dogs

    if not isinstance(breed, str):
        return "breed must be a string"

    lower_breed = breed.lower().strip()
    if lower_breed not in VALID_DOG_BREEDS:
        return f"breed '{breed}' is not a recognized dog breed"

    return None
