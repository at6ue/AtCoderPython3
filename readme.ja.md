[English](readme.md)

# AtCoderPython3

Python3 で AtCoder のコンテストに挑むための環境です。Visual Studio Code(VSCode) と Pipenv の使用を前提とします。

## Getting Started

このプロジェクトをクローンして、VSCode のワークスペースとして開きます。
`wip` ディレクトリ内に`foo.py`と`test_foo.py`を置くと unittest の対象となります。

コードテンプレートおよびテストケースの自動生成スクリプトを利用できます。

```
atcoder.py [-h] code alpha [url]
```

`python3 atcoder.py abc145 a` を実行すると、`wip` ディレクトリに`abc145_a.py`と`test_abc145_a.py`が生成されます。
`test_abc145_a.py`には AtCoder の[問題ページ](https://atcoder.jp/contests/abc145/tasks/abc145_a)から入力例と出力例を取得したテストケースが生成されます。  
問題ページの URL が`https://atcoder.jp/contests/code/tasks/code_alpha`で表されない場合、第 3 引数に問題ページの URL を加えると、指定された URL からテストケースが生成されます。

開催中のコンテストのテストケースを生成するには AtCoder へのログインが必要です。
`atcoder.ini`を作成し、以下の形式で認証情報を置いてください。

```
[login]
username = YOUR_USER_NAME
password = YOUR_PASSWORD
logout = True

[workspace]
wipdir = wip
```

`logout`が`True`のときは、スクリプトの終了時にログアウトします。
コードを`wip`ディレクトリ以外に生成したい場合は、`wipdir`に指定してください。

`_.py`と`test_.py`は、それぞれ提出コードとテストコードのひな形です。
コードは`import _ as task`以外は任意に書き換え可能です。
問題ページから取得したテストケースは`test_.py`内にある`# SAMPLES`と置き換えられます。

### Prerequisites

以下を予めインストールしておきます。

- [Python3.4.3](https://www.python.org/downloads/release/python-343/)
- [Pipenv](https://pipenv.kennethreitz.org/en/latest/install/#installing-pipenv)
- [Visual Studio Code](https://code.visualstudio.com/download/)

### Installing

プロジェクトのルートフォルダで以下を実行します。

```
pipenv install --dev
```

VSCode のワークスペースとして開くと、自動的に構成されます。

## Author

[atti](https://atcoder.jp/users/atti)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
