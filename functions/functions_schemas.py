schema_get_files_info: dict = {

    "type": "function",
    "function": {

        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {

            "type": "object",
            "properties": {

                "directory": {

                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)"
                }
            }
        }
    }
}

schema_get_file_content: dict = {

    "type": "function",
    "function": {

        "name": "get_file_content",
        "description": "Returns the contents of a file in a specified path relative to the working directory, in a string form.",
        "parameters": {

            "type": "object",
            "properties": {

                "file_path": {

                    "type": "string",
                    "description": "Path of the file to return the string from, relative to the working directory (default is the working directory itself)"
                }
            }
        }
    }
}

schema_write_file: dict = {

    "type": "function",
    "function": {

        "name": "write_file",
        "description": "Writes content to a specified file given the file path, relative to the working directory. If the file does not exit, the function creates the file with the specified content and if the file exists, the function overrides the current content",
        "parameters": {

            "type": "object",
            "properties": {

                "file_path": {

                    "type": "string",
                    "description": "Path of the file to write the content to, relative to the working directory (default is the working directory itself)"
                },

                "content": {

                    "type": "string",
                    "description": "Content in a string format that will be written in the specified file"
                }
            }
        }
    }
}

schema_run_python_file: dict = {

    "type": "function",
    "function": {

        "name": "run_python_file",
        "description": "Executes a python file from a specified path, relative to the working directory. The extension of the file should be '.py', anything else should return an error message.",
        "parameters": {

            "type": "object",
            "properties": {

                "file_path": {

                    "type": "string",
                    "description": "Path of the file to be executed. The path is relative to the working directory (default is the working directory itself)"
                },

                "args": {

                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "An optional array of arguments that will be considered when executing the python file."
                }
            }
        }
    }
}

