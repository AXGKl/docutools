{'ef141587432d3b777a84d336a0c7a980': [{'cmd': {'cmd': 'foo () { echo bar; }'},
                                       'res': '$ foo () { echo bar; }'},
                                      {'cmd': {'cmd': 'cat << EOF > test.pyc\n'
                                                      'foo$(foo)baz\n'
                                                      'second_line\n'
                                                      'EOF'},
                                       'res': '$ cat << EOF > '
                                              'test.pyc                 \n'
                                              '> foo$(foo)baz      \n'
                                              '> second_line       \n'
                                              '> EOF               \n'
                                              '$ '},
                                      {'cmd': {'cmd': 'cat test.pyc | sed -z '
                                                      '"s/\\n/X/g" | grep '
                                                      "'foobarbazXsecond_line'"},
                                       'res': '$ cat test.pyc | sed -z '
                                              '"s/\\n/X/g" | grep '
                                              "'foobarbazXsecond_line'         \n"
                                              '\x1b[1m\x1b[31mfoobarbazXsecond_line\x1b[0m\x1b[39m\x1b[49mX'}]}