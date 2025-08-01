#!/bin/bash
set -e

sudo apt-get update
sudo apt-get install -y \
    build-essential cmake ca-certificates curl pkg-config git libssl-dev

export LANG=C.UTF-8
export DEBIAN_FRONTEND=noninteractive
export TARGETARCH=$(uname -m)
export TARGETVARIANT=""

[ "$TARGETARCH" = "x86_64" ] && TARGETARCH=amd64

mkdir -p build install
cmake -Bbuild -DCMAKE_INSTALL_PREFIX=install
cmake --build build --config Release
cmake --install build

./build/piper_phonemize --help

mkdir -p tmp
cp -r ./install tmp/piper_phonemize

cd tmp
tar -czf "piper-phonemize_${TARGETARCH}${TARGETVARIANT}.tar.gz" piper_phonemize
cd ..
