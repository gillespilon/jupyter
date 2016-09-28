#! /bin/sh

extensions=+auto_identifiers
#extensions=$extensions-markdown_in_html_blocks
mathjax_cdn='http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML'

find -type f -name '*.mkd' \
  | while read mkd; do
        html="${mkd%%.mkd}.html"
        if ! [ -f "$html" ] || [ "$mkd" -nt "$html" ]; then
            printf "Updating \x1b[1;33m'%s'\x1b[0m..." "$html"
            if pandoc --standalone \
                      --smart \
                      --include-in-header="$(dirname   "$0")/template_header.html" \
                      --include-before-body="$(dirname "$0")/template_prebody.mkd" \
                      --mathjax="$mathjax_cdn" \
                      --from markdown$extensions \
                      --to html5 \
                      "$mkd" \
                 | python "$(dirname "$0")/preprocess.py" \
                 > "$html"; then
                printf ' \x1b[32mdone\x1b[0m.\n'
            else
                printf ' \x1b[31mfailed\x1b[0m.\n'
            fi
        fi
    done
