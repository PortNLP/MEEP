import json
from typing import List
import random
import os


class SeeSelector:
    def get_random_numbers(self, count: int, start:int, end:int) -> List[int]:
        if count > (end - start + 1):
            raise ValueError("Number of requested random numbers exceeds the range.")

        random_numbers = random.sample(range(start, end + 1), count)
        return random_numbers
    

    def extract_item_numbers(self, select_numbers, input_file_path, output_file_path):
        with open(input_file_path, 'r') as input_file:
            data = json.load(input_file)

        items = [data[i] for i in select_numbers]

        with open(output_file_path, 'w') as output_file:
            json.dump(items, output_file, indent=4)

    def get_random_subset(self, input_file_path, output_file_path, count: int, start: int, end: int) -> None:
        selection_numbers = self.get_random_numbers(count, start, end)
        self.extract_item_numbers(selection_numbers, input_file_path, output_file_path)

count = 300
start = 0
end = 3315
input_file_path = os.path.join(
    os.getcwd(),
    '..',
    'Datasets',
    'DSTC_11_Track_4',
    'metadata',
    'dev',
    'en',
    'persona-see',
    'persona-see_eval.json'
)
output_file_path = os.path.join(
    os.getcwd(),
    '..',
    'Datasets',
    'DSTC_11_Track_4',
    'metadata',
    'dev',
    'en',
    'persona-see',
    'persona-see_eval_subset_of_300.json'
)
SeeSelector().get_random_subset(input_file_path, output_file_path, count, start, end)
