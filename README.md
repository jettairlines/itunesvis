# Do you really like your iTunes Library?
Sorting your iTunes Play List based on how much you skip.

## Usage
- Get this repo
    ```bash
    $ git clone https://github.com/jettairlines/messenger-moods
    ```
- open iTunes, go to iTunes > Preference > Advanced
- Check "Shate iTunes Library XML", then go to path in grey box
- Drag path/iTunes Music Library.xml into cloned repo
- Run
    ```bash
    $ chmod +x run.sh 
    $ . run.sh
    ```
- Open http://localhost:8000/ to view results
- Drag bar to indicate how important Play & Skip is to you

### Tech
- Python XML reader & JSON dump
- JS & jQuery frontend
- Sorttable.js

**Rankings are calculated by** Play : Skips input over time since you've added this song to your library

## Background
### Do I have a good playlist?
### Motivation
tl;dr: relationship between "Loved" marl & listening habits (plays + skips)
I really really want to explorer my iTunes library data (yes I still use iTunes) to see how good am I at constructing my own music library. The way I listen to music is play everthing on shuffle and skip songs I'm not in the mood for. I am very commited to the "Loved" mark, and once I mark a song "Loved" I always look for it first and feel very bad skipping it. Thus, "Loved" and skip count are important to me.
### Audience
Anyone who still uses iTunes for music & finding themselves skipping way to much of their supposedly "favourite" songs
- Although iTunes makes play & skip count avalible, one never really thinks about the implications behind them. These numbers don't tell much by themselves
### Data
- In every iTunes folder
- Depends on personal playlist size. Personally I have ~680 songs.
- The point is to use iTunes very very often for good play & skip stats
### Related Wrk
- [iTunes Library Analyzer - Analyze iTunes Library to Charts]
    - Graphic method to represent given iTunes data
    - Some analysis with combinations of the data "Listening Times" etc...
    - Download & use though....
- [SwiBeat - MP3 Player & Analyzer to Visualize Your Music Choice]
    - Generates smarter/temporary PL based on preference input & given iTunes data
    - Based more on genre & year & other music metadata instead of actual useage data (plays etc.)
- More than enough Spotify analyzers... based on music metadata (what Spotify's good at) instead of usage history

## Shots & PoI
![](http://i1064.photobucket.com/albums/u362/Jett_Wang/Screen%20Shot%202016-05-12%20at%201.15.42%20PM_zpssjeq4upy.png)

vs. setting to 2/5
![](http://i1064.photobucket.com/albums/u362/Jett_Wang/Screen%20Shot%202016-05-12%20at%2012.49.42%20PM_zpsjkd6cseg.png)

You can see that by putting more weight to Plays, MGMT - Kids & OMAM - Little Talks & FTP - Houdini (the more played ones) were moved up, and the rest of the less played dropped out of top 5.

HOWEVER, the slider is set for people that value skips different. Although comparing betweent different slider parameters could yield interesting results, this vis was meant to NOT do that, but instead compare it with the audience's actual/mental iTunes PL.

Personally, I value Skips over Play by 4/5
![](http://i1064.photobucket.com/albums/u362/Jett_Wang/Screen%20Shot%202016-05-12%20at%201.16.01%20PM_zpsegnnvjcs.png)

**PoI**: among my least favs there are two songs I marked "Loved"
![](http://i1064.photobucket.com/albums/u362/Jett_Wang/Screen%20Shot%202016-05-12%20at%201.16.12%20PM_zps3uz2u0u0.png)

**PoI**: Despite under my input parameters where less skips do beter, when sorted by skips, I foudn out that there are plenty of songs I skip a lot but still "Loved" (#428 Chairlift - Bruises), and plenty others I don't skip as often but still dislike anyways (#207 Porter Robinson - Fellow Feelings).
![](http://i1064.photobucket.com/albums/u362/Jett_Wang/Screen%20Shot%202016-05-12%20at%201.17.21%20PM_zpspj3o8ltu.png)
![](http://i1064.photobucket.com/albums/u362/Jett_Wang/Screen%20Shot%202016-05-12%20at%201.17.40%20PM_zpsu8tvhphs.png)

## TIL
- Porter Robinson - Sad Machine is apparently my favourite song.
- I thought Fox Stevenson/Curbi - Hoohah was a good song and I was surprised to see it ranked #682. Guess not.
- Although like most humans, I like newly added songs better (I recognize them when looking down the list), there are a few songs that I've had for longer that still beats the newbie crowd.
- The "Loved" mark doesn't have as strong of a correlation w/ my listening habits as I expected.
- But I don't think I'm taking off the marks for songs at bottom of my list. I still think they are very very good songs, but I guess that just means I have to be in specific moods/circumstances to appreciate to them.
- My mental representation of the "Loved" the mark is probably something like "songs I think are good, though I don't always wanna listen to them."
- The "Loved" mark is actually a wonderful invention, like FB's "like" button.

Looking at this list actually changed my listening habit slightly even through the development process. I noticed that
- I skip top of the list less, especially Sad Machine. And due to Thought Polarization & Mere Exposure Effect I liked them better.
- I skip bottom of the list more, especially Rhianna - Diamond (most skipped).And due to Thought Polarization they are beling disliked more and more and some are mentally marked for deletion.
- But with execption of "Loved" songs at bottom of the list. Now I associate them stronger with the moods I usually am in while listening to them, and I still love them and learned that it's ok to skip them.

License
----

Copyright (c) 2016 Jett Wang Licensed under the WTFPL license.

[iTunes Library Analyzer - Analyze iTunes Library to Charts]: https://www.wondershare.com/apple-software/analyze-itunes-library.html
[SwiBeat - MP3 Player & Analyzer to Visualize Your Music Choice]:https://itunes.apple.com/us/app/swibeat-mp3-player-analyzer/id1044923292
