#!/usr/bin/env bash
#
# Run the main suite, testing all valid options and formats.

# get all our directories
script_dir=$(dirname "${BASH_SOURCE[0]}")
script_home=$(realpath "${script_dir}")
home=$(dirname "${script_home}")
rm -f "${home}/Results.md"

if [[ -z "${PYTHON}" ]]; then
    PYTHON="python"
fi
# shellcheck disable=SC2068
${PYTHON[@]} "${script_home}/format-validator.py" -d "${home}/data" -o "${home}/Results.md" -c "${home}/config.toml"
