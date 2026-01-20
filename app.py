import streamlit as st
import random
import time

st.set_page_config(
    page_title="Awkward Sorting Hat",
    page_icon="🧢",
)

st.title("🧢 The Awkward Sorting Hat")
st.caption("Please don’t make eye contact. This is hard enough already.")

houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

questions = [
    (
        "Someone cuts in line in front of you. You:",
        {
            "Say something immediately (voice cracks a little)": "Gryffindor",
            "Let it go but judge them silently for years": "Hufflepuff",
            "Analyze whether confrontation is statistically worth it": "Ravenclaw",
            "Remember their face. This will matter later.": "Slytherin",
        },
    ),
    (
        "Your group chat goes quiet after your message. You:",
        {
            "Double-text. Confidence is a choice.": "Gryffindor",
            "Assume everyone is busy and it’s totally fine (it’s fine)": "Hufflepuff",
            "Reread the message 12 times for tone issues": "Ravenclaw",
            "Delete it. Power move.": "Slytherin",
        },
    ),
    (
        "A stranger talks to you in public. You:",
        {
            "Roll with it. New friend unlocked.": "Gryffindor",
            "Are polite and emotionally available": "Hufflepuff",
            "Panic internally but respond appropriately": "Ravenclaw",
            "Immediately suspect an ulterior motive": "Slytherin",
        },
    ),
    (
        "You make a mistake in front of others. You:",
        {
            "Laugh it off loudly": "Gryffindor",
            "Apologize excessively": "Hufflepuff",
            "Replay it in your head forever": "Ravenclaw",
            "Pretend it was intentional": "Slytherin",
        },
    ),
    (
        "Your ideal role in a group project:",
        {
            "Leader (someone has to do it)": "Gryffindor",
            "Supporter (glue of the group)": "Hufflepuff",
            "Researcher (please don’t make me present)": "Ravenclaw",
            "Strategist (credit negotiator)": "Slytherin",
        },
    ),
]

# Initialize state
if "scores" not in st.session_state:
    st.session_state.scores = {house: 0 for house in houses}

answers = []

for i, (question, options) in enumerate(questions):
    choice = st.radio(
        question,
        list(options.keys()),
        key=f"q{i}",
    )
    answers.append(options[choice])

if st.button("😬 Sort me, I guess"):
    for house in answers:
        st.session_state.scores[house] += 1

    with st.spinner("Thinking… overthinking… spiraling…"):
        time.sleep(2)

    top_score = max(st.session_state.scores.values())
    top_houses = [
        house for house, score in st.session_state.scores.items()
        if score == top_score
    ]

    result = random.choice(top_houses)

    st.subheader("🎩 …Well this is awkward.")
    st.write("I’ve seen worse. I’ve seen better. Mostly I’ve seen *you*.")

    st.success(f"🏰 You’re a **{result}**.")

    awkward_comments = {
        "Gryffindor": "Bold. Loud. Emotionally impulsive. Respect.",
        "Hufflepuff": "Kind. Loyal. Apologized to this app at least once.",
        "Ravenclaw": "Smart. Overthinking this result already.",
        "Slytherin": "Ambitious. You knew this before clicking the button.",
    }

    st.caption(awkward_comments[result])

    st.write("…Please remove the hat. I need a moment.")

    if st.button("🔁 Re-sort (I don’t trust this)"):
        st.session_state.scores = {house: 0 for house in houses}
        st.experimental_rerun()
