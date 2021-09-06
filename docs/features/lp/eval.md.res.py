{'2a92bc680d958a454e1e75f05e6b7503': {'res': "\n# those header params will prevent to use caching when changed, they go into the hash of\n# a block which is the cache key:\nhashed_headers = [\n    'asserts',\n    'cwd',\n    'expect',\n    'mode',\n    'new_session',\n    'pdb',\n    'post',\n    'pre',\n    'session',\n    'timeout',\n]", 'formatted': '\n=== "Code"\n    ```python\n    \n    # those header params will prevent to use caching when changed, they go into the hash of\n    # a block which is the cache key:\n    hashed_headers = [\n        \'asserts\',\n        \'cwd\',\n        \'expect\',\n        \'mode\',\n        \'new_session\',\n        \'pdb\',\n        \'post\',\n        \'pre\',\n        \'session\',\n        \'timeout\',\n    ]\n    ```\n=== "[:fontawesome-brands-git-alt:](https://github.com/AXGKl/docutools/blob/master/src/lcdoc/mkdocs/lp/__init__.py#L30)"\n    https://github.com/AXGKl/docutools/blob/master/src/lcdoc/mkdocs/lp/__init__.py#L30\n'}, '2a92bc680d958a454e1e75f05e6b7503_': {'res': '\ndef patch_mkdocs_to_ignore_res_file_changes():\n    """sad. we must prevent mkdocs serve to rebuild each time we write a result file\n    And we want those result files close to the docs, they should be in that tree.\n    """\n    import mkdocs\n\n    fn = mkdocs.__file__.rsplit(\'/\', 1)[0]\n    fn += \'/livereload/__init__.py\'\n\n    if not exists(fn):\n        return app.warn(\'Cannot patch mkdocs - version mismatch\', missing=fn)\n\n    s = read_file(fn)\n    S = \'event.is_directory\'\n    if not S in s:\n        return app.warning(\'Cannot patch mkdocs - version mismatch\', missing=fn)\n    k = "\'%s\'" % lp_res_ext\n    if k in s:\n        return app.info(\'mkdocs is already patched to ignore %s\' % k, fn=fn)\n    os.system(\'cp "%s" "%s.orig"\' % (fn, fn))\n    new = S + \' or event.src_path.endswith(%s)\' % k\n    s = s.replace(S, new)\n    write_file(fn, s)\n    diff = os.popen(\'diff "%s.orig" "%s"\' % (fn, fn)).read().splitlines()\n    app.info(\'Diff\', json=diff)\n    msg = \'Have patched mkdocs to not watch %s  files. Please restart.\' % k\n    return app.die(msg, fn=fn)\n\n', 'formatted': '\n??? note "implementation"\n    \n    === "Code"\n        ```python\n        \n        def patch_mkdocs_to_ignore_res_file_changes():\n            """sad. we must prevent mkdocs serve to rebuild each time we write a result file\n            And we want those result files close to the docs, they should be in that tree.\n            """\n            import mkdocs\n        \n            fn = mkdocs.__file__.rsplit(\'/\', 1)[0]\n            fn += \'/livereload/__init__.py\'\n        \n            if not exists(fn):\n                return app.warn(\'Cannot patch mkdocs - version mismatch\', missing=fn)\n        \n            s = read_file(fn)\n            S = \'event.is_directory\'\n            if not S in s:\n                return app.warning(\'Cannot patch mkdocs - version mismatch\', missing=fn)\n            k = "\'%s\'" % lp_res_ext\n            if k in s:\n                return app.info(\'mkdocs is already patched to ignore %s\' % k, fn=fn)\n            os.system(\'cp "%s" "%s.orig"\' % (fn, fn))\n            new = S + \' or event.src_path.endswith(%s)\' % k\n            s = s.replace(S, new)\n            write_file(fn, s)\n            diff = os.popen(\'diff "%s.orig" "%s"\' % (fn, fn)).read().splitlines()\n            app.info(\'Diff\', json=diff)\n            msg = \'Have patched mkdocs to not watch %s  files. Please restart.\' % k\n            return app.die(msg, fn=fn)\n        \n        \n        ```\n    === "[:fontawesome-brands-git-alt:](https://github.com/AXGKl/docutools/blob/master/src/lcdoc/mkdocs/lp/__init__.py#L511)"\n        https://github.com/AXGKl/docutools/blob/master/src/lcdoc/mkdocs/lp/__init__.py#L511\n    \n'}, '2a92bc680d958a454e1e75f05e6b7503__': {'res': "\nclass Eval:\n    never = 'never'  # not even when not cached\n    always = 'always'  # even when cached. except skipped\n    on_change = 'on_change'  # only when block changed\n    on_page_change = 'on_page_change'  # whan any block (md irrelevant) on page changed\n    # Default: anything else would confuse user. e.g. cat <filename> would show old still when it changed but no lp change involved:\n    default = 'always'\n\n", 'formatted': '\n=== "Code"\n    ```python\n    \n    class Eval:\n        never = \'never\'  # not even when not cached\n        always = \'always\'  # even when cached. except skipped\n        on_change = \'on_change\'  # only when block changed\n        on_page_change = \'on_page_change\'  # whan any block (md irrelevant) on page changed\n        # Default: anything else would confuse user. e.g. cat <filename> would show old still when it changed but no lp change involved:\n        default = \'always\'\n    \n    \n    ```\n=== "[:fontawesome-brands-git-alt:](https://github.com/AXGKl/docutools/blob/master/src/lcdoc/mkdocs/lp/__init__.py#L51)"\n    https://github.com/AXGKl/docutools/blob/master/src/lcdoc/mkdocs/lp/__init__.py#L51\n'}}