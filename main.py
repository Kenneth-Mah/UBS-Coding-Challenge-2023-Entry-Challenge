from typing import Dict, List


def getNextProbableWords(classes: List[Dict],
                         statements: List[str]) -> Dict[str, List[str]]:
    # Convert the list of dictionaries into a single dictionary for easier access
    class_dict = {}
    for class_def in classes:
        for key, value in class_def.items():
            class_dict[key] = value

    def get_next_words(class_name, partial=""):
        # If the class name is not in the dictionary, return an empty list
        if class_name not in class_dict:
            return [""]

        # Fetch the definition of the class
        class_def = class_dict[class_name]

        # If it's an empty class, return an empty list
        if class_def == "":
            return [""]

        # If it's a dictionary, return the keys that match the partial word
        if isinstance(class_def, dict):
            matching_keys = [
                key for key in class_def.keys() if key.startswith(partial)
            ]

            # If the matching key is a polymorphic type, return an empty list
            if len(matching_keys) == 1 and "List<" in class_def[
                    matching_keys[0]]:
                return [""]

            return sorted(matching_keys)[:5]

        # If it's a list, determine if it's an enum or a polymorphic type
        if isinstance(class_def, list):
            # Check the first element of the list to determine the type
            first_element = class_def[0]

            # If it's a string and not a class name, it's an enum
            if isinstance(first_element,
                          str) and first_element not in class_dict:
                matching_enums = [
                    key for key in class_def if key.startswith(partial)
                ]
                return sorted(matching_enums)[:5]

            # If it's a string and a class name, it's a polymorphic type
            if isinstance(first_element, str) and first_element in class_dict:
                return [""]

        return [""]

    results = {}
    for statement in statements:
        parts = statement.split('.')

        # Get the class name (always the first part of the statement)
        class_name = parts[0]

        # If there's a partial word, it's the second part of the statement
        partial = parts[1] if len(parts) > 1 else ""

        results[statement] = get_next_words(class_name, partial)

    return results