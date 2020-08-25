
from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction


class auditform(FormAction):
    def name(self):
        return("audit_form")
    
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        if tracker.get_slot('did_audit') == False:
            return ["did_audit"]
        else:
            return ["did_audit", "course"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

        return {
            "course": self.from_entity(entity="course", intent="inform"),
            "did_audit": [
                self.from_intent(intent="affirm", value=True),
                self.from_intent(intent="deny", value=False),
            ],
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
        ) -> List[Dict]:
        print("successful")
        did_audit = tracker.get_slot('did_audit')
        course = tracker.get_slot('course')
        print(did_audit)
        print(course)
        # populate_table(tracker)
        return[]


