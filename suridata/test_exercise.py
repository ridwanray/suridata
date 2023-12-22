import unittest
from exercise import clean_data, generate_pairs, main

class TestEmployeePairing(unittest.TestCase):

    def test_clean_data(self):
        employees = [
            ('John', 'Engineer', 170),
            ('Doe', 'Doctor', 180),
            ('John', 'Engineer', 170), # Duplicate
            ('Smith', 'Artist', 160)
        ]
        cleaned_employees = list(clean_data(employees))
        expected_result = [('John', 'Engineer', 170), ('Doe', 'Doctor', 180), ('Smith', 'Artist', 160)]
        self.assertEqual(cleaned_employees, expected_result)


    def test_generate_pairs(self):
        """Test the generate_pairs function."""
        chunked_employees = [('John', 'Engineer', 170), ('Doe', 'Doctor', 180)]
        pairs = generate_pairs(chunked_employees)
        self.assertEqual(len(pairs), 1)

    def test_main_function(self):
        """Test the main function."""
        employees_list = [
            ('John', 'Engineer', 170),
            ('Doe', 'Doctor', 180),
            ('Smith', 'Artist', 160),
            ('Jane', 'Lawyer', 175),
            ('John', 'Engineer', 170),  # Duplicate
            ('Doe', 'Doctor', 180)  # Duplicate
        ]
        unique_pairs = main(employees_list)
        self.assertIsInstance(unique_pairs, list)
        self.assertTrue(all(isinstance(pair, tuple) and len(pair) == 2 for pair in unique_pairs))

if __name__ == '__main__':
    unittest.main()
