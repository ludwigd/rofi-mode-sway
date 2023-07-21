# rofi-mode-sway

A Rofi mode for switching windows under Sway that can be used in combination with other Rofi modes.

![Rofi with sway and drun modes enabled](screenshots/screenshot1.png)

![Rofi with sway and drun modes enabled, filtered](screenshots/screenshot2.png)

## Installation

The script depends on the following binaries:

- swaymsg
- jq
- xargs
- rofi (not a real dependency, but the script is useless without)

### Fedora

For Fedora there is a COPR you can use:

```
# dnf copr enable ludwigd/rofi-mode-sway
# dnf install rofi-mode-sway
```

### Other

Copy `rofi-mode-sway.sh` to a location in your `$PATH`, e.g., `~/bin`, and make it executable with `chmod +x rofi-mode-sway.sh`.

## Usage

The intended way to use this script is in combination with other Rofi modes. To combine it with `drun` mode, launch Rofi like this:

```
rofi -modes combi -combi-modes sway:rofi-mode-sway.sh,drun -show combi
```