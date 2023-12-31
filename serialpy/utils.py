import json
import yaml
import tomllib

# Get Serialized Data
# -------------------
# YAML 
def _open_yaml(f):
    with open(f, "r") as file:
        try:
            return yaml.load(file, yaml.Loader)
        except yaml.YAMLError as err:
            print("ERROR: Raised when loading configuration file: ", f)
            print(err)

# JSON
def _open_json(f):
    with open(f, "r") as file:
        try:
            return json.load(file)
        except ValueError as err:
            print("ERROR: Raised when loading configuration file: ", f)
            print(err)

# TOML
def _open_toml(f):
    with open(f, 'rb') as file:
        try:
            return tomllib.load(file)
        except tomllib.TOMLDecodeError as err:
            print("ERROR: Raised when loading configuration file: ", f)
            print(err)

# LOADER
# ------
def loader(file_path: str):
    '''
    Loads and parses a configuration file based on its file extension.

    :param file_path: The path to the configuration file.
    :type file_path: str

    :return: Parsed content of the configuration file.
    :rtype: dict
    '''
    if file_path.endswith(".yaml"):
        return _open_yaml(file_path)
    elif file_path.endswith(".json"):
        return _open_json(file_path)
    elif file_path.endswith(".toml"):
        return _open_toml(file_path)
    elif file_path.endswith("}"):
        return json.loads(file_path)
    else:
        print("ERROR: Cannot parse {}".format(file_path))

# WRITER
# ------
def writer(file_path: str, data):
    '''
    Loads and parses a configuration file based on its file extension.

    :param file_path: The path to the configuration file.
    :type file_path: str
    :param data: updated content to be written to file_path

    :return: true for successful write to file.
    :rtype: bool
    '''
    if file_path.endswith(".yaml"):
        with open(file_path, 'w') as file:
            file.writelines(data) if isinstance(data, list) else None
    elif file_path.endswith(".json"):
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=2) 
    else:
        print("ERROR: Cannot write to {}".format(file_path))
        return False
    return True

# CHECKING QUERY CONFIG ARGUMENTS
# -------------------------------
def _check_display_args(ret: str):
    arg_mappings = {
        "key": ["key", "Key", "KEY", "keys", "Keys", "KEYS"],
        "value": ["value", "Value", "VALUE", "values", "Values", "VALUES"],
        "both": ["both", "Both", "BOTH", "all", "All", "ALL"],
    }
    
    show = "both"
    for ret_type, aliases in arg_mappings.items():
        if ret in aliases:
            show = ret_type

    return show

# Result Filtering
# ----------------
def _update_add(show: str, key, value):
    if show == "key":
        return key
    elif show == "value":
        return value
    else:
        return {key: value}

# QUERY
# -----
def query(contents: (dict, list), word: str, find: str, ret: str, found: list):
    '''
    Recursively searches for occurrences of a word in keys and/or values within nested dictionaries and lists.

    :param contents: The data structure to search.
    :type contents: dict or list

    :param word: The word to search for.
    :param find: Specify "key", "value", or "both" to control the search scope (default is "both").
    :param ret: Specify "key", "value", or "both" to control the output format (default is "both").
    :type word, find, ret: str

    :param found: A list to store found instances.
    :type found: list

    :return: A list of found instances.
    :rtype: list

    Note:
    - The function performs a case-sensitive search.
    - The search scope is controlled by the 'find' parameter.
    - The output format is controlled by the 'ret' parameter.
    '''
    show = _check_display_args(ret)
    if isinstance(contents, dict):
        for key, value in contents.items():
            add = None
            if find == "key":
                if word in [key, str(key)]:
                    add = _update_add(show, key, value)
            elif find == "value":
                if word in [value, str(value)]:
                    add = _update_add(show, key, value)
            else:
                if word in [key, str(key), value, str(value)]:
                    add = _update_add(show, key, value)
            found.append(add) if add is not None else None 
            query(value, word, find, show, found)
            query(key, word, find, show, found)
    elif isinstance(contents, list):
        for item in contents:
            query(item, word, find, show, found)
    
    return found

# UPDATE
# -----------
def update(contents, word: str, replace: str, count: int = 0):
    for i, line in enumerate(contents):
        if word in line:
            count += 1
        contents[i] = line.replace(word, replace)

    return contents, count
