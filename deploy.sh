# Generate site
pelican -o output/ -s pelicanconf.py content/

# copy travis config to site to prevent ci build of master
cp .travis.yml output/

# export github pages to master branch
ghp-import -b master output

# push all branches to github
git push --all origin
