def get_filename(smart_filename):
    validate_smart_filename(smart_filename)
    return os.path.join(
        os.path.dirname(__file__),
        *[
            ".." if path_element.startswith("..") else path_element
            for path_element in smart_filename.split(os.sep)
        ]
    )

def validate_smart_filename(smart_filename):
    directory = os.path.dirname(__file__)
    for path_element in smart_filename.split(os.sep):
        if path_element.startswith(".."):
            directory = os.path.join(directory, "..")
            if not os.path.exists(directory):
                raise IOError("No such directory: '%s'" % directory)
        else:
            directory = os.path.join(directory, path_element)
