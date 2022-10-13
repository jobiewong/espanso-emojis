# Espanso Emojis 
This is a package created for [espanso](https://espanso.org/) called `actually-all-emojis` that provides up-to-date emoji triggers.

The method behind the package is very simple. Emoji unicode values and names are fetched from [Unicode.org](https://unicode.org/emoji/charts/full-emoji-list.html). They're then formatted and processed in Python and exported as a yml file.

There are two versions of the package:
- Default (underscores) - this formats the espanso triggers with underscores between words (e.g. `:kissing_face:`)
- Spaces - this formats the espanso triggers with spaces between words (e.g. `:kissing face:`)

## Installation
### Manual
1. Navigate to [Releases](https://github.com/jobiewong/espanso-emojis/releases/tag/espanso)
2. Decide whether you want to install the version that uses **underscores** or **spaces** and download the zip file for the relevant version
3. Navigate to your Espanso directory (on Windows this is located in %appdata% by default) and extract the zip file into `/match/packages`
