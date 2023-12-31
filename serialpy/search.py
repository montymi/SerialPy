from serialpy import utils, PRINT

def all(file: str, word: str, ret: str = "all", output: bool = PRINT):
    '''
    Searches for occurrences of a word in all keys and values within serialized data, prints matches to console.

    :param file: The path to the file to search.
    :param word: The word to search for.
    :param ret: Specify "both", "key", or "value" to control the output format (default is "both").
    :type file, word, ret: str
    :param output: True sets console output, default set in config.toml.
    :return: A list of found instances.
    :rytpe: list
    '''
    find = "all" 
    found = []
    contents = utils.loader(file)
    found = utils.query(contents, word, find, ret, found)
    if output:
        print("\033[1;95m{} instances of {} found!\033[00m".format(len(found), word))
        for index, x in enumerate(found):
            print("{} | ".format(index+1), x)
    return found

def keys(file: str, word: str, ret: str = "all", output: bool = PRINT):
    '''
    Searches for occurrences of a word in all keys within serialized data, prints matches to console.

    :param file: The path to the file to search.
    :param word: The word to search for.
    :param ret: Specify "both", "key", or "value" to control the output format (default is "both").
    :type file, word, ret: str
    :param output: True sets console output, default set in config.toml.
    :return: A list of found instances.
    :rytpe: list
    '''
    find = "key" 
    found = []
    contents = utils.loader(file)
    found = utils.query(contents, word, find, ret, found)
    if output:
        print("\033[1;95m{} instances of {} found!\033[00m".format(len(found), word))
        for index, x in enumerate(found):
            print("{} | ".format(index+1), x)
    return found

def values(file: str, word: str, ret: str = "all", output: bool = PRINT):
    '''
    Searches for occurrences of a word in all values within serialized data, prints matches to console.

    :param file: The path to the file to search.
    :param word: The word to search for.
    :param ret: Specify "both", "key", or "value" to control the output format (default is "both").
    :type file, word, ret: str
    :param output: True sets console output, default set in config.toml.
    :return: A list of found instances.
    :rytpe: list
    '''
    find = "value" 
    found = []
    contents = utils.loader(file)
    found = utils.query(contents, word, find, ret, found)
    if output:
        print("\033[1;95m{} instances of {} found!\033[00m".format(len(found), word))
        for index, x in enumerate(found):
            print("{} | ".format(index+1), x)
    return found
