#!/usr/bin/env bash
#
# Run the main suite, testing all valid options and formats.

set -ex

# get all our directories
script_dir=$(dirname "${BASH_SOURCE[0]}")
script_home=$(realpath "${script_dir}")
home=$(dirname "${script_home}")

src_dir="${home}/src"
target_dir="${home}/target"
mkdir -p "${target_dir}"

# list our toolchain versions
rustc --version
rustc "${src_dir}/rust.rs" -o "${target_dir}/rust"
"${target_dir}/rust"
