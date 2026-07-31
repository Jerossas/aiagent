import os
import subprocess


def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:
    
    try:

        abs_working_dir = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(abs_working_dir, file_path))

        if os.path.commonpath([abs_working_dir, target_path]) != abs_working_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_path):
            return f'Error: \"{file_path}\" does not exist or is not a regular file'

        if not file_path.endswith(".py"):
            return f"Error: \"{file_path}\" is not a Python file"

        command: list = ["python", target_path]

        if args != None:
            command.extend(args)

        completed_process = subprocess.run(command, capture_output=True, text=True, timeout=30, cwd=abs_working_dir)

        output_string: str = ""

        if completed_process.returncode != 0:
            output_string += f"Process exited with code {completed_process.returncode}"

        if completed_process.stdout == None and completed_process.stderr == None:
            output_string += "No output produced"
        else:
            output_string += f"STDOUT: {completed_process.stdout}STDERR: {completed_process.stderr}"

        return output_string

        
    except Exception as e:
        print(f"Error: executing Python file: {e}")
