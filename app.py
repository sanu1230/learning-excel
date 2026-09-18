import streamlit as st

from content import UNITS, all_chapters_flat

st.set_page_config(page_title="Excel Learning Course", page_icon=None, layout="wide")

FLAT_CHAPTERS = all_chapters_flat()
CHAPTER_BY_ID = {ch["id"]: ch for ch in FLAT_CHAPTERS}
CHAPTER_ORDER = [ch["id"] for ch in FLAT_CHAPTERS]

# ---------- session state ----------
if "current_id" not in st.session_state:
    st.session_state.current_id = CHAPTER_ORDER[0]
if "quiz" not in st.session_state:
    st.session_state.quiz = {}  # (chapter_id, q_idx) -> {"attempts": int, "revealed": bool, "solved": bool}
if "quiz_version" not in st.session_state:
    st.session_state.quiz_version = {}  # chapter_id -> int, bumped on reset to force radios to clear


def quiz_key(chapter_id, q_idx):
    return f"{chapter_id}__{q_idx}"


def get_quiz_state(chapter_id, q_idx):
    k = quiz_key(chapter_id, q_idx)
    if k not in st.session_state.quiz:
        st.session_state.quiz[k] = {"attempts": 0, "revealed": False, "solved": False}
    return st.session_state.quiz[k]


def go_to(chapter_id):
    st.session_state.current_id = chapter_id


def reset_quiz(chapter_id, num_questions):
    st.session_state.quiz_version[chapter_id] = st.session_state.quiz_version.get(chapter_id, 0) + 1
    for q_idx in range(num_questions):
        st.session_state.quiz.pop(quiz_key(chapter_id, q_idx), None)


# ---------- sidebar: free navigation ----------
with st.sidebar:
    st.title("Excel Learning Course")
    st.caption("Self-paced - jump to any chapter anytime.")
    for unit in UNITS:
        if not unit["chapters"]:
            with st.expander(f"Unit {unit['num']}: {unit['title']} (coming soon)", expanded=False):
                st.caption("Content not published yet.")
            continue
        with st.expander(f"Unit {unit['num']}: {unit['title']}", expanded=any(
            ch["id"] == st.session_state.current_id for ch in unit["chapters"]
        )):
            for ch in unit["chapters"]:
                label = f"{ch['num']}. {ch['title']}"
                is_current = ch["id"] == st.session_state.current_id
                st.button(
                    label,
                    key=f"nav_{ch['id']}",
                    on_click=go_to,
                    args=(ch["id"],),
                    use_container_width=True,
                    type="primary" if is_current else "secondary",
                )

# ---------- main area ----------
chapter = CHAPTER_BY_ID[st.session_state.current_id]
unit = next(u for u in UNITS if any(c["id"] == chapter["id"] for c in u["chapters"]))
idx_in_flat = CHAPTER_ORDER.index(chapter["id"])

st.caption(f"Unit {unit['num']}: {unit['title']}")
st.header(f"Chapter {chapter['num']}: {chapter['title']}")
progress_fraction = (idx_in_flat + 1) / len(CHAPTER_ORDER)
st.progress(progress_fraction, text=f"Chapter {idx_in_flat + 1} of {len(CHAPTER_ORDER)} in the course so far")

st.divider()

# --- Notes ---
st.subheader("Notes")
for bullet in chapter["notes"]:
    st.markdown(f"- {bullet}")

st.divider()

# --- Practice task ---
st.subheader("Practice: try this in your own Excel")
st.info("Open Excel on your computer for this part. Nothing here is checked - it's just for you to try.")
for i, step in enumerate(chapter["practice"], start=1):
    st.markdown(f"{i}. {step}")

st.divider()

# --- Quiz ---
quiz_header_col, quiz_reset_col = st.columns([4, 1])
with quiz_header_col:
    st.subheader("Quick check")
    st.caption("2 attempts per question, then the correct answer is shown. This doesn't block you from moving on.")
with quiz_reset_col:
    st.button(
        "Reset quiz",
        key=f"reset_{chapter['id']}",
        on_click=reset_quiz,
        args=(chapter["id"], len(chapter["quiz"])),
        use_container_width=True,
    )

quiz_version = st.session_state.quiz_version.get(chapter["id"], 0)

for q_idx, q in enumerate(chapter["quiz"]):
    state = get_quiz_state(chapter["id"], q_idx)
    st.markdown(f"**Q{q_idx + 1}. {q['q']}**")

    choice = st.radio(
        "Choose one:",
        options=q["options"],
        index=None,
        key=f"radio_{chapter['id']}_{q_idx}_{quiz_version}",
        label_visibility="collapsed",
        disabled=state["solved"] or state["revealed"],
    )

    col1, col2 = st.columns([1, 4])
    with col1:
        check_clicked = st.button(
            "Check answer",
            key=f"check_{chapter['id']}_{q_idx}_{quiz_version}",
            disabled=state["solved"] or state["revealed"] or choice is None,
        )

    if check_clicked and not state["solved"] and not state["revealed"]:
        state["attempts"] += 1
        chosen_idx = q["options"].index(choice)
        if chosen_idx == q["answer"]:
            state["solved"] = True
        elif state["attempts"] >= 2:
            state["revealed"] = True

    if state["solved"]:
        st.success("Correct.")
    elif state["revealed"]:
        st.warning(f"The correct answer is: {q['options'][q['answer']]}")
    elif state["attempts"] == 1:
        st.error("Not quite - one more try.")

    st.markdown("")

st.divider()

# --- Done / next chapter, no restriction ---
next_id = CHAPTER_ORDER[idx_in_flat + 1] if idx_in_flat + 1 < len(CHAPTER_ORDER) else None
if next_id:
    st.button("Done - Next Chapter", type="primary", on_click=go_to, args=(next_id,))
else:
    st.success("That's every chapter published so far. More units are on the way.")
