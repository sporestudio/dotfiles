![image](https://github.com/sporestudio/dotfiles/assets/144621916/47ec0562-7c52-476e-ba0e-67f085fe3503)


![image](https://github.com/sporestudio/dotfiles/assets/144621916/ecb5e301-bdf2-4a15-a4e1-5fb7f109db23)

![image](https://github.com/sporestudio/dotfiles/assets/144621916/b4076f20-a39b-490d-95ce-34d5447b5954)

![image](https://github.com/sporestudio/dotfiles/assets/144621916/0440bd5b-cf08-4eaa-b85b-2b3059e76b2e)



# SPORE SETUP CONFIGURATION FOR ARCH LINUX



<a href="https://qtile.org/"><img alt="QtileWM Logo" height="100" align = "left" src="https://docs.qtile.org/en/stable/_images/qtile-logo.svg"></a>

This project consists of the development and design of a minimalist window manager based on the Qtile window manager, which is a free and easily configurable window manager. 
It is written entirely in Python, so here are some of the features I have developed to make the window manager completely adapted to my needs and workflow.

It is also noteworthy that Qtile is a window manager that consumes very few resources of our computer, that added to the fact that it runs in a minimalist installation distribution such as Arch Linux, makes it can run smoothly on virtually any computer.



## ❄️ INFORMATION



- **OS:** [Arch Linux](https://archlinux.org)
- **WM:** [Qtile](https://qtile.org/)
- **Terminal:** [Kitty](https://sw.kovidgoyal.net/kitty/)
- **Shell:** [Fish](https://fishshell.com/)
- **Editor:** [Lazy vim](https://www.lazyvim.org/) 
- **Compositor:** [Picom](https://github.com/yshui/picom)

### Qtile modules:

```
├── qtile
│   ├── icons
│   │   ├── qtile-icon1.svg
|   |   └── qtile-icon2.svg
│   ├── settings
|   |   ├── groups.py
|   |   ├── keys.py
|   |   ├── layouts.py  
|   |   ├── mouse.py
|   |   ├── path.py
|   |   ├── screens.py
|   |   ├── theme.py
|   |   └── widgets.py
|   ├── themes
|   |   ├── dark-grey.json
|   |   ├── dracula.json
|   |   └── rosespine.json
|   ├── wallpapers
|   |   ├── cleanpaper.png
|   |   └── simplepaper.png
|   ├── autostart.sh
|   ├── config.json
|   └── config.py

```

#### Groups.py

In this module are configurated the workgroups of the window manager, used to allow several workspaces in which one or more programmes can be opened simultaneously.

In the code that we are going to see next, lists are configured where group names from 1 to 9 and a series of visual labels are stored. It is also defined that the layout of these groups will be in all cases "bsp" (binary space system), which we will talk about later. In this moment I'm using the icons label group.

```python
groups = []
group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9",]

#group_labels = ["DEV", "WWW", "SYS", "DOC", "VBOX", "CHAT", "MUS", "VID", "GFX",]
#group_labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9",]
group_labels = ["󰮯 ", " ", "󰊠 ", "󰊠 ", " ", " ", "󰮯 ", " ", "󰊠 ",]


group_layouts = ["bsp", "bsp", "bsp", "bsp", "bsp", "bsp", "bsp", "bsp", "bsp"]
```


In the code below, we create a Group instance for each group_name.

```python
for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))
```

This loop goes through each group in the groups list and defines two keyboard shortcuts (Key):

- Switch to group: mod + group name (i.name). This switches the current view to the specified group
- Move the window in focus to the group: mod + shift + group name. This moves the window that is in focus to the specified group without changing the current view.

```python
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
```

#### Keys.py

In this module we can find the keyboard shortcuts that I have defined for the manager. Here are all the key combinations that we must use to open certain programs such as the terminal or the web browser.

As we can see below we have created a list in which using the Key() function we can define a keystroke combination to open our programs.

```python
keys = [
    
    # menu
    Key([mod], "m", lazy.spawn("rofi -show drun")),

    # windows nav
    Key([mod, "shift"], "m", lazy.spawn("rofi -show")),

    # browser
    Key([mod], "b", lazy.spawn("chromium")),
    Key([mod], "f", lazy.spawn("firefox")),

    # terminal
    Key([mod], "Return", lazy.spawn("kitty")),

    # visual studio
    Key([mod], "v", lazy.spawn("code")),

    # screenshot
    Key([mod], "s", lazy.spawn("scrot")),
    Key([mod, "shift"], "s", lazy.spawn("scrot -s")),

]
```


#### Layouts.py

This code configures the layouts and rules for floating windows in Qtile. It defines how windows should look and behave, including border and margin colour, as well as rules for when windows should float rather than conform to a fixed layout. This is a crucial aspect of customising Qtile to suit the user's preferences and needs.

As we can see, the BSP (Binary Space Partitioning) layout, a layout provided by Qtile, is configured.
Binary Space Partitioning is an effective technique for organising and managing windows in a window manager such as Qtile. It provides a flexible and efficient way to use the available space on the screen, adapting dynamically to the user's needs.

```python
layout_conf = {
    'border_focus': '#E3DAC9',
    'border-width': 2,
    'margin': 5,
}


layouts = [
    #layout.MonadTall(**layout_conf),
    #layout.MonadWide(**layout_conf),
    #layout.Columns(**layout_conf),
    layout.Bsp(**layout_conf),
    layout.Max(),
    layout.Floating(**layout_conf),
]


floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),
        Match(wm_class='makebranch'),
        Match(wm_class='maketag'),
        Match(wm_class='ssh-askpass'),
        Match(wm_class='xterm'),
        #Match(tittle='branchdialog'),
        #Match(tittle='pinentry'),
    ],
    border_focus='#e3dac9'
)
```


#### Mouse.py

In this module we have a configuration related to the behaviour of the mouse in floating window mode.

```python
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position()
    ),
    Drag(
        [mod],
        "Button3",
        lazy.window.set_size_floating(),
        start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front())
]
```

The first Drag function allows us to move the floating window around the screen with super + left mouse button, while the second one allows us to resize the window with super + right mouse button.
The click function allows us to bring the window in focus with the mouse to the front with super + middle mouse button.


#### Screens.py

This code configures multiple screens in Qtile, creating a status bar. I have tried to create a minimalist and functional bar, but with a minimum of useful information.

```python
def status_bar(widgets):
    return bar.Bar(widgets, 38, opacity=0.92, background="#061113", margin=12)


screens = [Screen(top=status_bar(primary_widgets))]

xrandr = "xrandr | grep -w 'connected' | cut -d ' ' -f 2 | wc -l"

command = subprocess.run(
    xrandr,
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)

if command.returncode != 0:
    error = command.stderr.decode("UTF-8")
    logger.error(f"Failed counting monitors using {xrandr}:\n{error}")
    connected_monitors = 1
else:
    connected_monitors = int(command.stdout.decode("UTF-8"))

if connected_monitors > 1:
    for _ in range(1, connected_monitors):
        screens.append(Screen(top=status_bar(secondary_widgets)))

```

As we can see we create a status_bar function that creates a bar (bar.Bar) provided by the Qtile libqtile library with the specified widgets, as well as the bar height, colour...

We run the command "xrandr" to know the number of screens and store it in the command variable, capturing the output (stdout) and the errors (stderr).

We check the number of connected monitors and if there is more than one we add it to the list of screens (screens = [ ]).

#### Widgets.py

This module configures the widgets that appear in the status bar created earlier in screens.

First we create a function that will contain all the widgets, which include an image such as the logo, the workspaces, the selected layout, the time, the version of the operating system we are using and the CPU and Ram usage.

```python
def init_widgets_list():
    widgets_list= [
        widget.Image(
            filename = "~/.config/qtile/icons//qtile-icon1.svg",
            scale = "false",
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm)},
            padding = 2,
        ),
        widget.Prompt(
            font = "Ubuntu Nerd Font",
            fontsize = 14,
            foreground = "#f0ffff"
        ),
        widget.GroupBox(
            fontsize = 11,
            font = 'Ubuntu Nerd Font',
            margin_y = 3,
            margin_x = 4,
            padding_y = 2,
            padding_x = 3,
            borderwidth = 3,
            active = colors['active'],
            inactive = colors['inactive'],
            rounded = False,
            highlight_method = 'block',
	        urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True		
        ),
        widget.CurrentLayoutIcon(
            foreground = "#f0ffff",
            padding = 2,
            scale = 0.5
        ),
        widget.Spacer(length = bar.STRETCH),
        widget.Clock(
            foreground = "#f0ffff",
            format = "%a, %b %d - %H:%M",
        ),
        widget.Spacer(length = bar.STRETCH),
        widget.GenPollText(
                 update_interval = 300,
                 func = lambda: subprocess.check_output("printf $(uname -r)", shell=True, text=True),
                 foreground = "#f0ffff",
                 fmt = '❤  {}',
                 ),
        widget.Spacer(length = 12),
        widget.CPU(
                 format = '▓  {load_percent}%',
                 foreground = "#f0ffff",
                 ),
        widget.Spacer(length = 12),
        widget.Memory(
                 foreground = "#f0ffff",
                 mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e htop')},
                 format = '{MemUsed: .0f}{mm}',
                 fmt = '󰍛  {}',
                 ),
        widget.Spacer(length = 8),
        #widget.Systray(padding = 3),
        widget.Spacer(length = 8),

        ]
    return widgets_list
```

We define lists of widgets for primary and secondary screens using init_widgets_list().

```python
primary_widgets = [
    *init_widgets_list(),
]

secondary_widgets = [
    *init_widgets_list(),
]
```

Finally, we set default values for widgets such as font, font size and padding.

```python
widget_defaults = {
    'font': 'Helvetica Bold',
    'fontsize': 12,
    'padding': 1,
}

extension_defaults = widget_defaults.copy()
```


#### Config.py

Finally we have the main file, in which we import the modules created earlier, and set the start of the program with a hook.

```python
########################################
##                                    ##
## Spore Qtile Personal Configuration ##
##                                    ##
########################################

## ---------- Main config ----------- ##


from libqtile import hook

from settings.keys import mod, keys
from settings.groups import groups
from settings.layouts import layouts, floating_layout
from settings.widgets import widget_defaults, extension_defaults, myTerm
from settings.screens import screens
from settings.mouse import mouse
from settings.path import qtile_path

from os import path
import subprocess


@hook.subscribe.startup_once
def autostart():
    subprocess.call([path.join(qtile_path, 'autostart.sh')])



main = None
dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_wrap = True
auto_fullscreen = True
focus_on_window_activation = 'urgent'
wmname = "LG3D"
```

The hook will run the autostart.sh file, which contains some settings for the startup of the wallpaper and the "Picom" composer.
Finally I made some general settings, which can be customized.

### ❄️ SETUP

> This is step-by-step how to install qtile with spore config. Just [R.T.F.M](https://en.wikipedia.org/wiki/RTFM).

:warning: **This setup instructions only provided for Arch Linux and assuming that your AUR Helper is Paru (and other Arch-based distributions)**


<details>
   
   <summary><b>1. Install Required Dependencies and Qtile Window Manager</b></summary>


> First of all you should install Qtile Window Manager

```sh
sudo pacman -S qtile
```

> Install necessary dependencies

```sh
sudo pacman -S python-pip python-xlib xcb-util-keysyms
```


> Install qtile extras

```sh
paru -S qtile-extras
```


> You will need the Picom compositor

```sh
sudo pacman -S picom
```


> Create a directory for the user config

```sh
mkdir -p ~/.config/qtile
cp /usr/share/doc/qtile/default_config.py ~/.config/qtile/config.py
```


</details>


<details>
   <summary><b>2. Install spore.io</b></summary>


> Install git

```sh
sudo pacman -S git
```


> Clone the repository

```sh
mkdir ~/.config/qtile
cd ~/.config/qtile
git clone https://github.com/sporestudio/dotfiles/tree/main/.config/qtile
```

   
</details>


> Install a few fonts in order for text and icons to be rendered properly.

Necessary fonts:

- **Helvetica** - [here](https://fontsgeek.com/helvetica-font)
- **Mononoki Nerd Fonts** - [here](https://www.nerdfonts.com/font-downloads)
- **Icons Hack Nerd Fonts** - [here](https://www.nerdfonts.com/font-downloads)


Once you download them and unpack them, place them into `~/.fonts` or `~/.local/share/fonts`.

### ❄️ COLOR SCHEME

![image](../assets/color-scheme.png)

The colour scheme is called Dark grey. As the name suggests, a combination of greys has been used together with azure white to enhance the contrast.

This combination gives a sober and elegant touch to the design and fits well with the minimalist philosophy that the window environment aims to achieve. A wallpaper has also been designed to match the theme of the environment.


<!-- License -->

## ❄️ LICENSE

Spore.io is under <a href="https://github.com/sporestudio/dotfiles/blob/main/LICENSE">MIT License.
</a>

<!-- Author -->

## ❄️ AUTHOR

Created by <a href="https://github.com/sporestudio/">sporestudio</a>.

