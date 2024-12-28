def introspection_info(obj):

    obj_type = type(obj).__name__

    # Получаем атрибуты и методы объекта
    attributes = [attr for attr in dir(obj) if not attr.startswith('__')]
    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith('__')]

    # Получаем модуль, к которому принадлежит объект
    module = getattr(obj, '__module__', '__main__')

    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': module
    }

    return info


number_info = introspection_info(42)
print(number_info)

string_info = introspection_info("лорд")
print(string_info)

list_info = introspection_info([1, 2, 3])
print(list_info)