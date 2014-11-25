Title: Warning - ExtensionAttribute is defined in multiple assemblies
Date: 2014-11-25 13:30:00
Slug: warning-extensionattribute-defined-multiple-assemblies
Category: .net
Tags: .net, lucene

I've noticed a warning in Visual Studio in a few projects where it gives me the following warning after building,

    The predefined type "System.Runtime.CompilerServices.ExtensionAttribute" is defined in multiple assemblies in the global alias

I don't like leaving warnings in my build but I didn't have time to look into it until today.  [This handy tip][1] from Remco te Wierik led me to the root of the issue. The .net [Lucene contrib nuget package][2] contains a reference Lucene.Net.FastVectorHighlighter which defines an `ExtensionAttribute` class in the `System.Runtime.CompilerServices` namespace.

Updating the assembly reference `alias` from "global" to a custom one, fixed the warning.

[1]: http://stackoverflow.com/a/6518336/175394 "stackoverflow.com"
[2]: https://www.nuget.org/packages/Lucene.Net.Contrib/2.9.4.1 "Nuget: Lucene.Contrib"