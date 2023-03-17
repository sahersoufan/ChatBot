# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


from typing import List
from typing import Text, Any, Dict

from rasa_sdk import Tracker, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet
# langid : pip install langid
import langid


class ActionRestart(Action):

  def name(self) -> Text:
      return "action_extract_slots"

  async def run(
      self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
  ) -> List[Dict[Text, Any]]:
      try:
        # custom behavior
        latest_message_text = tracker.latest_message.get('text')
        print(latest_message_text)
        if isinstance(latest_message_text, str) and langid.classify(latest_message_text)[0] == 'ar':
            # validation succeeded, capitalize the value of the "location" slot
            print(1)
            return [SlotSet("language", 'ar')]
        else:
            # validation failed, set this slot to None
            print(2)
            return [SlotSet("language", 'en')]
      except:
          return [SlotSet("language", 'en')]

#rasa run --enable-api --cors "*"