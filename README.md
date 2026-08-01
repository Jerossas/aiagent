# Toy version of an AI Agent like Claude Clode or Cursor Agentic mode

> I don't encourage anyone to use this toy agent as-is, because is very unsafe. This is more like a practice thing. If you are curious and want to use it, please be careful on giving sensitive access to the "agent"

## What do you need to use it? :V

- You need to clone the repository (^///^)
- You need to have installed **uv** python project manager to create the virtual environment and run the script. You can install it from here **[uv installation page](https://docs.astral.sh/uv/getting-started/installation/#standalone-installer)**

Whit *uv* installed, you need to create the virtual environment using `uv venv` command. Then you need to activate the virtual enviroment with `source .venv/bin/activate` command.

## How to use it

Currently, the "agent" can call 4 tool functions:

- get_file_content
- get_files_info
- run_python_file
- write_file

With these 4 functions, we can do a lot of things. We try to limit the "agent" access by specifying a working directory. The working directory is hard-coded and you can change it in the `call_function.py` file.

To run the `main.py` script, you do as follow:

`uv run main.py "your prompt"`

You can add a **--verbose** flag before or after the prompt and it will show you the token usage from the LLM provider.

`uv run main.py "your prompt" --verbose`

Annnnnnd, that is it. Hats of to **[@bootdotdev](https://github.com/bootdotdev)**
