import os
import sys
import time

from lcdoc.mkdocs.tools import srcref


def lp_plugins_descr(**kw):
    from lcdoc.tools import read_file, dirname

    d = dirname(kw['page'].file.abs_src_path)
    r = ['']
    for k in os.listdir(d):
        fn = d + '/' + k + '/index.md'
        if not os.path.exists(fn):
            continue
        k1 = k
        s = read_file(fn).strip().split('\n', 1)[1].strip().split('\n', 1)[0]
        if s:
            s = ': ' + s
        r.append('- [`%s`](./%s/index.md)%s' % (k1, k1, s))
    r.append('')
    return '\n'.join(r)


table = {
    'ctime': time.strftime('%a, %d %b %Y %Hh GMT', time.localtime()),
    'srcref': srcref,
    # only prevents the editor from going crazy, with nested code examples in nested code:
    'fences:all:': '```',
    'lp_plugins_descr': lp_plugins_descr,
}
