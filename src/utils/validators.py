"""Validation utilities for the Pet Adoption Center.

This module provides reusable validation functions for input data.
"""

from typing import Any, Optional


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
