{'4c1983f69f64940d425016f159689014': [], '39d75b9e7c5bf77cf0917cb01421b217': [{'cmd': 'echo "Hello World!"', 'res': '$ echo "Hello World!"                                 \nHello World!'}], 'ed9d4f5a23d0c4cecb298af92221a6a2': [{'cmd': 'ls -lta /etc | grep hosts', 'res': '$ ls -lta /etc | grep hosts\n-rw-r--r--. 1 root root       206 Aug  2 12:15 hosts'}, {'cmd': 'echo "Hello World!"      ', 'res': '$ echo "Hello World!"      \nHello World!'}], '7228e49bc88a91fb614305530ffaafa0': [{'cmd': 'say_hello () { \n    echo -e "Hello, from \\n"$(env | grep -i tmux)""; \n}', 'res': '$ say_hello () {    \n>     echo -e "Hello, from \\n"$(env | grep -i tmux)"";                          \n> }                 \n$ '}], '2ffda9d45e11c3f8b26224068a478a93': [{'cmd': 'echo $0 # lp: expect=bash', 'res': '$ echo $0           \n-bash               \n$'}, {'cmd': 'export -f say_hello', 'res': '$ export -f say_hello'}, {'cmd': '/bin/sh # lp: expect=', 'res': '$ /bin/sh           \n$'}, {'cmd': 'echo $0 # lp: expect=/bin/sh', 'res': '$ echo $0           \n/bin/sh             \n$'}, {'cmd': 'say_hello', 'res': '$ say_hello   \nHello, from         \nTMUX=/tmp/tmux-1000/default,1113980,591 TMUX_PANE=%591 BASH_FUNC_say_hello%%=() { echo -e "Hello, from                  \n"$(env | grep -i tmux)""'}, {'cmd': 'R="\\x1b["; r="${R}1;31m"', 'res': '$ R="\\x1b["; r="${R}1;31m"'}, {'cmd': 'echo -e "Means: We have\n- $r Cross block sessions  ${R}0m\n- $r Blocking commands     ${R}0m\n- and...${R}4m$r Full Ansi\n"', 'res': '$ echo -e "Means: We have               \n> - $r Cross block sessions  ${R}0m     \n> - $r Blocking commands     ${R}0m     \n> - and...${R}4m$r Full Ansi            \n> "                 \nMeans: We have      \n- \x1b[1m\x1b[31m Cross block sessions  \x1b[0m\x1b[39m\x1b[49m               \n- \x1b[1m\x1b[31m Blocking commands     \x1b[0m\x1b[39m\x1b[49m               \n- and...\x1b[1;4m\x1b[31m Full Ansi\x1b[0m\x1b[39m\x1b[49m  \n\n\x1b[1;4m\x1b[31m$ \x1b[0m\x1b[39m\x1b[49m             \n\x1b[1;4m\x1b[31m'}]}