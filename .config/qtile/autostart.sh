#!/bin/sh

# Keyboard #
setxkbmap es

# Wallpaper #
nitrogen --restore &

# Picom daemon #
picom --daemon

# Screen configuration #
xrandr --output DP-1 --mode 1920x1080 --output HDMI-1 --mode 1360x768 --left-of DP-1
xset s off
xset -dpms
