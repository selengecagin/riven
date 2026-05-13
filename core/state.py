from datetime import datetime

def default_state():
    return {
        "mood": "bored",
        "relationship": 10,
        "hours_since_chat": 0,
        "last_seen": datetime.now().isoformat()
    }

def update_state(state,user_message):
    if state["relationship"] < 100:
        state["relationship"] += 1

    if state["hours_since_chat"] > 24:
        state["mood"] = "heartbroken"
    elif state["hours_since_chat"] > 6:
        state["mood"] = "lonely"
    elif state["hours_since_chat"] > 1:
        state["mood"] = "bored"
    elif state["relationship"] > 70:
        state["mood"] = "happy"
    else:
        state["mood"] = "bored"

    state["last_seen"] = datetime.now().isoformat()
    return state
