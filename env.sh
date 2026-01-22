#!/bin/bash
# set -ex

if [ -f versions.sh ]; then
	source versions.sh
fi

if [ "$0" = "$BASH_SOURCE" ]; then
	echo "This script must be sourced, not executed."
	exit 1
fi

PROJECT_ROOT=$(pwd)
export PROJECT_ROOT

export PROJECT_NAME=skunkworks

if [ -z "$DEPLOY_PREFIX" ]; then
	export DEPLOY_PREFIX="$HOME"
fi

export HOMEDIR_STORE=$DEPLOY_PREFIX/.$PROJECT_NAME
export THIRD_PARTY_DIR=$HOMEDIR_STORE/3rdparty

export OPT_DIR=$HOMEDIR_STORE/opt

# echo "Using DEPLOY_PREFIX=$DEPLOY_PREFIX"
# echo "Using HOMEDIR_STORE=$HOMEDIR_STORE"
# echo "Using THIRD_PARTY_DIR=$THIRD_PARTY_DIR"
# echo "Using OPT_DIR=$OPT_DIR"

# Figure out what OS we're running.
case $(uname -s) in
Darwin) OS=darwin ;;
Linux) OS=linux ;;
*)
	echo "Unsupported OS $(uname -s)"
	exit 1
	;;
esac

export OS

# Figure out what Arch
ARCH=$(uname -m)
case $ARCH in
x86_64) ARCH=x64 ;;
aarch64) ARCH=arm64 ;;
esac

export ARCH

# Go

# Add go to PATH and configure GOROOT and GOPATH.
export GOROOT=$OPT_DIR/goroot
PATH=$GOROOT/bin:$PATH

export GOPATH=$OPT_DIR/go
if [ ! -d $GOPATH ]; then
	mkdir -p $GOPATH
fi

PATH=$PATH:$GOPATH/bin

# python
export UV_UNMANAGED_INSTALL=$OPT_DIR/uv-$UV_VERSION
export UV_PYTHON_INSTALL_DIR=$OPT_DIR/python
export UV_LINK_MODE=copy
export UV_NO_CACHE=true
export UV_PYTHON_PREFERENCE=only-managed

PATH=$UV_UNMANAGED_INSTALL:$PATH

export VIRTUAL_ENV=$OPT_DIR/venv

# if the venv exists...
if [ -d $VIRTUAL_ENV ]; then
	PATH=$VIRTUAL_ENV/bin:$PATH
	source $VIRTUAL_ENV/bin/activate
fi

# local site-packages
LOCAL_SITE_PACKAGES=$VIRTUAL_ENV/lib/python$PY_VERSION_MAJOR.$PY_VERSION_MINOR/site-packages

PYTHONPATH=$LOCAL_SITE_PACKAGES:$PYTHONPATH

# local python source
PYTHONPATH=$PROJECT_ROOT:$PYTHONPATH
export PYTHONPATH

# check if python is in the path, and its the one in the venv
if [ "$(which python)" != "$VIRTUAL_ENV/bin/python" ]; then
	echo "WARNING: Python not in path, or not the one in the venv"
fi

# Node
PATH=$OPT_DIR/node$NODE_VERSION/bin:$PATH

# bun

export BUN_INSTALL="$OPT_DIR/bun"
PATH=$BUN_INSTALL/bin:$PATH

PATH=$PROJECT_ROOT/node_modules/.bin:$PATH

chmod +x $PROJECT_ROOT/bin/*
PATH=$PROJECT_ROOT/bin:$PATH
export PATH

if [ -f secrets.sh ]; then
	source secrets.sh
fi
