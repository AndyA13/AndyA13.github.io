Title: Caching file contents with CacheDependency
Date: 2011-04-18 21:02:20
Category: .net
Tags: caching, .net
Slug: caching-file-contents-with-cachedependency

The CacheDependency will monitor a file or folder for changes. When it detects a change it will remove the associated key from the cache.

This comes in quite handy for my hangman game which stores the film titles in an xml file.

Below is how I cache the data and setup the CacheDependency. Some validation has been removed to keep it clear.

    private HangmanGameCollection ReadGameFile()
    {
        if (HttpRuntime.Cache["HangmanGame"] != null)
        {
            return (HangmanGameCollection)HttpRuntime.Cache["HangmanGame"];
        }

        HangmanGameCollection hangmanGames;

        FileInfo xmlFile = new FileInfo(Server.MapPath("~/TopSecret.xml"));

        XmlSerializer xmlSerializer = new XmlSerializer(typeof(HangmanGameCollection));

        using (FileStream fileStream = xmlFile.OpenRead())
        {
            hangmanGames = (HangmanGameCollection)xmlSerializer.Deserialize(fileStream);

            // Put it in cache with a dependency on the xml file
            HttpRuntime.Cache.Insert("HangmanGame", hangmanGames, new CacheDependency(xmlFile.FullName));
        }

        return hangmanGames;
    }

Should maybe do something about fitting in long lines of code :\
