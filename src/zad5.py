def flatten_list(nested_list: list) -> list:
    result = []
    for element in nested_list:
        if isinstance(element, list):
            result.extend(element)
        else:
            result.append(element)
    return result
