"""Pet model for the Pet Adoption Center.

This module defines the Pet class and related validation logic.
"""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional

from src.utils.validators import validate_dog_breed


class PetStatus(Enum):
    """Enumeration of possible pet adoption statuses."""
    AVAILABLE = "available"
    PENDING = "pending"
    ADOPTED = "adopted"
    UNAVAILABLE = "unavailable"


VALID_SPECIES = ["dog", "cat", "bird", "rabbit", "hamster", "fish", "other"]


@dataclass
class Pet:
    """Represents a pet available for adoption.

    Attributes:
        id: Unique identifier for the pet.
        name: The pet's display name.
        species: Type of animal (dog, cat, etc.).
        breed: Specific breed (optional).
        age_years: Age in years (optional).
        description: Bio or personality description.
        status: Current adoption status.
        created_at: When the pet was added to the system.
        updated_at: Last modification timestamp.

    Example:
        >>> pet = Pet(name="Buddy", species="dog")
        >>> pet.status
        <PetStatus.AVAILABLE: 'available'>
    """
    name: str
    species: str
    id: Optional[int] = None
    breed: Optional[str] = None
    age_years: Optional[float] = None
    description: Optional[str] = None
    status: PetStatus = PetStatus.AVAILABLE
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    def __post_init__(self):
        """Validate pet data after initialization."""
        self.validate()

    def validate(self) -> None:
        """Validate pet data.

        Raises:
            ValueError: If any field fails validation.
        """
        if not self.name or not self.name.strip():
            raise ValueError("Pet name is required")

        if len(self.name) > 100:
            raise ValueError("Pet name must be 100 characters or less")

        if not self.species or self.species.lower() not in VALID_SPECIES:
            raise ValueError(f"Species must be one of: {', '.join(VALID_SPECIES)}")

        if self.age_years is not None and self.age_years < 0:
            raise ValueError("Age cannot be negative")

        # Validate dog breed if species is dog
        breed_error = validate_dog_breed(self.breed, self.species)
        if breed_error:
            raise ValueError(breed_error)

    def to_dict(self) -> dict:
        """Convert pet to dictionary representation.

        Returns:
            dict: Pet data as a dictionary.
        """
        return {
            "id": self.id,
            "name": self.name,
            "species": self.species,
            "breed": self.breed,
            "age_years": self.age_years,
            "description": self.description,
            "status": self.status.value,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Pet":
        """Create a Pet instance from a dictionary.

        Args:
            data: Dictionary containing pet data.

        Returns:
            Pet: New Pet instance.

        Raises:
            ValueError: If required fields are missing.
        """
        status = data.get("status", "available")
        if isinstance(status, str):
            status = PetStatus(status)

        return cls(
            id=data.get("id"),
            name=data["name"],
            species=data["species"],
            breed=data.get("breed"),
            age_years=data.get("age_years"),
            description=data.get("description"),
            status=status,
        )
