from serialpy import utils, PRINT

def all(file_path: str, word: str, replacement: str, output: bool = PRINT):
    with open(file_path, 'r') as file:
            # Read each line into a list
            lines = file.readlines()

        # Perform the update in-memory
    updated, count = utils.update(lines, word, replacement)
    print("\033[1;95m{} instances of {} found and replaced with {}!\033[00m".format(count, word, replacement))

    with open(file_path, 'w') as file:
        file.writelines(updated)
    
    return output

''' WIP
def keys(file: str, word: str, replace: str, output: bool = PRINT):
    find = "key"
    count = [0]
    contents = utils.loader(file)
    updated, count = utils.update(contents, word, replace, find, count)
    import pdb; pdb.set_trace()
    if utils.writer(file, updated):  # Access the updated contents from the tuple
        if output: 
            print("\033[1;95m{} instances of {} replaced with {}!\033[00m".format(count, word, replace))
        return updated
    return None

def values(file: str, word: str, replace: str, output: bool = PRINT):
    find = "value"
    count = [0]
    contents = utils.loader(file)
    updated, count = utils.update(contents, word, replace, find, count)
    import pdb; pdb.set_trace()
    if utils.writer(file, updated):  # Access the updated contents from the tuple
        if output: 
            print("\033[1;95m{} instances of {} replaced with {}!\033[00m".format(count, word, replace))
        return updated
    return None
'''
