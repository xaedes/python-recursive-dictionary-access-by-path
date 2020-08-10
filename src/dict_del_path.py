import copy

def dict_del_path(dictionary, path, return_copy=False, path_sep = "."):
    path = path.split(path_sep)
    if return_copy:
        dictionary = copy.deepcopy(dictionary)
    if len(path)<1:
        return dictionary
    # go to last dictionary
    
    current = dictionary
    chain = [current]
    for item in path[:-1]:
        if item not in current:
            return dictionary
        current = current[item]
        chain.append(current)
    
    # propagating delete starting from value
    for k,(current, item)  in enumerate(reversed(list(zip(chain, path)))):
        if k == 0 or len(current[item]) == 0:
            del(current[item])

    return dictionary
