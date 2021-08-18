# vim: ft=bash
M="\x1b[1;32m"
O="\x1b[0m"
T1="\x1b[48;5;255;38;5;0m"
T2="\x1b[48;5;124;38;5;255m"

TERMINAL="${TERMINAL:-st}"

nfo() { test -z "$2" && echo -e "${M}$*$O" || h1 "$@"; }
h1()  { local a="$1" && shift && echo -e "$T1 $a $T2 $* $O"; }
sh()  { nfo "$@" && "$@"; }

help() {
    funcs()   { local a="func" && grep "${a}tion" ./make | grep " {" | sed -e "s/${a}tion/- /g" | sed -e 's/{//g' | sort; }
    aliases() { local a="## Function" && grep -A 30 "$a Aliases:" ./make | grep -B 30 'make()' | grep -v make; }
    local doc="
    # Repo Maintenance Functions

    ## Usage: ./make <function> [args]

    ## Functions:
    $(funcs)

    $(aliases)
    "
    doc="$(echo "$doc" | sed -e 's/^    //g')"
    echo -e "$doc"
}

activate_venv() {
    # must be set in environ:
    test "$CONDA_PREFIX" = "${conda_env:-x}" && return 0
    nfo Activating "$conda_env"
    conda activate "$conda_env"
}

set_version() {
    if [ "${versioning:-}" = "calver" ]; then
        local M="$(date "+%m" | sed -e 's/0//g')"
        test -z "${1:-}" && {
            version="$(date "+%Y.$M.%d")"
            return 0
        }
    fi
    nfo "Say ./make release <version>"
    return 1
}

# ----------------------------------------------------------------------------------------- Make Functions:
function badges { # inserts badges into readme. defunct for now
    local u="hg+https://badges.github.com/scm/hg/noauth/badges::/tmp/badges_$USER"
    sh doc make_badges --badge_directory "$u" --modify_readme
}

function ci { # Trigger a CI Run by pushing and empty commit
    echo ' ' >> README.md
    sh git commit README.md -m "ci: trigger CI (empty commit)"
    sh git push
}

function clean {
    for i in .coverage .mypy_cache .pytest_cache build dist pip-wheel-metadata site public
    do
        sh rm -rf "$i"
    done
}

function coverage {
    mkdir -p build
    sh coverage report --rcfile=config/coverage.ini | tee build/coverage_report
    sh coverage html --rcfile=config/coverage.ini
}

function docs {
    docs_regen
    sh mkdocs build
}

function docs_regen {
    sh doc pre_process \
        --fail_on_blacklisted_words \
        --patch_mkdocs_filewatch_ign_lp \
        --gen_theme_link \
        --gen_last_modify_date \
        --gen_change_log \
        --gen_change_log_versioning_stanza="${versioning:-calver}" \
        --gen_credits_page \
        --gen_auto_docs \
        --lit_prog_evaluation="${lit_prog_eval_match:-md}" \
        --lit_prog_evaluation_timeout="${lit_prog_eval_match:-5}" \
        --lit_prog_on_err_keep_running=false || exit 1 # fail build on error
}

function docs_serve {
    docs_regen
    sh mkdocs serve
}

function tests {
    test -z "$1" && {
        sh pytest -xs tests -p no:randomly -c config/pytest.ini tests
        return $?
    }
    test -n "$1" && sh pytest "$@"
}

function release {
    version="${1:-}"
    test -z "$version" && { set_version || return 1; }
    nfo "New Version = $version"
    sh poetry version "$version"
    sh docs
    sh git add pyproject.toml -f CHANGELOG.md
    sh git commit -am "chore: Prepare release $version"
    sh git tag "$version"
    sh git push
    sh git push --tags
    sh mkdocs gh-deploy
}

## Function Aliases:
d()   { docs       "$@"; }
ds()  { docs_serve "$@"; }
rel() { release    "$@"; }
t()   { tests      "$@"; }

make() {
    test -z "$1" && {
        help
        return
    }
    local f="$1"
    type $f >/dev/null 2>/dev/null || {
        help
        return
    }
    shift
    $f "$@" || {
        nfo "ERR" $f
        return 1
    }
}

activate_venv || nfo "Cannot activate $\conda_env"