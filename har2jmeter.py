#!/usr/bin/env python
# coding=UTF-8
import os
import sys, json, codecs, re

from jinja2 import Environment, FileSystemLoader


def har2jmeter(harfile):
    hardata = codecs.open(harfile, 'r', 'utf-8').read()
    har = json.loads(hardata)
    harentries = har['log']['entries']

    urls = [urlparts(entry['request']) for entry in harentries]
    urls = [url for url in urls if not url is None]
    templates_dir = os.path.join(sys.exec_prefix, 'templates')
    env = Environment(loader=FileSystemLoader(templates_dir))
    template = env.get_template('jmeter.jinja')

    print(template.render(urls=urls))

def urlparts(harrequest):
    host_arr = [h['value'] for h in harrequest['headers'] if ('name' in h and h['name'] == 'Host')]
    if len(host_arr) == 1:
        host = host_arr[0]
    else:
        return None
    url = harrequest['url']
    get_parts = url.split('?')
    if len(get_parts) > 1:
        url = get_parts[0]
        params = dict([p.split('=') for p in get_parts[1].split("&")])
    else:
        params = {}
    pathstart = re.search(host, url).end()
    path = url[pathstart:]
    return {'url': url, 'host': host, 'path': path, 'params': params}

if __name__ == '__main__':
    fname = sys.argv[1]
    har2jmeter(fname)
