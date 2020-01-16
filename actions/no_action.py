import action

"""
no action is needed for this event
"""
class NoAction(action.Action):
    def run(self):
        print("no action needed")
        return "no action"