from __future__ import print_function
import subprocess
import platform
import os

from BinPy.__init__ import *
try:
    from BinPy import __version__ as BINPY_VERSION
except ImportError:
    BINPY_VERSION = ""


def shellclear():
    if platform.system() == "Windows":
        return
    subprocess.call("clear")


def magic_clear(self, arg):
    shellclear()

banner = '+-----------------------------------------------------------+\n'
banner += ' BinPy '
banner += BINPY_VERSION
banner += ' [interactive shell]\n'
banner += '+-----------------------------------------------------------+\n'
banner += '\n'
banner += 'Commands: \n'
banner += '\t"exit()" or press "Ctrl+ D" to exit the shell\n'
banner += '\t"clear()" to clear the shell screen\n'
banner += '\n'

exit_msg = '\n... [Exiting the BinPy interactive shell] ...\n'


def self_update():
    URL = "https://github.com/binpy/binpy/zipball/master"
    command = "pip install -U %s" % URL

    if os.getuid() == 0:
        command = "sudo " + command

    returncode = subprocess.call(command, shell=True)
    sys.exit()


def setupIpython():

    try:
        import IPython
    except:
        raise("ERROR: IPython Failed to load")

    try:
        from IPython.config.loader import Config
        from IPython.frontend.terminal.embed import InteractiveShellEmbed

        cfg = Config()
        cfg.PromptManager.in_template = "BinPy:\\#> "
        cfg.PromptManager.out_template = "BinPy:\\#: "
        bpyShell = InteractiveShellEmbed(config=cfg, banner1=banner,
                                         exit_msg=exit_msg)
        bpyShell.define_magic("clear", magic_clear)

    except ImportError:
        try:
            from IPython.Shell import IPShellEmbed
            argsv = ['-pi1', 'BinPY:\\#>', '-pi2', '   .\\D.:', '-po',
                     'BinPy:\\#>', '-nosep']
            bpyShell = IPShellEmbed(argsv)
            bpyShell.set_banner(banner)
            bpyShell.set_exit_msg(exit_msg)
        except ImportError:
            raise

    return bpyShell()


def run_notebook(mainArgs):
    """Run the ipython notebook server"""

    try:
        import IPython
    except:
        raise("ERROR: IPython Failed to load")

    try:
        from IPython.html import notebookapp
        from IPython.html.services.kernels import kernelmanager
    except:
        from IPython.frontend.html.notebook import notebookapp
        from IPython.frontend.html.notebook import kernelmanager

    kernelmanager.MappingKernelManager.first_beat = 30.0
    app = notebookapp.NotebookApp.instance()
    with open('BinPyNotebook0.ipynb', 'a') as new_ipynb:
        if (new_ipynb.tell() == 0):
            new_ipynb.write(
                """
                {
                "metadata": {
                "name": "",
                "signature": ""
                },
                "nbformat": 3,
                "nbformat_minor": 0,
                "worksheets": [
                {
                "cells": [
                    {
                    "cell_type": "code",
                    "collapsed": false,
                    "input": [
                    "from BinPy import *"
                    ],
                    "language": "python",
                    "metadata": {},
                    "outputs": [],
                    "prompt_number": 1
                    }
                ],
                "metadata": {}
                }
                ]
                }
            """
            )

    app.initialize(['BinPyNotebook0.ipynb'])
    app.start()
    sys.exit()


def shellMain(*args):
    log_level = logging.WARNING
    interface = None

    if len(sys.argv) > 1 and len(sys.argv[1]) > 1:
        flag = sys.argv[1]
        print (flag)

        if flag == 'update':
            print ("Updating BinPy...")
            self_update()

        elif flag == 'notebook':
            run_notebook(['.'])
            sys.exit()

        if flag in ['--nowarnings', 'nowarnings']:
            log_level = logging.INFO
        elif flag in ['--debug', 'debug']:
            log_level = logging.DEBUG

    init_logging(log_level)
    shellclear()
    bpyShell = setupIpython()
