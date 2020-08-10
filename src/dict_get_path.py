
def dict_get_path(dictionary, path, default=None, path_sep = "."):
    path = path.split(path_sep)
    if len(path)==0:
        return dictionary
    # go to last entry
    current = dictionary
    for item in path:
        if item not in current:
            return default
        current = current[item]
    return current
    
