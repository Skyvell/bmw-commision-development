from decimal import Decimal
    
def convert_floats_to_decimals(obj):
    """
    Recursively converts all float values to Decimal in supported objects.

    This function converts float values in an object to Decimal types. It is designed to work
    specifically with floats, dictionaries, and lists. The conversion is recursive for nested
    structures like dictionaries and lists. If an unsupported object type (like a custom class) is
    passed, it returns the object unchanged.

    Parameters:
    obj (float/dict/list/other): The object that potentially contains float values. The object can be
                                 a single float, a list, a dictionary, or any other type. In the case of
                                 other types, the object is returned as is without conversion.

    Returns:
    Decimal/dict/list/other: The input object with all float values converted to Decimal type for
                             supported object types. The type of the returned object matches the type
                             of the input obj, with floats converted in supported structures.
    """
    if isinstance(obj, float):
        return Decimal(str(obj))
    elif isinstance(obj, dict):
        return {k: convert_floats_to_decimals(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_floats_to_decimals(v) for v in obj]
    else:
        return obj