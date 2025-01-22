#!/usr/bin/env bash
#
# Run the main suite, testing all valid options and formats.

set -ex

# get all our directories
script_dir=$(dirname "${BASH_SOURCE[0]}")
script_home=$(realpath "${script_dir}")
home=$(dirname "${script_home}")

if [[ -z "${PYTHON}" ]]; then
    PYTHON="python"
fi
# shellcheck disable=SC2068
${PYTHON[@]} "${script_home}/format-validator.py" -d "${home}/data" -o "Results.md"
