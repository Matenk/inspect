import inspect
import types


def introspection_info(obj):
    obj_type = type(obj)

    attributes = dir(obj)
    attrib = []
    method = []
    for attr in attributes:
        if callable(getattr(obj, attr)):
            method.append(attr)
        else:
            attrib.append(attr)






    module = inspect.getmodule(obj)

    info = {
        'type': obj_type,
        'attributes': attrib,
        'methods': method,
        'module': module,

    }

    return info


print(introspection_info(5))




