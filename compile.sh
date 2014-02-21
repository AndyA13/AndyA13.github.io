# Clear old output
rm -r ./output/*

# Clear the theme and copy it back in
rm -rf ./themes/coffee-code

cp -r ../pelican-theme ./themes/coffee-code

# Generate site
pelican -o output/ -s pelicanconf.py content/
