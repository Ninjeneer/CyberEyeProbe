def safe_dict_value(key: str, dict: str):
    return dict[key] if key in dict else None