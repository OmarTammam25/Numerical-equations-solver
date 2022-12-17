import sys


PY3 = sys.version_info >= (3, 0)
if PY3:  # pragma: PY3
    import builtins
    class_types = type,
    string_types = (str, bytes)
    unicode = str
else:  # pragma: PY2
    import __builtin__ as builtins  # noqa: F401 import unused
    from types import ClassType
    class_types = (type, ClassType)
    string_types = basestring,  # noqa: F821 undefined name 'basestring'
    unicode = unicode
