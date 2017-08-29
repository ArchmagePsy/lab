#!/usr/bin/env bash

docs/make html
cp -uvr docs/build/html/* .
touch .nojekyll
git add --all
git commit -am "documentation updated at: $(date +\%d-\%m-\%Y)"
git push origin gh-pages
