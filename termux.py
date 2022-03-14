import subprocess
import sys
import time
import json
import argparse

from functools import partial
from fabric import Connection

argv = sys.argv
print(argv)
c = Connection("192.168.86.197:23189")

# Prefix with 'termux-' to run in shell
termux_api_cmds = {
    "battery-status",
    "brightness",
    "call-log",
    "camera-info",
    "camera-photo",
    "clipboard-get",
    "clipboard-set",
    "contact-list",
    "dialog",
    "download",
    "fingerprint",
    "infrared-frequencies",
    "infrared-transmit",
    "job-scheduler",
    "location",
    "media-player",
    "media-scan",
    "microphone-record",
    "notification",
    "notification-remove",
    "sensor",
    "share",
    # "sms-list",
    "sms-send",
    "storage-get",
    "telephony-call",
    "telephony-cellinfo",
    "telephony-deviceinfo",
    "toast",
    "torch",
    "tts-engines",
    "tts-speak",
    "usb",
    "vibrate",
    "volume",
    "wallpaper",
    "wifi-connectioninfo",
    "wifi-enable",
    "wifi-scaninfo",
}

# pprint(termux_api_cmds)


def run(cmd, **kwargs):

    # args = []
    args = kwargs.get("args")

    if cmd in termux_api_cmds:
        cmd = cmd
    else:
        print("do nothing")
        return False

    cmd = "termux-" + cmd

    if not args == None:
        cmd = cmd + " " + args

    try:
        result = c.run(cmd)
        print(result)
        r = list(result)
        # json_result = json.load(result)
        print(r)
    except KeyboardInterrupt:
        sys.exit()
    except Exception as e:
        print(e, "error has happend")
        time.sleep(2)
        sys.exit()


def toast(**kwargs):
    run(cmd="toast")


def notification(**kwargs):
    if get.kwargs["title"]:
        title = kwargs["title"]
    else:
        title = "Testes"

    if get.kwargs["content"]:
        content = kwargs["content"]
    else:
        content = "Beep, Boop"

    cmd = "termux-notification --title " + title + "--content " + content
    result = c.run(cmd)
    return result


def smslist(**kwargs):
    print("red")
    run(cmd="sms-list")


def wifi_scaninfo(**kwargs):
    run(cmd="wifi-scaninfo")
    cmd = "termux-wifi-scaninfo"
    result = c.run(cmd)
    return result


def microphone_record(**kwargs):
    cmd = "termux-microphone-record -f test2.aac -e aac -l 10"
    result = c.run(cmd)
    return result


def battery_status():
    cmd = "termux-battery-status"
    result = c.run(cmd)
    return result


def telephony_cellinfo():
    cmd = "termux-telephony-cellinfo"
    result = c.run(cmd)
    return result


def dialog():
    cmd = "termux-dialog"
    subcmds = [
        "confirm",
        "checkbox",
        "counter",
        "date",
        "radio",
        "sheet",
        "spinner",
        "speech",
        "text",
        "time",
    ]
    result = c.run(cmd)
    return result


kcmds = [
    "smslist()",
    wifi_scaninfo(),
    michrophone_record(),
    battery_status(),
    telephony_cellinfo(),
    dialog(),
    toast(),
    notification(),
]


def main2(args):
    # command = args[1]
    if len(args) == 1:
        print("Need at least 1 arg")
        sys.exit()
    elif command in kcmds:
        print(cmds)
        print(command, "command")
        # command
    else:
        print(command, "is not a known command")
    try:
        print("2")
    except KeyboardInterrupt:
        sys.exit()
    except Exception as e:
        print(e, "error has happend")
        time.sleep(2)
        sys.exit()


if __name__ == "__main__":
    main2(argv)
