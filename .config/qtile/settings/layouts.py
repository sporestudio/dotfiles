from libqtile import layout
from libqtile.config import Match
from .theme import colors

# Layouts and config


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
