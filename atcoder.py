# coding: utf-8
import argparse
import configparser
import os
import re
import shutil

import requests


def login(session, username: str, password: str):
    login_url = 'https://atcoder.jp/login'
    res = session.get(login_url)

    csrf_token, = re.search(
        r'var csrfToken = "(.+?)"',
        res.text,
        flags=(re.MULTILINE | re.DOTALL)
    ).groups()

    session.post(login_url, data={
        'csrf_token': csrf_token,
        'username': username,
        'password': password
    }).raise_for_status()

    return csrf_token


def get_samples(task_page: str) -> tuple:
    hooks = (
        ('入力例', '出力例'),
        ('Sample Input', 'Sample Output')
    )

    ret = None
    for i, o in hooks:
        if re.search(i, task_page, flags=re.MULTILINE):
            pat = r'<h3>{}\s*?[1-9]</h3>.*?<pre.*?>(.+?)</pre>'
            ret = tuple(zip(
                map(lambda x: tuple(x.strip().splitlines()), re.findall(
                    pat.format(i), task_page, flags=(re.MULTILINE | re.DOTALL)
                )),
                map(lambda x: x.replace('\r\n', '\n').strip(), re.findall(
                    pat.format(o), task_page, flags=(re.MULTILINE | re.DOTALL)
                ))
            ))
            break
    return ret


def modify(name: str, test: str, samples: tuple) -> str:

    head, indent, tail = re.search(
        r'(.*)^(\s*?)# SAMPLES\s*?$(.*)',
        test,
        flags=(re.MULTILINE | re.DOTALL)
    ).groups()

    ret = re.sub(
        r'^(import )_( as task$)',
        r'\1{}\2'.format(name),
        head,
        flags=re.MULTILINE
    )
    ret += ',\n'.join(map(lambda x: indent+str(x), samples))
    ret += tail

    return ret


def snake(text: str):
    return text.replace('-', '_')


def main(code: str, alpha: str, url: str = '',
         username: str = '', password: str = '', logout: bool = False,
         wipdir: str = ''):

    session = requests.session()
    session.cookies.clear()

    csrf_token = ''
    if username and password:
        csrf_token = login(session, username, password)

    if not url:
        url = 'https://atcoder.jp/contests/{c}/tasks/{cs}_{a}'.format(
            c=code, cs=snake(code), a=alpha
        )
    res = session.get(url)
    samples = get_samples(res.text)

    if logout:
        session.post('https://atcoder.jp/logout', data={
            'csrf_token': csrf_token
        }).raise_for_status()
        session.cookies.clear()

    if not samples:
        print('No test cases found. Just copy templates? (Y/n)')
        if input().lower() != 'y':
            return
        samples = tuple()

    with open('test_.py', 'r') as temp:
        test = temp.read()

    name = '{}_{}'.format(code, alpha)

    new_test = modify(name, test, samples)
    with open(os.path.join(wipdir, 'test_{}.py'.format(name)), 'w') as o:
        o.write(new_test)

    shutil.copyfile('_.py', os.path.join(wipdir, '{}.py'.format(name)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('code', type=str)
    parser.add_argument('alpha', type=str)
    parser.add_argument('url', nargs='?', type=str, default='')
    args = parser.parse_args()

    code, alpha, url = args.code, args.alpha, args.url

    config_file = 'atcoder.ini'
    if os.path.exists(config_file):
        config = configparser.ConfigParser()
        config.read(config_file)

        login_sec = config['login']
        username = login_sec.get('username')
        password = login_sec.get('password')
        logout = login_sec.getboolean('logout', fallback=False)

        workspace_sec = config['workspace']
        wipdir = workspace_sec.get('wipdir', fallback='')

    filename = '{}_{}.py'.format(snake(code), alpha)
    if os.path.exists(os.path.join(wipdir, filename)) or \
            os.path.exists(os.path.join(wipdir, 'test_{}'.format(filename))):
        print('File exists. Overwrite? (y/N)')
        if input().lower() != 'y':
            exit()

    main(code, alpha, url, username, password, logout, wipdir)

    print('Done')
