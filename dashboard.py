# Import libraries
import streamlit as st

def get_sales_approaches_resources(score):
	if score == 3:
		return ['Social Selling', 'Problem-Solving Selling', 'Need-Satisfaction Selling', 'Challenger Selling', 'Enterprise Selling', 'Consultative Selling']
	elif score == 2:
		return ['Challenger Selling', 'Enterprise Selling', 'Social Selling', 'Problem-Solving Selling', 'Need-Satisfaction Selling']
	elif score == 1:
		return ['Social Selling', 'Need-Satisfaction Selling']

def get_sales_channels_resources(score):
	if score == 3:
		return ['Internet', 'Telemarketing', 'Value-added partners', 'Distributors', 'Trade Shows', 'Direct Sales Force']
	elif score == 2:
		return ['Internet', 'Telemarketing', 'Value-added partners', 'Distributors', 'Trade Shows']
	elif score == 1:
		return ['Internet', 'Telemarketing', 'Trade Shows']

def get_sales_approaches_innovation(score1, score2, approaches1):
	if score1 == 3:
		if score2 == 3:
			return ['Consultative Selling', 'Enterprise Selling']
		elif score2 == 2:
			return ['Problem-Solving Selling', 'Need-Satisfaction Selling', 'Challenger Selling']
		elif score2 == 1:
			return ['Social Selling']
	elif score1 == 2:
		if score2 == 3:
			return ['Challenger Selling', 'Problem-Solving Selling', 'Enterprise Selling']
		elif score2 == 2:
			return ['Need-Satisfaction Selling', 'Enterprise Selling']
		elif score2 == 1:
			return ['Social Selling']
	elif score1 == 1:
		if score2 == 3 or score2 == 2:
			return ['Need-Satisfaction Selling', 'Social Selling']
		elif score2 == 1:
			return ['Social Selling']

def get_sales_channels_innovation(score1, score2, channels1):
	if score1 == 3:
		if score2 == 3:
			return ['Direct Sales Force', 'Telemarketing']
		elif score2 == 2:
			return ['Value-added partners', 'Distributors', 'Trade Shows', 'Telemarketing']
		elif score2 == 1:
			return ['Internet']
	elif score1 == 2:
		if score2 == 3:
			return ['Telemarketing', 'Trade Shows', 'Value-added partners']
		elif score2 == 2:
			return ['Value-added partners', 'Distributors']
		elif score2 == 1:
			return ['Internet', 'Value-added partners', 'Distributors']
	elif score1 == 1:
		if score2 == 3:
			return ['Telemarketing', 'Trade Shows']
		elif score2 == 2:
			return ['Telemarketing', 'Trade Shows', 'Internet']
		elif score2 == 1:
			return ['Internet', 'Trade Shows']

# Reduce margins of layout
st.set_page_config(layout = "wide")

# Hiding arrow from metric
st.write(
	"""
	<style>
	[data-testid="stMetricDelta"] svg {
		display: none;
	}
	</style>
	""",
	unsafe_allow_html=True)

# Insert title
st.title("Welcome to the Startup Sales Strategy Tool!")
st.markdown('Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum')

# Define a dictionary to map labels to numeric values
label_to_value = {"Low": 1, "Medium": 2, "High": 3}

    
# Create sliders for the user to input values

col1, col2, = st.columns(2, gap = 'large')
with col1:
	st.markdown('### :rocket: Resouces')
	# STATEMENT 1
	stat1 = st.select_slider('We dispose of adequate financial and human resources to potentially support a long and resource-intensive sales process or we are willing to invest to gain those resources',
		options=['Low', 'Medium', 'High'], key = 'stat1')

	score1 = label_to_value[stat1]
	approaches1 = get_sales_approaches_resources(score1)
	channels1 = get_sales_channels_resources(score1)

	st.markdown('-------')

	# STATEMENT 2
	st.markdown('### :bulb: Innovativeness & Complexity')
	stat2 = st.select_slider('Our cloud computing service represents an entirely new, innovative, and complex product in the market',
		options=['Low', 'Medium', 'High'], key = 'stat2')

	score2 = label_to_value[stat2]
	approaches_final = get_sales_approaches_innovation(score1, score2, approaches1)
	channels_final = get_sales_channels_innovation(score1, score2, channels1)

with col2:
	responses = {}
	st.markdown('### :busts_in_silhouette: Customer Needs & Understanding')
	# STATEMENT 3
	stat3 = st.select_slider('We engage with clients who value strategic partnerships',
		options=['Low', 'Medium', 'High'], key = 'stat3')
	responses['Consultative Selling'] = label_to_value[stat3]

	# STATEMENT 4
	stat4 = st.select_slider('Our clients require comprehensive solutions across their organization',
		options=['Low', 'Medium', 'High'], key = 'stat4')
	responses['Enterprise Selling'] = label_to_value[stat4]

	# STATEMENT 5
	stat5 = st.select_slider('Our customers might benefit from new insights and ways of thinking',
		options=['Low', 'Medium', 'High'], key = 'stat5')
	responses['Challenger Selling'] = label_to_value[stat5]

	# STATEMENT 6
	stat6 = st.select_slider('We serve a tech-savvy customer base that prefers digital engagement',
		options=['Low', 'Medium', 'High'], key = 'stat6')
	responses['Social Selling'] = label_to_value[stat6]

	# STATEMENT 7
	stat7 = st.select_slider('Our customers seek tailored solutions for their unique needs',
		options=['Low', 'Medium', 'High'], key = 'stat7')
	responses['Need-Satisfaction Selling'] = label_to_value[stat7]

	# STATEMENT 8
	stat8 = st.select_slider('Our clients often require detailed explanations and demonstrations',
		options=['Low', 'Medium', 'High'], key = 'stat8')
	responses['Problem-Solving Selling'] = label_to_value[stat8]

	max_score = max(responses.values())
	customer_approaches = [approach for approach, score in responses.items() if score == max_score]

mega_dict_1 = {
	"Social Selling" : "Descrizione a caso",
	'Problem-Solving Selling': "Descrizione a caso",
	'Need-Satisfaction Selling' : "Descrizione a caso",
	'Challenger Selling' : "Descrizione a caso",
	'Enterprise Selling': "Descrizione a caso",
	'Consultative Selling': "Descrizione a caso",
	'Internet' : "Descrizione a caso",
	'Telemarketing' : "Descrizione a caso", 
	'Value-added partners' : "Descrizione a caso",
	'Distributors' : "Descrizione a caso",
	'Trade Shows' : "Descrizione a caso",
	'Direct Sales Force' : "Descrizione a caso",
	}

# Create a submit button
if st.button("Submit"):
	common_approaches = set(approaches_final).intersection(set(customer_approaches))
	if common_approaches:
		if len(common_approaches) == len(customer_approaches):
			st.write('The most suitable approaches are:')
			for item in approaches_final:
				st.markdown(f"- **{item}**: {mega_dict_1[item]}")
			st.write('')
			st.markdown('-------')
	
			st.write('The most suitable channels are:')
			for item in channels_final:
				st.markdown(f"- **{item}**: {mega_dict_1[item]}")
	
			st.markdown('-------')
			st.write('Based on the customer needs of your target segment, the same approaches are most appropriate:')
			for item in common_approaches:
				st.markdown(f"- **{item}**: {mega_dict_1[item]}")
		else:
			st.write('The most suitable approaches are:')
			for item in approaches_final:
				st.markdown(f"- **{item}**: {mega_dict_1[item]}")
			st.write('')
			st.markdown('-------')
	
			st.write('The most suitable channels are:')
	
			for item in channels_final:
				st.markdown(f"- **{item}**: {mega_dict_1[item]}")
			st.markdown('-------')
			st.write('Based on the customer needs of your target segment, the appropriate approaches can include both')
			for item in list(common_approaches):
				st.markdown(f"- **{item}**: {mega_dict_1[item]}")
	
			for item in list(set(customer_approaches) - common_approaches):
				st.markdown(f"- **{item}**: {mega_dict_1[item]}")
	
	else:
		st.write('The most suitable approaches are:')
		for item in approaches_final:
			st.markdown(f"- **{item}**: {mega_dict_1[item]}")
		st.write('')
		st.markdown('-------')
	
		st.write('The most suitable channels are:')
		for item in channels_final:
			st.markdown(f"- **{item}**: {mega_dict_1[item]}")
	
		st.markdown('-------')
		st.write('However, based on the customer needs of your target segment, the most suitable approaches are:')
		for item in customer_approaches:
			st.markdown(f"- **{item}**: {mega_dict_1[item]}")
