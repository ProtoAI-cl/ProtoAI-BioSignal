def get_content(file_name) -> str:
    file = open(file_name, "r")
    return file.read()
