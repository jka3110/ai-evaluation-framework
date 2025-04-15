import streamlit as st

st.set_page_config(page_title="AI Evaluation Framework", layout="centered")

if "step" not in st.session_state:
    st.session_state.step = 1

def restart():
    st.session_state.step = 1

def next_step():
    st.session_state.step += 1

# Display title
st.title("🧠 AI Evaluation Framework")

# Logic for each screen
if st.session_state.step == 1:
    st.header("Is the output specific and verifiable?")
    if st.button("✅ Yes"):
        next_step()
    if st.button("❌ No"):
        st.warning("Reprompt and ask for sources or clarification.")
        restart()

elif st.session_state.step == 2:
    st.header("Does the output cite credible sources?")
    if st.button("✅ Yes"):
        next_step()
    if st.button("❌ No"):
        st.error("Possible misinformation. Investigate claims manually.")
        next_step()

elif st.session_state.step == 3:
    st.header("Can you cross-check the information with trusted sources?")
    if st.button("✅ Yes"):
        st.success("Good! ✅ Validate Claims")
        next_step()
    if st.button("❌ No"):
        st.warning("Output may not be reliable.")
        next_step()

elif st.session_state.step == 4:
    st.header("Is there internal logic and consistency in the output?")
    if st.button("✅ Yes"):
        next_step()
    if st.button("❌ No"):
        st.warning("Check for contradictions or ask AI to rephrase.")
        next_step()

elif st.session_state.step == 5:
    st.header("Does the output cover major counterarguments or uncertainties?")
    if st.button("✅ Yes"):
        next_step()
    if st.button("❌ No"):
        st.warning("Potential bias. Consider restarting.")
        restart()

elif st.session_state.step == 6:
    st.header("Does the output oversimplify the issue?")
    if st.button("✅ Yes"):
        st.warning("Ask for nuance to dive deeper.")
        next_step()
    if st.button("❌ No"):
        next_step()

elif st.session_state.step == 7:
    st.header("Could the AI be mirroring online bias?")
    if st.button("✅ Yes"):
        st.warning("Be skeptical — AI could reflect training data.")
    if st.button("❌ No"):
        st.success("More likely to be balanced.")

# Restart button at bottom
st.markdown(
    "<div style='position: fixed; bottom: 20px; right: 20px;'>"
    "<form action='#'><input type='submit' value='🔁 Restart' onclick='window.location.reload();' "
    "style='font-size:18px; padding:8px 16px;'></form></div>",
    unsafe_allow_html=True
)
