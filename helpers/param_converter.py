def convert_params(params: dict) -> dict:
    """Convert parameter values to their most appropriate type."""
    converted = {}
    for key, value in params.items():
        value = value[0]
        if value.isdigit():
            converted[key] = int(value)
        elif value.lower() in ["true", "false"]:
            converted[key] = value.lower() == "true"
        else:
            converted[key] = value
    return converted
