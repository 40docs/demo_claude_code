"""Pet API endpoints for the Pet Adoption Center.

This module provides RESTful API handlers for pet operations.
"""

from typing import Optional
from src.models.pet import Pet, PetStatus, VALID_SPECIES
from src.utils.validators import validate_required, validate_string_length


# In-memory storage for demo purposes
_pets_db: dict[int, Pet] = {}
_next_id: int = 1


def _success_response(data, message: str = "Success") -> dict:
    """Create a standard success response."""
    return {
        "success": True,
        "data": data,
        "message": message,
    }


def _error_response(code: str, message: str) -> dict:
    """Create a standard error response."""
    return {
        "success": False,
        "error": {
            "code": code,
            "message": message,
        },
    }


def list_pets(species: Optional[str] = None, status: Optional[str] = None) -> dict:
    """List all pets with optional filtering.

    Args:
        species: Filter by species (optional).
        status: Filter by adoption status (optional).

    Returns:
        dict: Response containing list of pets.
    """
    pets = list(_pets_db.values())

    if species:
        pets = [p for p in pets if p.species.lower() == species.lower()]

    if status:
        pets = [p for p in pets if p.status.value == status.lower()]

    return _success_response(
        data=[p.to_dict() for p in pets],
        message=f"Found {len(pets)} pets",
    )


def get_pet(pet_id: int) -> dict:
    """Get a specific pet by ID.

    Args:
        pet_id: The pet's unique identifier.

    Returns:
        dict: Response containing pet data or error.
    """
    pet = _pets_db.get(pet_id)

    if not pet:
        return _error_response("NOT_FOUND", f"Pet with ID {pet_id} not found")

    return _success_response(data=pet.to_dict())


def create_pet(data: dict) -> dict:
    """Create a new pet.

    Args:
        data: Dictionary containing pet data.

    Returns:
        dict: Response containing created pet or error.
    """
    global _next_id

    # Validate required fields
    name_error = validate_required(data.get("name"), "name")
    if name_error:
        return _error_response("VALIDATION_ERROR", name_error)

    species_error = validate_required(data.get("species"), "species")
    if species_error:
        return _error_response("VALIDATION_ERROR", species_error)

    # Validate name length
    length_error = validate_string_length(data["name"], "name", max_length=100)
    if length_error:
        return _error_response("VALIDATION_ERROR", length_error)

    # Validate species
    if data["species"].lower() not in VALID_SPECIES:
        return _error_response(
            "VALIDATION_ERROR",
            f"Invalid species. Must be one of: {', '.join(VALID_SPECIES)}",
        )

    try:
        pet = Pet.from_dict(data)
        pet.id = _next_id
        _next_id += 1
        _pets_db[pet.id] = pet

        return _success_response(
            data=pet.to_dict(),
            message="Pet created successfully",
        )
    except ValueError as e:
        return _error_response("VALIDATION_ERROR", str(e))


def update_pet(pet_id: int, data: dict) -> dict:
    """Update an existing pet.

    Args:
        pet_id: The pet's unique identifier.
        data: Dictionary containing updated pet data.

    Returns:
        dict: Response containing updated pet or error.
    """
    pet = _pets_db.get(pet_id)

    if not pet:
        return _error_response("NOT_FOUND", f"Pet with ID {pet_id} not found")

    # Update allowed fields
    if "name" in data:
        pet.name = data["name"]
    if "species" in data:
        pet.species = data["species"]
    if "breed" in data:
        pet.breed = data["breed"]
    if "age_years" in data:
        pet.age_years = data["age_years"]
    if "description" in data:
        pet.description = data["description"]
    if "status" in data:
        pet.status = PetStatus(data["status"])

    try:
        pet.validate()
        return _success_response(
            data=pet.to_dict(),
            message="Pet updated successfully",
        )
    except ValueError as e:
        return _error_response("VALIDATION_ERROR", str(e))


def delete_pet(pet_id: int) -> dict:
    """Delete a pet.

    Args:
        pet_id: The pet's unique identifier.

    Returns:
        dict: Response confirming deletion or error.
    """
    if pet_id not in _pets_db:
        return _error_response("NOT_FOUND", f"Pet with ID {pet_id} not found")

    del _pets_db[pet_id]

    return _success_response(
        data=None,
        message=f"Pet {pet_id} deleted successfully",
    )
