import utils
import subprocess
import webbrowser

def launch(name):
    # disable some ongoing stuff
    subprocess.run(["playerctl", "pause"])
    subprocess.run(["hyprctl", "eval", 'hl.dispatch(hl.dsp.window.fullscreen({ action = "unset" }))'])

    subject = utils.subjects[name]
    webbrowser.open(subject["link"])