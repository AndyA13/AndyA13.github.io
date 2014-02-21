# compile first
./compile.sh

# export github pages to master branch
ghp-import -b master output

# push all branches to github
git push --all origin
