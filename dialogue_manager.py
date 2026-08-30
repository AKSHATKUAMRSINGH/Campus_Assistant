# dialogue_manager.py
from data import TIMETABLE, FAQS, SUBJECTS, DAYS
import datetime

class DialogueManager:
    """
    Implements a frame-based dialogue system inspired by GUS.
    Tracks slots required for specific intents and asks follow-up questions
    if information is missing.
    """
    def __init__(self):
        self.state = {
            "intent": None,
            "slots": {}
        }
        
        # Define what slots are mandatory for each query type
        self.required_slots = {
            "find_class": ["subject", "day"],
            "todays_classes": ["day"],
            "faq": ["topic"],
            "library_timing": []
        }
        
    def reset_state(self):
        """Clear conversation state after fulfilling a request."""
        self.state["intent"] = None
        self.state["slots"] = {}
        
    def extract_entities(self, text):
        """Extracts known entities (day, subject, faq topic) from user input."""
        text = text.lower()
        entities = {}
        
        # 1. Extract Day Order
        for day in DAYS:
            if day.lower() in text:
                entities["day"] = day
                break
                
        # Handle just the number? If user replies "1", we map to "Day 1"
        if not entities.get("day"):
            # Simple check for standalone numbers 1-5
            words = text.split()
            for word in words:
                if word in ["1", "2", "3", "4", "5"]:
                    entities["day"] = f"Day {word}"
                    break

        # 2. Extract Subject
        for sub in SUBJECTS:
            if sub.lower() in text:
                entities["subject"] = sub
                break
                
        # 3. Extract FAQ topic
        for topic in FAQS.keys():
            if topic in text:
                entities["topic"] = topic
                break
                
        return entities

    def identify_intent(self, text, entities):
        """Determines the user's intent based on keywords and extracted entities."""
        text_lower = text.lower()
        
        # Handle Utility-based Menu Choice
        if self.state["intent"] == "awaiting_menu_selection":
            if "1" in text_lower or "classroom" in text_lower:
                return "find_class"
            elif "2" in text_lower or "library" in text_lower:
                return "library_timing"
            elif "3" in text_lower or "timetable" in text_lower:
                return "todays_classes"
            elif "4" in text_lower or "faq" in text_lower:
                return "faq"
            else:
                return "awaiting_menu_selection"
                
        # Heuristic intent mapping
        if "library" in text_lower:
            return "library_timing"
        elif "class" in text_lower or "where is" in text_lower or "room" in text_lower or "subject" in text_lower:
            # Distinguish between finding a specific class and today's schedule
            if "today" in text_lower and ("all" in text_lower or "schedule" in text_lower):
                return "todays_classes"
            return "find_class"
        elif "timetable" in text_lower or "schedule" in text_lower:
            return "todays_classes"
        elif "help" in text_lower or "what can you do" in text_lower or "menu" in text_lower:
            return "menu"
        elif entities.get("topic") and not self.state["intent"]:
            return "faq"
        elif "faq" in text_lower or "question" in text_lower or "ask" in text_lower:
            return "faq"
            
        return None

    def process_input(self, user_input):
        """Main entry point to process a single turn of user input."""
        entities = self.extract_entities(user_input)
        
        # If we are already tracking an intent (and not waiting for menu), just absorb new slots
        if self.state["intent"] and self.state["intent"] != "awaiting_menu_selection":
            for key, value in entities.items():
                self.state["slots"][key] = value
                
            # Fallback for ambiguous FAQ topics when asking follow up
            if self.state["intent"] == "faq" and not entities.get("topic"):
                for topic in FAQS.keys():
                    # Check if any word in the topic matches the input
                    if any(word in user_input.lower() for word in topic.split() if len(word) > 3):
                        self.state["slots"]["topic"] = topic
                        break
        else:
            # Identify intent for a new conversation turn
            intent = self.identify_intent(user_input, entities)
            
            # Fallback to Utility Menu if ambiguous or requested
            if intent == "menu" or intent is None:
                self.state["intent"] = "awaiting_menu_selection"
                return ("What do you need?\n"
                        "1. Classroom\n"
                        "2. Library\n"
                        "3. Timetable\n"
                        "4. Academic FAQ")
            elif intent == "awaiting_menu_selection":
                return "Please select a valid option from 1 to 4."
            else:
                self.state["intent"] = intent
                self.state["slots"] = entities

        return self.execute_state()

    def execute_state(self):
        """Checks if all required slots are filled, and either asks for missing slots or executes."""
        intent = self.state["intent"]
        slots = self.state["slots"]
        req_slots = self.required_slots.get(intent, [])
        
        # Check for missing slots
        missing_slots = [slot for slot in req_slots if slot not in slots]
        
        # Ask follow-up question if slots are missing
        if missing_slots:
            missing_slot = missing_slots[0]
            if missing_slot == "subject":
                return f"Which subject? (Available: {', '.join(SUBJECTS)})"
            elif missing_slot == "day":
                return "Which day order? (e.g., Day 1, Day 2)"
            elif missing_slot == "topic":
                # Show a preview of available topics
                topics_preview = ", ".join(list(FAQS.keys())[:5])
                return f"What FAQ topic are you looking for? (e.g., {topics_preview}...)"
                
        # All required slots are filled, execute action
        response = ""
        if intent == "find_class":
            day = slots["day"]
            subject = slots["subject"]
            day_schedule = TIMETABLE.get(day, {})
            
            # Resolve exact case for output
            matched_subject = None
            for s in day_schedule.keys():
                if s.lower() == subject.lower():
                    matched_subject = s
                    break
                    
            if matched_subject:
                info = day_schedule[matched_subject]
                response = f"Your {matched_subject} class on {day} is in Room {info['room']} at {info['time']}."
            else:
                response = f"You don't have a {subject} class on {day}."
                
        elif intent == "todays_classes":
            day = slots["day"]
            day_schedule = TIMETABLE.get(day, {})
            if day_schedule:
                classes = [f" - {sub}: {info['time']} in Room {info['room']}" for sub, info in day_schedule.items()]
                response = f"Here is the timetable for {day}:\n" + "\n".join(classes)
            else:
                response = f"You have no classes scheduled on {day}."
                
        elif intent == "library_timing":
            response = FAQS["library timing"]
            
        elif intent == "faq":
            topic = slots["topic"]
            response = FAQS.get(topic, "I don't have information on that topic.")
            
        # Reset state after successfully handling the request
        self.reset_state()
        return response
