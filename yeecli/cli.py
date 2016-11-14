import os
import sys
try:
    import ConfigParser
except ImportError:
    import configparser as ConfigParser

import click
import yeelight

try:
    import tbvaccine
    tbvaccine.add_hook()
except:
    pass

try:
    from . import __version__
except (SystemError, ValueError):
    from __init__ import __version__

BULB = None


def param_or_config(param, config, section, name, default):
    """
    Return a parameter, config item or default, in thar order of
    priority.
    """
    try:
        conf_param = config.get(section, name)
    except (ConfigParser.NoSectionError, ConfigParser.NoOptionError):
        conf_param = None

    try:
        # Try to see if this parameter is an integer.
        conf_param = int(conf_param)
    except:
        pass

    return param or conf_param or default


@click.group()
@click.version_option(
    version=__version__,
    prog_name="yeecli",
    message="%(prog)s %(version)s: And there was light."
)
@click.option('--ip', metavar='IP', help="The bulb's IP address.")
@click.option('--port', metavar='PORT', help="The bulb's port.", type=int)
@click.option("--effect", metavar='EFFECT', help="The transition effect.", type=click.Choice(['smooth', 'sudden']))
@click.option("--duration", metavar="DURATION_MS", help="The transition effect duration.", type=click.IntRange(1, 60000, clamp=True))
@click.option("--bulb", metavar="NAME", default="default", help="The name of the bulb in the config file.", type=str)
def cli(ip, port, effect, duration, bulb):
    """
    yeecli is a command-line utility for controlling the YeeLight RGB LED
    lightbulb.
    """
    global BULB

    config = ConfigParser.SafeConfigParser()
    config.read([os.path.expanduser('~/.config/yeecli/yeecli.cfg')])

    ip = param_or_config(ip, config, bulb, "ip", None)
    port = param_or_config(port, config, bulb, "port", 55443)
    effect = param_or_config(effect, config, bulb, "effect", "sudden")
    duration = param_or_config(duration, config, bulb, "duration", 500)

    if not ip:
        click.echo("No IP address specified.")
        sys.exit(1)

    BULB = yeelight.Bulb(
        ip=ip,
        port=port,
        effect=effect,
        duration=duration,
        auto_on=True
    )


@cli.command()
@click.argument("value", type=click.IntRange(1, 100, clamp=True))
def brightness(value):
    """Set the brightness of the bulb."""
    click.echo("Setting the bulb to {} brightness...".format(value))
    BULB.set_brightness(value)


@cli.command()
@click.argument("degrees", type=click.IntRange(1700, 6500, clamp=True))
def temperature(degrees):
    """Set the color temperature of the bulb."""
    click.echo("Setting the bulb's color temperature to {}...".format(degrees))
    BULB.set_color_temp(degrees)


@cli.command()
@click.argument("hue", type=click.IntRange(0, 359, clamp=True))
@click.argument("saturation", type=click.IntRange(0, 100, clamp=True))
def hsv(hue, saturation):
    """Set the HSV value of the bulb."""
    click.echo("Setting the bulb to HSV {}, {}...".format(hue, saturation))
    BULB.set_hsv(hue, saturation)


@cli.command()
@click.argument("red", type=click.IntRange(0, 255, clamp=True))
@click.argument("green", type=click.IntRange(0, 255, clamp=True))
@click.argument("blue", type=click.IntRange(0, 255, clamp=True))
def rgb(red, green, blue):
    """Set the RGB value of the bulb."""
    click.echo("Setting the bulb to RGB {}, {}, {}...".format(red, green, blue))
    BULB.set_rgb(red, green, blue)


@cli.command()
def toggle():
    """Toggle the bulb's state on or off."""
    click.echo("Toggling the bulb...")
    BULB.toggle()


@cli.command()
@click.argument("state", type=click.Choice(['on', 'off']))
def turn(state):
    """Turn the bulb on or off."""
    click.echo("Turning the bulb {}...".format(state))
    if state == "on":
        BULB.turn_on()
    elif state == "off":
        BULB.turn_off()


@cli.command()
def save():
    """Save the current settings as default."""
    click.echo("Saving settings...")
    BULB.set_default()


@cli.command()
def status():
    """Show the bulb's status."""
    click.echo("Bulb parameters:")
    for key, value in BULB.get_properties().items():
        click.echo("* {}: {}".format(key, value))

if __name__ == "__main__":
    cli()
