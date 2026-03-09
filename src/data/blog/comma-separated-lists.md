---
title: "Comma separated lists"
description: "A handy generic method for creating comma separated strings from object properties in C#."
pubDate: 2013-01-18
tags: ["c#"]
---

While working on a site recently I had to output the name property from a list of objects that had been selected by the user.

I wrote a handy little method that let me pass in the objects and a Func to select the property to be used in the list.

```csharp
private string ToCommaSeperatedString<T>(IEnumerable<T> items, Func<T, string> property)
{
    if (items != null && items.Count() > 0)
    {
        List<string> values = new List<string>();

        foreach (T item in items)
        {
            values.Add(property.Invoke(item));
        }

        if (values.Count > 0)
        {
            return String.Join(", ", values);
        }
    }

    return String.Empty;
}
```

Embedding code is still something of a work in progress. Just noticed it had deleted part of the method declaration.
