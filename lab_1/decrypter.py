import argparse
import json
import logging
import os
from writer_and_reader import read_from_file, write_to_file


logging.basicConfig(level=logging.INFO)


def char_freq_analysis(text: str, json_text:str) -> dict:
    """Perform character frequency analysis of the given text."""
    data = read_from_file(text)
    my_dict = {}

    for char in data:
        my_dict[char] = my_dict.get(char, 0) + 1

    total_chars = len(data)
    relative_freq_dict = {char: count / total_chars for char, count in my_dict.items()}

    sorted_dict = dict(sorted(relative_freq_dict.items(), key=lambda x: x[1], reverse=True))

    with open(json_text, "w", encoding="utf-8") as json_file:
        json.dump(sorted_dict, json_file, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Perform character frequency analysis.")
    parser.add_argument("--input_file",
                        type=str,
                        default=os.path.join('lab_1','task2','cod1.txt'),
                        help="Path to the input file.")
    parser.add_argument("--output_file",
                        type=str,
                        default=os.path.join('lab_1','task2','result.json'),
                        help="Path to the output JSON file.")
    args = parser.parse_args()
    
    if not os.path.exists(args.input_file):
        logging.error(f"File '{args.input_file}' does not exist.")
        exit(1)
    
    char_freq_analysis(args.input_file, args.output_file)