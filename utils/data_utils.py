import csv

from models.data import Data


def is_duplicate_data(data_name: str, seen_names: set) -> bool:
    return data_name in seen_names


def is_complete_data(data: dict, required_keys: list) -> bool:
    return all(key in data for key in required_keys)


def save_data_to_csv(data: list, filename: str):
    if not data:
        print("No data to save.")
        return

    # Use field names from the Venue model
    fieldnames = Data.model_fields.keys()

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    print(f"Saved {len(data)} venues to '{filename}'.")