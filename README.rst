======
yeecli
======

.. image:: https://img.shields.io/pypi/v/yeecli.svg
        :target: https://pypi.python.org/pypi/yeecli

.. image:: https://gitlab.com/stavros/yeecli/badges/master/build.svg
        :target: https://gitlab.com/stavros/yeecli/pipelines


yeecli is a command-line utility for controlling the YeeLight RGB LED lightbulb.
It is released under the BSD license.


Installation
------------

You can install yeecli with pip::

    pip install yeecli


Usage
-----

To see the commands supported by yeecli, just run it without any commands. It
allows you to turn the light bulb on or off, set the RGB value, the color
temperature, the HSV value, etc.

yeecli does not support discovery, so you have to specify the IP of the bulb you
want to use every time. To make this easier, yeecli supports using
a configuration file.

Simply create a file in `~/.config/yeecli/yeecli.cfg` that looks something like
this::

    [default]
    ip = 192.168.12.3
    port = 55433
    effect = smooth
    duration = 500

And the defaults will be loaded from it. All the values in it are optional, and
you can override them in the command line when running the script.
