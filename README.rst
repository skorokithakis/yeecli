======
yeecli
======

.. image:: https://img.shields.io/pypi/v/yeecli.svg
        :target: https://pypi.python.org/pypi/yeecli

.. image:: https://gitlab.com/stavros/yeecli/badges/master/build.svg
        :target: https://gitlab.com/stavros/yeecli/pipelines


yeecli is a command-line utility for controlling the YeeLight RGB LED lightbulb.
It is released under the BSD license.


Quick start
-----------

You can install yeecli with pip::

    pip install yeecli

You're done! Here are a few sample commands::

    yee --ip=192.168.0.34 turn on
    yee --ip=192.168.0.34 toggle
    yee --ip=192.168.0.34 rgb ff00ff
    yee --ip=192.168.0.34 brightness 100


Features
--------

This is a list of features supported right now and features that I'm wanting to
add later.

Currently supported:

* Non-music modes
* All flow transitions in the protocol
* Additional HSV flow transition
* Presets
* Multiple bulbs

Will probably be supported at some point:

* Music mode
* Bulb groups
* Discovery


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

You can also specify multiple bulbs like so::

    [default]
    ip = 192.168.12.3
    port = 55433
    effect = smooth
    duration = 500

    [bedroom]
    ip = 192.168.12.4
    effect = smooth
    duration = 500

    [hallway]
    ip = 192.168.12.5

Then, to select a specific bulb, just pass it to the ``--bulb`` option::

    yee --bulb=bedroom brightness 100
