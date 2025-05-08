# SkylandersGiants_Manual
Manual Archipelago world for Skylanders: Giants

This manual requires a new save and at least one Skylander of each element. Any Skylanders you do not own or do not\
want to use should be included in the characters_to_exclude yaml option. Currently, you start with one random Skylander\
and the first chapter unlocked (or a random chapter; see yaml options). Depending on the chosen goal, you either need\
to defeat Kaos in Chapter 16 or get 3 stars on every level (essentially, complete everything). 

[TOC]

## Required Hardware/Software

- Dolphin or another emulator that supports the Portal of Power, or a playable PC/console copy of the game. At least one\
Skylander from each element is manditory.
- If you are playing with linear mode disabled, you will need an existing save with all chapters unlocked but minimal
other progress. If using Dolphin emulator, you can find such a save in the Releases tab with every chapter available but\
zero progress on them (making your own save like this requires some third-party files and a bit of technical knowledge).

## Installation Procedures

- Set up like you would any other multiworld. Place the apworld in the custom_worlds folder of the Archipelago client\
with all other multiworlds, place this and all other yamls in the players folder, open the Archipelago client and click\
Generate. A complete guide can be found in the manual Discord server <a href=https://discord.com/channels/1097532591650910289/1163846227570462820/1163846227570462820>here</a>.
- If you are using Dolphin and not playing in linear mode, download All_Chapters.bin from the releases tab and perform\
the following steps:
  1. Open Dolphin emulator.
  2. If you already have saves that you care about, back them up now by right-clicking the game, selecting Export\
Wii Save, and following the on-screen dialog. 
  3. From the tool bar, select Tools → Import Wii Save and find the file you just downloaded. Open it and select Yes.
  4. The next time you boot up the game, you will have a fresh save with all chapters unlocked. 

## Joining a MultiWorld Game

Visit the manual Discord server <a href=https://discord.com/channels/1097532591650910289/1163846227570462820/1163846227570462820>here</a> and begin from step 6.



## Items
* Progressive Chapters (linear mode): The number of chapters currently available to play.\
**You will always start with 1**.
* Chapters (non-linear mode): Individually named chapters based on the levels in the game.
**You will always start with 1**.
* Adventure Pack Levels - If enabled, unlocks the corresponding adventure pack level.
* Map to Arkus Fragments (non-linear mode) - A pre-defined amount are required to fight Kaos.
* Progressive Soul Abilities - Unlocks the use of soul abilities collected in the first *n* chapters.
* Progressive Skylander Upgrades - Unlocks the ability to purchase *n* upgrades for each Skylander (or each Skylander\
of that element, depending on the yaml configuration).
* Skylanders - Unlocked individually or by element, depending on the yaml configuration. **You will always start with 1**.
* Active Items - Unlocks the item in question if its corresponding adventure pack is enabled.
* Luck-o-tron Wheel Slots - Each unlocks the ability to slot one luck-o-tron wheel, up to four.

## Locations
* Completion of each base chapter.
* Completion of adventure pack chapters (if enabled).
* Hats
* Legendary Treasures
* Chests
* Soul Gems
* Winged Sapphires
* Heroic Challenges (if enabled)
* Achieving 3 stars on levels ("Perfection")
* Arena Battles
* Skystones battles

## Traps
* Element Lock Trap - Upon starting a level, you can only use Skylanders of the same element as the one you began the\
level with. Effect ends on level completion.
* Solo Trap - Upon starting a level, you may notuse any other Skylanders or active items until you beat the level or\
are defeated. 
* Rename Skylander Trap - Joke trap. Upon receipt, you must rename the last Skylander played using a name of the\
sender's choosing.
* Reset Last Character Trap - Hard Trap. Upon receipt, you must delete all data associated with the last Skylander\
used. Level, money, and upgrades are reset.
* Traps are handled a little different here than in other manuals. There is no set amount of each trap. Instead,\
the filler_trap_percent yaml option determines what percentage of filler items will be replaced with traps, and\
yaml options determine the likelihood of traps relative to one another. Let me use the default as a example:
  * By default, 50% of filler items are replaced with traps. Let's say we end up with 40 traps
  * The chance of a particular trap being selected for generation is its weight divided by the sum of all trap weights.\
  The default weight of element lock traps is 45, and the sum of all **default** trap weights is 100. 
  * What does this mean?
    * Each trap has a 45% (45/100) chance to be an element lock trap. 
  * What does this **not** mean?
    * 45% of all traps will be element lock traps
    * there will be 45 element lock traps


## Ideas for the Future
* upgrade fairy as an item?
* pacifist trap (only kill necessary enemies on next level and restart if you fail)
* progressive shops? nah
* I don't want to add story scrolls because you rarely have to stray from the main path to get them. In my opinion,\
most collectable locations should require *some* effort to reach, and there are too many locations right now anyway

Credits:
* emmet_is_a_birb for adding a bunch of locations and items when I was busy and correcting some of my logic