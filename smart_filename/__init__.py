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

def read(smart_filename):
    file_path_relative_to_project_root = get_filename(smart_filename)
    smart_filename_directory = path.dirname(__file__)
    project_root = path.join(analytricks_common, "..")
    file_path_relative_to_working_directory = path.join(
        project_root,
        file_path_relative_to_project_root,
    )
    with open(file_path_relative_to_working_directory) as f:
        return f.read()
