# Espanso Emojis v0.3.0

> ✅ Now updated to support v15.0 Emojis

This is a package created for [espanso](https://espanso.org/) called `actually-all-emojis` that provides up-to-date emoji triggers.

The method behind the package is very simple. Emoji unicode values and names are fetched from [Unicode.org](https://unicode.org/emoji/charts/full-emoji-list.html). They're then formatted and processed in Python and exported as a yml file.

There are two versions of the package:

- Default (underscores) - this formats the espanso triggers with underscores between words (e.g. `:kissing_face:`)
- Spaces - this formats the espanso triggers with spaces between words (e.g. `:kissing face:`)

Shortcodes are used to match those found on popular platforms such as Slack and Discord. A list of shortcodes can be found [here](https://listemoji.com/cheat-sheet)

## Installation

### CLI (from Git)

This approach installs the package directly from the Git repository as the external package.

1. Ensure Espanso is properly installed and accessible through the terminal
2. Paste the following code into your command line: `espanso package install actually-all-emojis --git https://github.com/jobiewong/espanso-emojis -e` (or `actually-all-emojis-spaces`)
3. Hit <kbd>Enter</kbd>

### Manual

1. Navigate to [Releases](https://github.com/jobiewong/espanso-emojis/releases/tag/espanso)
2. Decide whether you want to install the version that uses **underscores** or **spaces** and download the zip file for the relevant version
3. Navigate to your Espanso directory (on Windows this is located in %appdata% by default) and extract the zip file into `/match/packages`

### CLI
1. Ensure Espanso is properly installed and accessible through the terminal
2. Paste the following code into your command line: `espanso install actually-all-emojis`
3. Hit enter
> ⚠️ The version of this package on the espanso hub may not be the most up-to-date!
