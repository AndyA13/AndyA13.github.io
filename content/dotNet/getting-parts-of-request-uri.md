Title: Getting parts of a Uri
Date: 2015-05-21 14:00:00
Slug: getting-parts-of-request-uri
Category: .net
Tags: c#

One thing that keeps coming up, but not enough for me to actually remember what I learnt last time, is how to get different parts of a request [Uri][1]

So I made a little [console app][2] that outputs the different parts from two example Uris.

Behold

    Uri Properties:
    
    Using          : https://www.example.com/folder/page.aspx?query=1&sample=2#anchor
    AbsolutePath   : /folder/page.aspx
    AbsoluteUri    : https://www.example.com/folder/page.aspx?query=1&sample=2#anchor
    Authority      : www.example.com
    DnsSafeHost    : www.example.com
    Fragment       : #anchor
    Host           : www.example.com
    HostNameType   : Dns
    IsAbsoluteUri  : True
    IsDefaultPort  : True
    IsFile         : False
    IsLoopback     : False
    IsUnc          : False
    LocalPath      : /folder/page.aspx
    OriginalString : https://www.example.com/folder/page.aspx?query=1&sample=2#anchor
    PathAndQuery   : /folder/page.aspx?query=1&sample=2
    Port           : 443
    Query          : ?query=1&sample=2
    Scheme         : https
    Segments       : /, folder/, page.aspx
    UserEscaped    : False
    UserInfo       : 
    
    Using          : http://www.example.com/folder
    AbsolutePath   : /folder
    AbsoluteUri    : http://www.example.com/folder
    Authority      : www.example.com
    DnsSafeHost    : www.example.com
    Fragment       : 
    Host           : www.example.com
    HostNameType   : Dns
    IsAbsoluteUri  : True
    IsDefaultPort  : True
    IsFile         : False
    IsLoopback     : False
    IsUnc          : False
    LocalPath      : /folder
    OriginalString : http://www.example.com/folder
    PathAndQuery   : /folder
    Port           : 80
    Query          : 
    Scheme         : http
    Segments       : /, folder
    UserEscaped    : False
    UserInfo       : 
    
    Uri.GetLeftPart(UriPartial part)
    
    Using                : https://www.example.com/folder/page.aspx?query=1&sample=2#anchor
    UriPartial.Authority : https://www.example.com
    UriPartial.Path      : https://www.example.com/folder/page.aspx
    UriPartial.Query     : https://www.example.com/folder/page.aspx?query=1&sample=2
    UriPartial.Scheme    : https://
    
    Using                : http://www.example.com/folder
    UriPartial.Authority : http://www.example.com
    UriPartial.Path      : http://www.example.com/folder
    UriPartial.Query     : http://www.example.com/folder
    UriPartial.Scheme    : http://


[1]: https://msdn.microsoft.com/en-us/library/system.uri%28v=vs.110%29.aspx "MSDN"
[2]: https://gist.github.com/AndyA13/147f079cf7d69c55038d "gist.github.com"