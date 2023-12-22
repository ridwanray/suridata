import random
from multiprocessing import Pool


def clean_data(employees: list) -> list:
    """Clean duplicates from the data source using fields combination."""
    seen = set()  # keep track of seen combinations
    for each in employees:
        key = tuple(each)
        if key not in seen:
            seen.add(key)
    return seen


def generate_pairs(chunked_employees):
    """Generate random pairs ensuring uniqueness names."""
    random.shuffle(chunked_employees)

    pairs = []
    while len(chunked_employees) >= 2:
        employee1 = chunked_employees.pop()[0]
        employee2 = chunked_employees.pop()[0]

        # Ensure that the pair is unique
        if (employee1, employee2) not in pairs and (employee2, employee1) not in pairs:
            pairs.append((employee1, employee2))
    return pairs


def main(employees):
    num_chunks = 3 
    unique_data = list(clean_data(employees))
    chunk_size = len(clean_data(employees)) // num_chunks
    chunks = [unique_data[i:i + chunk_size] for i in range(0, len(unique_data), chunk_size)]

    # Use multiprocessing Pool to process chunks in parallel
    with Pool() as pool:
        results = pool.map(generate_pairs, chunks)

    final_pairs = [pair for sublist in results for pair in sublist]

    return final_pairs


if __name__ == "__main__":
    employees_list = [
        ("John", "Engineer", 170),
        ("Doe", "Doctor", 180),
        ("Smith", "Artist", 160),

        ("Jane", "Lawyer", 175),
        ("Ray", "Lawyer", 175),
        ("Lee", "Lawyer", 175),

        ("Python", "Lawyer", 175),
        ("Node", "Lawyer", 175),
        ("Billy", "Engineer", 170),

        ("Kay", "Doctor", 180),
        ("Mayegun", "Engineer", 170),
        ("Ajayi", "Doctor", 180),

        ("John", "Engineer", 170),  # Duplicate
        ("Doe", "Doctor", 180),  # Duplicate
    ]

    unique_pairs = main(employees_list)
    print("Final Unique Pairs:", unique_pairs)
