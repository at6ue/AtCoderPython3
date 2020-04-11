[日本語](readme.ja.md)

# AtCoderPython3

The Python3 environment for AtCoder contests with Pipenv and Visual Studio Code(VSCode).

## Getting Started

Just clone this project and open as a workspace on VSCode.
Unittest will discovers `test_foo.py` test code for `foo.py` in the `wip` directory.

Auto generation script for code template and test case is available.

```
atcoder.py [-h] code alpha [url]
```

Run `python3 atcoder.py abc145 a` then the script fetches the [contest task](https://atcoder.jp/contests/abc145/tasks/abc145_a)'s example inputs & outputs and generates `abc145_a.py` and `test_abc145_a.py` with testcases into the `wip` directory.  
Add the url as the third argument if the task page is not represented by `https://atcoder.jp/contests/code/tasks/code_alpha`. The script fetches the page on the designated url.

To fetch tasks on the ongoing contest, put your authentication information into `atcoder.ini` as follows,

```
[login]
username = YOUR_USER_NAME
password = YOUR_PASSWORD
logout = True

[workspace]
wipdir = wip
```

If `logout` is `True`, the script logouts from AtCoder before terminate.
Put your directory name on `wipdir` to change where codes generated.

`_.py` and `test_.py` are the templates for submission and unittest respectively.
You can modify the codes except `import _ as task`.
`# SAMPLES` in `test_.py` works as the placeholder for the fetched testcases.

### Prerequisites

This project requires,

- [Python3.4.3](https://www.python.org/downloads/release/python-343/)
- [Pipenv](https://pipenv.kennethreitz.org/en/latest/install/#installing-pipenv)
- [Visual Studio Code](https://code.visualstudio.com/download/)

Set `true` to the environment variable `PIPENV_VENV_IN_PROJECT`.

### Installing

Run following command in the project root directory,

```
pipenv install --dev
```

Open the prject directory as a workspace on VSCode, then the environment will be automatically configured.

## Author

[atti](https://atcoder.jp/users/atti)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details
