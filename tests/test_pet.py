"""Tests for Pet model and API.

Run with: pytest tests/test_pet.py -v
"""

import pytest
from src.models.pet import Pet, PetStatus, VALID_SPECIES
from src.api.pets import create_pet, get_pet, list_pets, update_pet, delete_pet


class TestPetModel:
    """Tests for the Pet model."""

    def test_create_pet_valid(self):
        """Test creating a pet with valid data."""
        pet = Pet(name="Buddy", species="dog")
        assert pet.name == "Buddy"
        assert pet.species == "dog"
        assert pet.status == PetStatus.AVAILABLE

    def test_create_pet_all_fields(self):
        """Test creating a pet with all optional fields."""
        pet = Pet(
            name="Whiskers",
            species="cat",
            breed="Tabby",
            age_years=2.5,
            description="Friendly and playful",
        )
        assert pet.breed == "Tabby"
        assert pet.age_years == 2.5
        assert pet.description == "Friendly and playful"

    def test_create_pet_missing_name(self):
        """Test that missing name raises ValueError."""
        with pytest.raises(ValueError, match="Pet name is required"):
            Pet(name="", species="dog")

    def test_create_pet_missing_species(self):
        """Test that missing species raises ValueError."""
        with pytest.raises(ValueError, match="Species must be one of"):
            Pet(name="Buddy", species="")

    def test_create_pet_invalid_species(self):
        """Test that invalid species raises ValueError."""
        with pytest.raises(ValueError, match="Species must be one of"):
            Pet(name="Puff", species="dragon")

    def test_create_pet_negative_age(self):
        """Test that negative age raises ValueError."""
        with pytest.raises(ValueError, match="Age cannot be negative"):
            Pet(name="Buddy", species="dog", age_years=-1)

    def test_create_pet_name_too_long(self):
        """Test that name over 100 characters raises ValueError."""
        long_name = "A" * 101
        with pytest.raises(ValueError, match="100 characters or less"):
            Pet(name=long_name, species="dog")

    def test_pet_to_dict(self):
        """Test converting pet to dictionary."""
        pet = Pet(name="Buddy", species="dog", id=1)
        data = pet.to_dict()
        assert data["id"] == 1
        assert data["name"] == "Buddy"
        assert data["species"] == "dog"
        assert data["status"] == "available"

    def test_pet_from_dict(self):
        """Test creating pet from dictionary."""
        data = {"name": "Buddy", "species": "dog", "breed": "Labrador"}
        pet = Pet.from_dict(data)
        assert pet.name == "Buddy"
        assert pet.breed == "Labrador"

    @pytest.mark.parametrize("species", VALID_SPECIES)
    def test_valid_species(self, species):
        """Test all valid species are accepted."""
        pet = Pet(name="Test", species=species)
        assert pet.species == species

    def test_create_dog_with_valid_breed(self):
        """Test creating a dog with a recognized breed."""
        pet = Pet(name="Buddy", species="dog", breed="Labrador Retriever")
        assert pet.breed == "Labrador Retriever"

    def test_create_dog_with_invalid_breed(self):
        """Test that invalid dog breed raises ValueError."""
        with pytest.raises(ValueError, match="not a recognized dog breed"):
            Pet(name="Buddy", species="dog", breed="Unicorn Dog")

    def test_create_dog_breed_case_insensitive(self):
        """Test that breed validation is case-insensitive."""
        pet = Pet(name="Buddy", species="dog", breed="GOLDEN RETRIEVER")
        assert pet.breed == "GOLDEN RETRIEVER"

    def test_create_cat_with_any_breed(self):
        """Test that cats can have any breed (no validation)."""
        pet = Pet(name="Whiskers", species="cat", breed="Tabby")
        assert pet.breed == "Tabby"

    def test_create_dog_without_breed_is_valid(self):
        """Test that dogs without a breed are still valid."""
        pet = Pet(name="Buddy", species="dog")
        assert pet.breed is None


class TestPetAPI:
    """Tests for the Pet API endpoints."""

    @pytest.fixture(autouse=True)
    def reset_db(self):
        """Reset the in-memory database before each test."""
        from src.api import pets
        pets._pets_db.clear()
        pets._next_id = 1

    def test_create_pet_success(self):
        """Test successful pet creation via API."""
        response = create_pet({"name": "Buddy", "species": "dog"})
        assert response["success"] is True
        assert response["data"]["name"] == "Buddy"
        assert response["data"]["id"] == 1

    def test_create_pet_missing_name(self):
        """Test create pet fails with missing name."""
        response = create_pet({"species": "dog"})
        assert response["success"] is False
        assert response["error"]["code"] == "VALIDATION_ERROR"

    def test_get_pet_success(self):
        """Test successful pet retrieval."""
        create_pet({"name": "Buddy", "species": "dog"})
        response = get_pet(1)
        assert response["success"] is True
        assert response["data"]["name"] == "Buddy"

    def test_get_pet_not_found(self):
        """Test get pet returns error for non-existent ID."""
        response = get_pet(999)
        assert response["success"] is False
        assert response["error"]["code"] == "NOT_FOUND"

    def test_list_pets_empty(self):
        """Test list pets returns empty list when no pets."""
        response = list_pets()
        assert response["success"] is True
        assert response["data"] == []

    def test_list_pets_with_filter(self):
        """Test list pets with species filter."""
        create_pet({"name": "Buddy", "species": "dog"})
        create_pet({"name": "Whiskers", "species": "cat"})

        response = list_pets(species="dog")
        assert response["success"] is True
        assert len(response["data"]) == 1
        assert response["data"][0]["species"] == "dog"

    def test_update_pet_success(self):
        """Test successful pet update."""
        create_pet({"name": "Buddy", "species": "dog"})
        response = update_pet(1, {"name": "Max"})
        assert response["success"] is True
        assert response["data"]["name"] == "Max"

    def test_update_pet_status(self):
        """Test updating pet status."""
        create_pet({"name": "Buddy", "species": "dog"})
        response = update_pet(1, {"status": "adopted"})
        assert response["success"] is True
        assert response["data"]["status"] == "adopted"

    def test_delete_pet_success(self):
        """Test successful pet deletion."""
        create_pet({"name": "Buddy", "species": "dog"})
        response = delete_pet(1)
        assert response["success"] is True

        # Verify pet is gone
        response = get_pet(1)
        assert response["success"] is False

    def test_delete_pet_not_found(self):
        """Test delete returns error for non-existent pet."""
        response = delete_pet(999)
        assert response["success"] is False
        assert response["error"]["code"] == "NOT_FOUND"

    def test_create_dog_with_valid_breed_via_api(self):
        """Test creating a dog with a valid breed via API."""
        response = create_pet({
            "name": "Max",
            "species": "dog",
            "breed": "German Shepherd"
        })
        assert response["success"] is True
        assert response["data"]["breed"] == "German Shepherd"

    def test_create_dog_with_invalid_breed_via_api(self):
        """Test that creating a dog with invalid breed fails via API."""
        response = create_pet({
            "name": "Max",
            "species": "dog",
            "breed": "Flying Dragon Dog"
        })
        assert response["success"] is False
        assert response["error"]["code"] == "VALIDATION_ERROR"
        assert "not a recognized dog breed" in response["error"]["message"]

    def test_update_dog_with_invalid_breed_via_api(self):
        """Test that updating a dog with invalid breed fails via API."""
        create_pet({"name": "Buddy", "species": "dog", "breed": "Labrador"})
        response = update_pet(1, {"breed": "Imaginary Breed"})
        assert response["success"] is False
        assert response["error"]["code"] == "VALIDATION_ERROR"
        assert "not a recognized dog breed" in response["error"]["message"]
