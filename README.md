# 🎓 Campus Assistant

A Python based campus assistant chatbot designed to help students with common academic and campus-related queries.

The system uses a **frame-based dialogue approach inspired by GUS**, maintains dialogue state across multiple turns, extracts relevant entities/slots, asks follow-up questions when information is missing, and provides responses using a predefined campus knowledge base.

The project includes a simple **Tkinter graphical user interface (GUI)** for interacting with the assistant.

---

## ✨ Features

- 💬 Conversational campus assistant
- 🧠 Frame-based dialogue management inspired by GUS
- 🔄 Dialogue-state tracking across multiple turns
- 🧩 Slot/entity extraction
- ❓ Follow-up questions for incomplete requests
- 📅 Class and timetable lookup
- 🏫 Classroom information through scheduled class lookup
- 📚 Library timing information
- 🎓 Academic FAQ support
- 🗂️ Menu-based handling for ambiguous/help requests
- 🖥️ Simple Tkinter graphical user interface
- 🧹 Clear-chat functionality with dialogue-state reset
- 🐍 Built using Python standard libraries

---

## 📌 Project Overview

The Campus Assistant is designed as a small frame-based dialogue system for student assistance.

Instead of treating every user message independently, the dialogue manager keeps track of the current **intent** and the information already provided by the user.

For example:

```text
User: Where is my Consumer Behaviour class?

Assistant: Which day order? (e.g., Day 1, Day 2)

User: Day 1

Assistant: Your Consumer Behaviour class on Day 1 is in Room LH: 1105
at 11:35 AM - 12:25 PM.
