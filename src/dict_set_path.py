def dict_set_path(dictionary, path, val, path_sep = "."):
    path = path.split(path_sep)
    if len(path)<1:
        return dictionary
    # go to last dictionary
    current = dictionary
    for item in path[:-1]:
        if item not in current:
            current[item] = dict()
        current = current[item]
    current[path[-1]] = val
    return dictionary
