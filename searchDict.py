import sys
import json
import yaml
import string

FOUND=[]
TAB_COUNTER=0

# LVL 3
# QUERY TOOLS - each get arg
# --------------------------
def _query_both(d, phrase, instances=FOUND):
    for key, value in d.items():
        instance={}
        if phrase in [key, value, str(key), str(value)]:
            instance[key]=value
            instances.append(instance)
        _query_both(value, phrase, instances) if type(value)==dict else None
        if type(value)==list:
            [_query_both(i, phrase, instances) for i in value if type(i)==dict]
        _query_both(key, phrase, instances) if type(key)==dict else None
        if type(key)==list:
            [_query_key(i, phrase, instances) for i in key if type(i)==dict]

def _query_value(d, phrase, instances=FOUND):
    for key, value in d.items():
        if phrase in [key, value, str(key), str(value)]:
            instances.append(value)
        _query_value(value, phrase, instances) if type(value)==dict else None
        if type(value)==list:
            [_query_value(i, phrase, instances) for i in value if type(i)==dict]
        _query_value(key, phrase, instances) if type(key)==dict else None
        if type(key)==list:
            [_query_key(i, phrase, instances) for i in key if type(i)==dict]
        
def _query_key(d, phrase, instances=FOUND):
    for key, value in d.items():
        if phrase in [key, value, str(key), str(value)]:
            instances.append(key)
        _query_key(value, phrase, instances) if type(value)==dict else None
        if type(value)==list:
            [_query_key(i, phrase, instances) for i in value if type(i)==dict]
        _query_key(key, phrase, instances) if type(key)==dict else None
        if type(key)==list:
            [_query_key(i, phrase, instances) for i in key if type(i)==dict]

def _query_structure(d, phrase, instances=FOUND, tc=TAB_COUNTER):
    for key, value in d.items():
        if phrase in [value, str(value), key, str(key)]:
            print(f"\033[1;92m{key}: {value}\033[00m")
            instances.append(value)
        else:
            _query_structure(value, phrase, instances) and print(f"{key}: ",end='') if type(value)==dict else print(f"{key}: {value}")
            if type(value)==list:
                [_query_structure(i, phrase, instances) for i in value if type(i)==dict]
            _query_structure(key, phrase, instances) if type(key)==dict else None


# LVL 2
# MAIN QUERY CALL - based on get arg
def _query(f: dict, x: str, p: str, get="both"):
    if get=="value":
        _query_value(f, x)
    elif get=="key":
        _query_key(f, x)
    elif get=="structure":
        _query_structure(f, x)
    else: _query_both(f, x)
    
    if p != "off":
        print("{} instances of {} found!".format(len(FOUND), x))
        if not get=="structure":
            for index, x in enumerate(FOUND):
                print("\033[1;95m({}) {}\033[00m".format(index+1, x)) if (index+1)%5==0 else print("({}) {}".format(index+1, x))
    return FOUND

# OPENING FILE PATHS
# ------------------
# LVL 3
# YAML 
def _open_yaml(f):
    with open(f, "r") as file:
        try:
            opened=yaml.safe_load(file)
            return opened
        except yaml.YAMLError:
            print("ERROR: Raised when loading file: ", f)

# LVL 3
# JSON
# def _open_json(f):

# LVL 2
def _open_file(file_path):
    if file_path.endswith(".yaml"):
        return _open_yaml(file_path)
    elif file_path.endswith(".json"):
        return _open_json(file_path)
    elif file_path.endswith("}"):
        return json.loads(file_path)
    else:
        raise("ERROR: Cannot parse {}".format(peek_arg))

# LVL 2
# CHECKING INPUT VARIABLES
def _check_display_arg(arg):
    if arg in ["key", "Key", "KEY", "keys", "Keys", "KEYS"]:
        return "key"
    elif arg in ["value", "Value", "VALUE", "values", "Values", "VALUES"]:
        return "value"
    elif arg in ["both", "Both", "BOTH", "all", "All", "ALL"]:
        return "both"
    elif arg in ["struct", "Struct", "STRUCT", "structure", "Structure", "STRUCTURE"]:
        return "structure"
    else:
        raise("ERROR: Incorrect value for ", arg)

# LVL 1
# *CALLABLE* SEARCH BAR 
    #file-path/dict
    #d2esired word
    #<default: both> type of return value
    #<default: off> turns on/off printing to console
def search(f: dict, x: str, get="both", print="off"):
    peek_file=_open_file(f) 
    display=_check_display_arg(get)
    return _query(peek_file, x, print, get)

# LVL 1
if __name__ == '__main__':
    # PRESET PRINT STATE FOR TERMINAL BASED USE
    print_results='on'
    num_args = len(sys.argv) # getting the number of args passed
    if num_args > 4 or num_args < 3: # checks for incorrect arg amount
        raise("ERROR: Call `search` with 2 or 3 arguments")
    
    peek_arg=sys.argv[1] # accessing file-path/dictionary to be parsed
    find_arg=sys.argv[2] # accessing desired word to be found
    
    peek_file=_open_file(peek_arg) # calls the 
    
    if num_args==4: # checks display setting input 
        display=_check_display_arg(sys.argv[3])
        results=_query(peek_file, find_arg, print_results, display)
    else: results=_query(peek_file, find_arg, print_results)
