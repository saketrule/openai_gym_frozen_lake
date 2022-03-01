import streamlit as st
import gym

st.title("Frozen Lake")
st.subheader("Falabella Reinforcement Learning bootcamp!")
st.markdown('-------')
st.text("")
st.text("")
st.text("")

game = "FrozenLake-v1"
action_map = {
	'Up': 3,
	'Down': 1,
	'Left': 0,
	'Right': 2
}

# Utility functions
def initialize_game(game=game, is_slippery=True):
	env = gym.make(game, is_slippery=is_slippery)
	env.reset()
	st.session_state['env'] = env
	return env


def render_state(action=None):
	env = st.session_state['env']
	done = False
	if action:
		obs, reward, done, info = env.step(action_map[action])
	state = env.render('rgb_array')
	state_comp.image(state)
	if done:
		st.success(f"Episode Done! - You got reward {reward}")
		if reward > 0:
			st.balloons()


# Initialize
if 'env' not in st.session_state:
	initialize_game(game)


# Create display state component
col1, col2 = st.columns([1,1])

with col1:
	state_comp = st.empty()

with col2:

	reset_comp = st.button("Reset")
	
	# Create actions radio
	with st.form(key='action', clear_on_submit=False):
		action_select_comp = st.radio('Select Action:', action_map.keys())
		step_comp = st.form_submit_button("Step")
		if step_comp:
			render_state(action_select_comp)




render_state()

slippery_comp = st.sidebar.markdown("Game Options")
slippery_comp = st.sidebar.checkbox("Slippery ?", value=True)

if reset_comp:
	initialize_game(game, is_slippery=slippery_comp)
	render_state()

