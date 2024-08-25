import inspect
import types


def introspection_info(obj):
    
    obj_type = type(obj).__name__

    attributes = dir(obj)

    methods = [method for method in attributes if callable(getattr(obj, method))]

    module = inspect.getmodule(obj)

    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': module
    }

    
    return info


