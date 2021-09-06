import json
import os

from lcdoc.mkdocs.tools import src_link
from lcdoc.tools import app, dirname, exists, now, os, read_file, require

fmt_default = 'mk_console'

T = '''
=== "Code"
    ```%(lang)s
    %(body)s
    ```
=== "%(src_link)s"
    %(url)s
'''

TM = '''
??? note "%(header)s"
    %(body)s
'''


def md(**kw):
    kw['body'] = kw['body'].replace('\n', '\n    ')
    return T % kw


def mdhide(**kw):
    M = md(**kw)
    kw['body'] = md(**kw).replace('\n', '\n    ')
    return TM % kw


def run(cmd, kw):
    require('rg --version')
    LP = kw['LP']
    delim = kw['delim']
    dir = kw['dir']
    if not dir[0] == '/':
        droot = os.path.dirname(LP.config['docs_dir'])
        dir = droot + '/' + dir
    if not exists(dir):
        return app.error('Not exists', dir=dir)
    expr = ':docs:%s' % delim
    cmd = 'rg "%s" %s --json --max-filesize 1M' % (expr, dir)
    rg = os.popen(cmd).read().strip()
    rg2 = [json.loads(l) for l in rg.splitlines()]
    j = [k for k in rg2 if k['type'] == 'begin']
    if len(j) == 0:
        return app.error('Expression not found', cmd=cmd, expr=delim)
    if len(j) != 1:
        return app.error('Expression not unique', cmd=cmd, found=len(j), expr=expr)
    fn = j[0]['data']['path']['text']
    s = read_file(fn).split(expr)
    if len(s) != 3:
        return app.error(
            'Expression not correct in file',
            cmd=cmd,
            found=len(j),
            expr=expr,
            fn=fn,
            matches_file=len(s),
        )
    line = len(s[0].splitlines())
    res = s[1].rsplit('\n', 1)[0]
    l = src_link(fn, LP.config, line=line + 1)
    h = kw.get('hide')
    if h == True:
        h = 'Implementation'
    f = mdhide if h else md
    return {
        'res': res,
        'formatted': f(
            header=h, lang=kw['lang'], body=res, src_link=l['link'], url=l['url']
        ),
    }
