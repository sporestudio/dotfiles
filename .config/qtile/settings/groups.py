#!/usr/bin/env python3

from libqtile.config import Key, Group
from libqtile.lazy import lazy
from .keys import mod, keys


groups = []
group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9",]

#group_labels = ["DEV", "WWW", "SYS", "DOC", "VBOX", "CHAT", "MUS", "VID", "GFX",]
#group_labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9",]
group_labels = ["󰮯 ", " ", "󰊠 ", "󰊠 ", " ", " ", "󰮯 ", " ", "󰊠 ",]


group_layouts = ["bsp", "bsp", "bsp", "bsp", "bsp", "bsp", "bsp", "bsp", "bsp"]




for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))
 
for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=False),
                desc="Move focused window to group {}".format(i.name),
            ),
        ]
    )


