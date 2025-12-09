# Complete Database Schema

## Tables

### pets
| Column | Type | Description |
|--------|------|-------------|
| id | UUID | Primary key |
| name | VARCHAR(100) | Pet's name |
| species | VARCHAR(50) | dog, cat, bird, etc. |
| breed | VARCHAR(100) | Specific breed |
| age_years | INTEGER | Age in years |
| shelter_id | UUID | FK to shelters |
| is_active | BOOLEAN | Soft delete flag |
| created_at | TIMESTAMP | Record creation |
| updated_at | TIMESTAMP | Last update |

### shelters
| Column | Type | Description |
|--------|------|-------------|
| id | UUID | Primary key |
| name | VARCHAR(200) | Shelter name |
| address | TEXT | Full address |
| capacity | INTEGER | Max pets |

### adoptions
| Column | Type | Description |
|--------|------|-------------|
| id | UUID | Primary key |
| pet_id | UUID | FK to pets |
| adopter_name | VARCHAR(200) | Person adopting |
| adoption_date | DATE | When adopted |
