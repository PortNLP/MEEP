import json
import os

IDS_IN_SUBSET = 300

class SeeSubsetMaker:
    def make_subset(self, ids_file_path, see_file_path, subset_file_path):
        with open(ids_file_path, 'r') as ids_file:
            ids = json.load(ids_file)

        dialogue_ids = [ids[i] for i in range(IDS_IN_SUBSET)]

        with open(see_file_path, 'r') as see_file:
            full_data = json.load(see_file)

        subset_data = [entry for entry in full_data if entry['dialogue_id'] in dialogue_ids]

        with open(subset_file_path, 'w') as subset_file:
            json.dump(subset_data, subset_file, indent=4)

ids_file_path = 'persona-see_subset_dialogue_ids.json'
see_file_path = os.path.join(
    os.getcwd(),
    '..',
    '..',
    'Datasets',
    'DSTC_11_Track_4',
    'metadata',
    'dev',
    'en',
    'persona-see',
    'persona-see_eval.json'
)
subset_file_path = os.path.join(
    os.getcwd(),
    '..',
    '..',
    'Datasets',
    'DSTC_11_Track_4',
    'metadata',
    'dev',
    'en',
    'persona-see',
    'persona-see_eval_subset_of_300_en.json'
)

SeeSubsetMaker().make_subset(ids_file_path, see_file_path, subset_file_path)
