Title: Deploying my blog with Travis
Date: 2014-04-04 14:45:00
Slug: deploying-my-blog-with-travis
Tags: pelican, travis-ci, github-pages

I was curious about having my blog deployed whenever I push a commit, so after a bit of googling I found this [handy tutorial][1] by Mathieu Leplatre.

There were a few differences, I am using the GitHub user pages, where he was using a project page, so my blog output needs to sit on the `master` branch and not `gh-pages`.

I'll just show what I had to do differently, so here is my `.travis.yml` file. I had a few issues with it, but nothing [YAML lint][2] and [Travis WebLint][3] couldn't sort out.

    language: python
    python: 2.7
    env:
      global:
        secure: "my-encrypted-token (truncated for size)"
    branches:
      only:
        - source
    install:
      - "pip install -r requirements.txt"
    script:
      - "make publish github"

And my modified `Makefile`

    github: publish
        cp .travis.yml output/
        ghp-import -b master $(OUTPUTDIR)
        @git push -fq https://${GH_TOKEN}@github.com/$(TRAVIS_REPO_SLUG).git master > /dev/null

Key differences are the `-b master` parameter passed to `ghp-import` which tells it to update the master branch. I also copy my `.travis.yml` file to the output as it tells Travis only to build the `source` branch and I don't want it trying to `rake` my html.

You can see it all on my [GitHub page][4].

[1]: http://blog.mathieu-leplatre.info/publish-your-pelican-blog-on-github-pages-via-travis-ci.html "Mathieu Leplatre"
[2]: http://yamllint.com/ "YAML Lint"
[3]: http://lint.travis-ci.org/ "Travis WebLint"
[4]: https://github.com/AndyA13/AndyA13.github.io