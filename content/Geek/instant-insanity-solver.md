Title: Instant insanity solver
Date: 2013-01-29 21:12:05
Slug: instant-insanity-solver
Tags: c#, .net

I was visiting my sister for Christmas and they had a puzzle for us to play with. It's called the Instant Insanity puzzle, or at least it was a variation of it with old comic book covers instead of plain colours like the one on [Wikipedia](http://en.wikipedia.org/wiki/Instant_Insanity).

Pretty much everyone had a shot but nobody could quite get all 4 cubes to have different sides. Like a true geek I decided to write some code to solve it for me.

I put a little sticker with an arrow on each cube so I could identify them and what direction was "north". This allowed me to map the cubes in code and also reverse the map when the code found a solution.

You can find the code here: [GitHub](https://github.com/AndyA13/InstantInsanitySolver)

As it says in the Readme, it definitely needs refactored but it got the job done. It ran pretty much instantly and found 4 solutions (you can turn the stack 90 degrees and still have the same solution). It also finds 65,532 non solutions but I have to assume there are four of each one, making there 16,383 invalid solutions. A lot less than claimed on the box...
