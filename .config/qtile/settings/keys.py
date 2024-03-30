# Qtile keybindings

from libqtile.config import Key
from libqtile.command import lazy


mod = "mod4"

keys = [
    # -------------Windows conf---------------------

    # switch focus beetween windows
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "space", lazy.layout.next()),

    # move windows between left/right columns or move uo/down in current stack
    # moving out of range in columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),

    # grow windows
    Key([mod, "control"], "h", lazy.layout.grow_left()),
    Key([mod, "control"], "l", lazy.layout.grow_right()),
    Key([mod, "control"], "j", lazy.layout.grow_down()),
    Key([mod, "control"], "k", lazy.layout.grow_up()),
    Key([mod], "n", lazy.layout.normalize()),

    # toggle floating
    Key([mod, "shift"], "f", lazy.window.toggle_floating()),

    # toggle beetween split and unsplit of stack.
    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),

    # toggle between differents layouts as defined below
    Key([mod], "Tab", lazy.next_screen()),
    Key([mod, "shift"], "Tab", lazy.prev_layout()),

    # kill window
    Key([mod], "w", lazy.window.kill()),

    # switch focus of monitor
    Key([mod], "period", lazy.next_screen()),
    Key([mod], "comma", lazy.prev_screen()),

    # restart qtile
    Key([mod, "control"], "r", lazy.restart()),

    Key([mod, "control"], "q", lazy.shutdown()),
    Key([mod], "r", lazy.spawncmd()), # command prompt



    # ----------------Apps config------------------

    # menu
    Key([mod], "m", lazy.spawn("rofi -show drun")),

    # windows nav
    Key([mod, "shift"], "m", lazy.spawn("rofi -show")),

    # browser
    Key([mod], "b", lazy.spawn("chromium")),
    Key([mod, "shift"], "b", lazy.spawn("firefox")),

    # terminal
    Key([mod], "Return", lazy.spawn("kitty")),

    # visual studio
    Key([mod], "v", lazy.spawn("code")),

    # screenshot
    Key([mod], "s", lazy.spawn("scrot")),
    Key([mod, "shift"], "s", lazy.spawn("scrot -s")),

]
