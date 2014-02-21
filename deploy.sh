# Update gh-pages branch

# compile first
./compile.sh

# import github pages
ghp-import output

# push to repo
git push git@github.com:AndyA13/AndyA13.github.io.git gh-pages:master
