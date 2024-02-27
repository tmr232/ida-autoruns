# IDA Autoruns

IDA-Autoruns is a simple plugin to make a script run automatically
every time you open a specific IDB.

> [!CAUTION]
> ## Security Notice
> This is a _very_ bad idea for anything you get from other people.
> It just runs code. 
> No sandboxing, no verification.

## Installation
1. `pip install ida-settings`
1. Change `EDITOR` to your editor of choice.
    **Important:** The editing takes place once the editor process terminates.
1. Copy `autoruns.py` into IDA's plugin directory.

## Usage

1. Press `View -> Edit Autoruns` to edit the autoruns script
1. Be sure to save the IDB, as it will store the script
1. The script will run automatically when you save it,
    and every time you load the IDB.


## Drawbacks

While this plugin is useful for small, IDB-specific hacks, I highly
recommend using proper plugins whenever possible.
