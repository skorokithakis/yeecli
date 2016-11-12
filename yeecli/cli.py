import os
import sys
import configparser as ConfigParser

import click
import pyyeelight

try:
    import tbvaccine
    tbvaccine.add_hook()
except:
    pass

from __init__ import __version__

BULB = None


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
def cli(ip, port, effect, duration):
    """
    yeecli is a command-line utility for controlling the YeeLight RGB LED
    lightbulb.
    """
    global BULB

    config = ConfigParser.SafeConfigParser()
    config.read([os.path.expanduser('~/.config/yeecli/yeecli.cfg')])

    ip = ip or config.get("default", "ip", fallback=None)
    port = port or int(config.get("default", "port", fallback="0")) or 55443
    effect = effect or config.get("default", "effect", fallback=None) or "sudden"
    duration = duration or int(config.get("default", "duration", fallback="0")) or 500

    if not ip:
        click.echo("No IP address specified.")
        sys.exit(1)

    BULB = pyyeelight.YeelightBulb(ip=ip, port=port)

    BULB.effect = effect
    BULB.transition_time = duration


@cli.command()
@click.argument("value", type=click.IntRange(1, 100, clamp=True))
def brightness(value):
    """Set the brightness of the bulb."""
    click.echo("Setting the bulb to {} brightness...".format(value))
    BULB.set_brightness(value, effect=BULB.effect, transition_time=BULB.transition_time)


@cli.command()
@click.argument("degrees", type=click.IntRange(1700, 6500, clamp=True))
def temperature(degrees):
    """Set the HSV value of the bulb."""
    click.echo("Setting the bulb's color temperature to {}...".format(degrees))
    BULB.set_color_temperature(degrees, effect=BULB.effect, transition_time=BULB.transition_time)


@cli.command()
@click.argument("hue", type=click.IntRange(0, 359, clamp=True))
@click.argument("saturation", type=click.IntRange(0, 100, clamp=True))
def hsv(hue, saturation):
    """Set the HSV value of the bulb."""
    click.echo("Setting the bulb to HSV {}, {}...".format(hue, saturation))
    # Work around bulb bug.
    if hue == saturation:
        hue += 1
    BULB.set_hsv_color(hue, saturation, effect=BULB.effect, transition_time=BULB.transition_time)


@cli.command()
@click.argument("red", type=click.IntRange(0, 255, clamp=True))
@click.argument("green", type=click.IntRange(0, 255, clamp=True))
@click.argument("blue", type=click.IntRange(0, 255, clamp=True))
def rgb(red, green, blue):
    """Set the RGB value of the bulb."""
    click.echo("Setting the bulb to RGB {}, {}, {}...".format(red, green, blue))
    BULB.set_rgb_color(red, green, blue, effect=BULB.effect, transition_time=BULB.transition_time)


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
        BULB.turn_on(effect=BULB.effect, transition_time=BULB.transition_time)
    elif state == "off":
        BULB.turn_off(effect=BULB.effect, transition_time=BULB.transition_time)


@cli.command()
def save():
    """Save the current settings as default."""
    click.echo("Saving settings...")
    BULB.save_state()


@cli.command()
def status():
    """Show the bulb's status."""
    click.echo("Bulb parameters:")
    for key, value in BULB.get_all_properties().items():
        click.echo("* {}: {}".format(key, value))

if __name__ == "__main__":
    cli()
