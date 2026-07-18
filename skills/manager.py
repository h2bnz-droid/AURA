from skills.calculator import execute as calculator
from skills.reminder import execute as reminder
from skills.list_reminders import execute as list_reminders

def run(text):

    for skill in [
        calculator,
        reminder,
        list_reminders
   ]:

        result = skill(text)

        if result:
            return result

    return None