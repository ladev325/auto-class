#!/usr/bin/env python3
import utils
import schedule as sc

utils.notify("[AutoLesson] Started", 3000)
was_exception = False
try:
    sc.schedule_daemon()

except KeyboardInterrupt:
    utils.notify("[AutoLesson] Task was killed (KeyboardInterrupt)", 0, True)
    was_exception = True
except Exception:
    utils.notify("[AutoLesson] Crashed (unknown exception)", 0, True)
    was_exception = True
finally:
    if not was_exception:
        utils.notify("[AutoLesson] Task was killed", 0, True)