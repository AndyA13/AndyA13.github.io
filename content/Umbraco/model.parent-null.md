Title: Model.Parent == null
Date: 2012-08-29 21:52:48
Slug: model.parent-null
Tags: umbraco

Thought I would put up a quick post on an issue that I came across when converting my blog to Umbraco.

I have a macro that lists posts, it will show the normal page as well as the filtered pages for categories and tags.  While trying to get my tag filter to work I hit a strange issue.

    if (Model.Parent != null && Model.Parent.Id == 1234)

In the above if statement, Model.Parent was always null.

Parent should only be null if you are on the homepage, so I checked Model.Level and sure enough it was 1.

It took a bit of head scratching and some fruitless googling before I realized it was because the node I was loading was called "Blog", as was the root element of my site. Doh!

Quick rename of the tag (and the category as it would have suffered the same problem) and all was good in the world of Umbraco again.

I'm still not 100% sure on the rules of nodes with the same name. They seem to be fine if they are not direct descendants of one another.
