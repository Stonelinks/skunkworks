#!/bin/bash
# set -ex

if [ "$0" = "$BASH_SOURCE" ]; then
	echo "This script must be sourced, not executed."
	exit 1
fi

# https://go.dev/doc/devel/release
export GO_VERSION=1.25.4

# https://devguide.python.org/versions/
export PYTHON_VERSION=3.12.12

# https://github.com/astral-sh/uv/releases
export UV_VERSION=0.9.10

# https://nodejs.org/en/about/previous-releases
export NODE_VERSION=24.11.1

# https://github.com/oven-sh/bun/releases
export BUN_VERSION=1.3.2

# KEEP THESE IN SYNC
# https://github.com/mostlygeek/llama-swap/pkgs/container/llama-swap
export LLAMA_SWAP_VERSION_PREFIX=v178
# https://github.com/mostlygeek/llama-swap/releases
export LLAMA_SWAP_SHA=565c44766db9cdcaa0f3e61d0a60c44884b95d62

# https://github.com/ggml-org/llama.cpp/releases?q=b7524&expanded=true
export LLAMACPP_SERVER_VERSION=b7524
export LLAMACPP_SHA=5ee4e43f2629fc88c3c3ff428a47ffb842fa8d84
