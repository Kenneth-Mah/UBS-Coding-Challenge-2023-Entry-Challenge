from typing import Dict, List


def getNextProbableWords(classes: List[Dict], statements: List[str]) -> Dict[str, List[str]]:
    # Create a dictionary to store class definitions
    class_definitions = {}
    for class_def in classes:
        for class_name, attributes in class_def.items():
            class_definitions[class_name] = attributes

    # Create a dictionary to store probable words for statements
    probable_words = {}

    # Process each statement
    for statement in statements:
        # Split the statement into class and variable
        parts = statement.split(".")
        class_name = parts[0]  # The first part is always the class name
        variable = ".".join(parts[1:])  # Join all remaining parts as the variable

        # Initialize a list to store probable words
        probable_word_list = []

        # Check if the class exists in class_definitions
        if class_name in class_definitions:
            attributes = class_definitions[class_name]

            # Handle an empty class (Case 1)
            if attributes == "":
                probable_word_list.append("")

            # Handle a class containing key-value pairs (Case 2)
            elif isinstance(attributes, dict):
                if variable == "":
                    # Return all keys for this case
                    probable_word_list.extend(attributes.keys())
                elif variable in attributes:
                    # Check if the variable exists as a key in the class
                    probable_word_list.append(attributes[variable])

            # Handle a list of strings (Case 3)
            elif isinstance(attributes, list):
                if variable == "":
                    # Return all items in the list for this case
                    probable_word_list.extend(attributes)
                elif variable in attributes:
                    # Check if the variable exists in the list (polymorphic type)
                    probable_word_list.append("")

        # Sort the probable words in ascending alphabetical order
        probable_word_list.sort()

        # Limit the list to at most 5 words
        probable_word_list = probable_word_list[:5]

        # Store the probable words for this statement
        probable_words[statement] = probable_word_list

    return probable_words