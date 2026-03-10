---
title: "Deploying my blog with Travis"
description: "Setting up Travis CI to automatically deploy a Pelican blog to GitHub Pages on every push."
pubDate: 2014-04-04
tags: ["pelican", "travis-ci", "github-pages"]
---

I was curious about having my blog deployed whenever I push a commit, so after a bit of googling I found this [handy tutorial](http://blog.mathieu-leplatre.info/publish-your-pelican-blog-on-github-pages-via-travis-ci.html "Mathieu Leplatre") by Mathieu Leplatre.

There were a few differences, I am using the GitHub user pages, where he was using a project page, so my blog output needs to sit on the `master` branch and not `gh-pages`.

I'll just show what I had to do differently, so here is my `.travis.yml` file. I had a few issues with it, but nothing [YAML lint](http://yamllint.com/ "YAML Lint") and [Travis WebLint](http://lint.travis-ci.org/ "Travis WebLint") couldn't sort out.

```yaml
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
```

And my modified `Makefile`

```makefile
github: publish
    cp .travis.yml output/
    ghp-import -b master $(OUTPUTDIR)
    @git push -fq https://${GH_TOKEN}@github.com/$(TRAVIS_REPO_SLUG).git master > /dev/null
```

Key differences are the `-b master` parameter passed to `ghp-import` which tells it to update the master branch. I also copy my `.travis.yml` file to the output as it tells Travis only to build the `source` branch and I don't want it trying to `rake` my html.

You can see it all on my [GitHub page](https://github.com/AndyA13/AndyA13.github.io).
