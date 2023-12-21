import random
from multiprocessing import Pool


def clean_data(employees: list) -> list:
    """Clean duplicates from the data source using fields combination."""
    seen = set()  # keep track of seen combinations
    for each in employees:
        key = tuple(each)
        if key not in seen:
            seen.add(key)
            yield each


def chunk_generator(data, chunk_size):
    """Generate cleaned chunks of data."""
    chunk = []

    # Loop through cleaned data and yield chunks of specified size
    for item in clean_data(data):
        chunk.append(item)

        # Check if the chunk is of the desired size
        if len(chunk) == chunk_size:
            yield chunk
            chunk = []  # empty the chunk container for next iteration

    # Yield the remaining items if any that does not match the size
    if chunk:
        yield chunk


def generate_pairs(chunked_employees):
    """Generate random pairs ensuring uniqueness names."""
    random.shuffle(chunked_employees)

    pairs = []
    while len(chunked_employees) >= 2:
        employee1 = chunked_employees.pop(0)[0]
        employee2 = chunked_employees.pop(0)[0]

        # Ensure that the pair is unique
        if (employee1, employee2) not in pairs and (employee2, employee1) not in pairs:
            pairs.append((employee1, employee2))
    return pairs


def main(employees):
    num_of_chunks = 2

    chunks = list(chunk_generator(employees, num_of_chunks))

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
        ("John", "Engineer", 170),  # Duplicate
        ("Doe", "Doctor", 180),  # Duplicate
    ]

    unique_pairs = main(employees_list)
    print("Final Unique Pairs:", unique_pairs)
