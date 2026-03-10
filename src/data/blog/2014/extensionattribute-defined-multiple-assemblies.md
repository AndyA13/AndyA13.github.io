---
title: "Warning - ExtensionAttribute is defined in multiple assemblies"
description: "Fixing a Visual Studio build warning caused by Lucene.Net defining ExtensionAttribute in the System.Runtime.CompilerServices namespace."
pubDate: 2014-11-25
tags: [".net", "lucene"]
---

I've noticed a warning in Visual Studio in a few projects where it gives me the following warning after building,

```
The predefined type "System.Runtime.CompilerServices.ExtensionAttribute" is defined in multiple assemblies in the global alias
```

I don't like leaving warnings in my build but I didn't have time to look into it until today.  [This handy tip](http://stackoverflow.com/a/6518336/175394 "stackoverflow.com") from Remco te Wierik led me to the root of the issue. The .net [Lucene contrib nuget package](https://www.nuget.org/packages/Lucene.Net.Contrib/2.9.4.1 "Nuget: Lucene.Contrib") contains a reference Lucene.Net.FastVectorHighlighter which defines an `ExtensionAttribute` class in the `System.Runtime.CompilerServices` namespace.

Updating the assembly reference `alias` from "global" to a custom one, fixed the warning.
