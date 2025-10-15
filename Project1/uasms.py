import signal
import sys

if not sys.platform.startswith("win"):
    signal.signal(signal.SIGINT, signal.SIG_DFL)
