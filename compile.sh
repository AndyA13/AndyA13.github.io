# Clear old output
rm -rf output

# Clear the theme and copy it back in
rm -rf themes/coffee-code

mkdir themes

# Copy theme in from working folder
cp -r ../pelican-theme ./themes/coffee-code

# Generate site
pelican -o output/ -s pelicanconf.py content/
