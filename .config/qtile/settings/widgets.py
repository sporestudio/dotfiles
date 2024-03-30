from libqtile import widget, bar, extension, qtile
from libqtile.widget import GenPollText
from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration 
from .theme import colors
from qtile_extras.popup.toolkit import PopupRelativeLayout, PopupImage, PopupText, PopupWidget
import subprocess
import os

myTerm = "kitty"


# Bar widgets
def init_widgets_list():
    widgets_list= [
        widget.Image(
            filename = "~/.config/qtile/img/qtile-icon1.svg",
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

    



primary_widgets = [
    *init_widgets_list(),
]

secondary_widgets = [
    *init_widgets_list(),
]

widget_defaults = {
    'font': 'Helvetica Bold',
    'fontsize': 12,
    'padding': 1,
}

extension_defaults = widget_defaults.copy()
