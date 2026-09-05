import utils
import launch as lc
from datetime import datetime
import time

def get_schedule_subject():
    today_schedule = utils.schedule[datetime.now().weekday()]
    subject = None

    if len(today_schedule) > 0:
        now = datetime.now()
        for i in range(len(today_schedule)):
            s = today_schedule[i]
            start_time = datetime.strptime(s["start_time"], "%H:%M")
            end_time = datetime.strptime(s["end_time"], "%H:%M")
            start_full_date = now.replace(
                hour=start_time.hour, minute=start_time.minute, second=0, microsecond=0
            )
            end_full_date = now.replace(
                hour=end_time.hour, minute=end_time.minute, second=0, microsecond=0
            )

            if now > start_full_date and now < end_full_date:
                 subject = s
                 break    
    return subject


def get_subject_message(schedule_subject):
    info_subject = utils.subjects[schedule_subject["name"]]
    duration_message = "[" + schedule_subject["start_time"] + "-" + schedule_subject["end_time"] + "] "
    return duration_message + info_subject["name"]


prev_subject = None
def schedule_daemon():
    global prev_subject
    while True:
        utils.update_files()
        schedule_subject = get_schedule_subject()
        if prev_subject != schedule_subject and schedule_subject is not None:
            prev_subject = schedule_subject
            utils.notify(get_subject_message(schedule_subject), 0)
        time.sleep(utils.CHECK_INTERVAL)


def run_subject():
    utils.update_files()
    schedule_subject = get_schedule_subject()
    if schedule_subject:
        utils.notify(get_subject_message(schedule_subject), 2000)
        lc.launch(schedule_subject["name"])
    else:
        utils.notify("🚫 No subjects by now", 1000)