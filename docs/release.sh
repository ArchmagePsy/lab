#!/usr/bin/env bash
[ -d ../site ] || mkdir ../site
cp -uvr build/html/* ../site
