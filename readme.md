## Preview

### Browse games library
![](repo-assets/general.gif)

### Resize window
![](repo-assets/feature-resize.gif)

### Launch game from within PS2Library
![](repo-assets/start-game.gif)

## CHANGELOG

### 2022-11-05

- added active, fuzzy search

## Why?

- Modern, web-technology based UI (everything is OFFLINE, but the technology used is HTML and CSS)
- Simple to use

I personally tried Specabis and PCSX2Bonus, of which both had some problems or were too elaborate for my lazy ass to set up, so I did what any other sane software engineer would do: make my own.

## Limitations

- Multidisc games are not supported in the UI yet (not too much work left but it takes some time to get done)
- Requires you to put each game into its own folder
- Requires you to download artwork on your own
- Folder configuration is currently done via an INI file which some might perceive as clunky.

## Pros & Features

-  ⚡ Blazingly fast
-  😎 Good looking UI
-  ⚙ Easy to set up

## How does it work under the hood?

I use *Python* as the general language, *Flask* for the UI and *flaskwebgui*, *HTML* and *CSS* for creating and styling the UI.


## Inspiration

|  Link |
|---|
| [Specabis](https://github.com/valters-tomsons/Spectabis)  |
| [PCSX2Bonus](https://forums.pcsx2.net/Thread-PCSX2Bonus-A-PCSX2-launcher-frontend) |


## Recognized Formats

All formats that are supported by PCSX2 are recognized by PS2Library:

- .iso
- .bin
- .mdf
- .nrg
- .img
- .dump
- .gz
- .cso
- .chd

- .ISO
- .BIN
- .MDF
- .NRG
- .IMG
- .DUMP
- .GZ
- .CSO
- .CHD

### Supported art cover formats

- .png
- .jpg
- .jpeg
- .gif
- .webp

- .PNG
- .JPG
- .JPEG
- .GIF
- .WEBP

## Known issues

- After starting a game right after launching PS2Library, any consequent launches are in the background (you have to switch to PCSX2 via the taskbar) (cause: unkown as of now.)