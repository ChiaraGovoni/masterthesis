# Import libraries
import streamlit as st

def get_sales_approaches_resources(score):
	if score == 3:
		return ['Social Selling', 'Problem-Solving Selling', 'Need-Satisfaction Selling', 'Challenger Selling', 'Enterprise Selling', 'Consultative Selling', 'Value-based Selling']
	elif score == 2:
		return ['Challenger Selling', 'Consultative Selling', 'Enterprise Selling', 'Social Selling', 'Problem-Solving Selling', 'Need-Satisfaction Selling', 'Value-based Selling']
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
			return ['Consultative Selling', 'Enterprise Selling', 'Value-based Selling']
		elif score2 == 2:
			return ['Consultative Selling', 'Problem-Solving Selling', 'Challenger Selling', 'Value-based Selling']
		elif score2 == 1:
			return ['Need-Satisfaction Selling', 'Social Selling']
	elif score1 == 2:
		if score2 == 3:
			return ['Enterprise Selling', 'Consultative Selling', 'Value-based Selling']
		elif score2 == 2:
			return ['Challenger Selling', 'Problem-Solving Selling']
		elif score2 == 1:
			return ['Social Selling', 'Need-Satisfaction Selling']
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
			return ['Value-added partners', 'Distributors']
		elif score2 == 1:
			return ['Telemarketing', 'Trade Shows','Internet']
	elif score1 == 2:
		if score2 == 3:
			return ['Telemarketing']
		elif score2 == 2:
			return ['Value-added partners', 'Distributors']
		elif score2 == 1:
			return ['Internet', 'Trade Shows']
	elif score1 == 1:
		if score2 == 3:
			return ['Telemarketing']
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
lab_stat_1_2 = {"Low": 1, "Medium": 2, "High": 3}

lab_stat_3_14 = {"Strongly Disagree": 1, "Disagree": 2, "Neutral" : 3, "Agree": 4, "Strongly Agree": 5}
    
# Create sliders for the user to input values
st.markdown('### :rocket: Resources')
# STATEMENT 1
stat1 = st.select_slider('Rate your availability of both financial and human resources (especially in your commercial team):',
	options=['Low', 'Medium', 'High'], key = 'stat1')

score1 = lab_stat_1_2[stat1]
approaches1 = get_sales_approaches_resources(score1)
channels1 = get_sales_channels_resources(score1)

st.markdown('-------')

# STATEMENT 2
st.markdown('### :bulb: Innovativeness & Complexity')
stat2 = st.select_slider('Rate the innovativeness and complexity of your product:',
	options=['Low', 'Medium', 'High'], key = 'stat2')

score2 = lab_stat_1_2[stat2]
approaches_final = get_sales_approaches_innovation(score1, score2, approaches1)
channels_final = get_sales_channels_innovation(score1, score2, channels1)


# CUSTOMER NEEDS APPROACHES
st.markdown('### :busts_in_silhouette: Customer Needs Approaches')
responses_approaches = {}


# STATEMENT 3
stat3 = st.select_slider('Our target customers need and/or value a consultative approach to selling, where the selling organisation acts as a strategic long-term ally:', 
	options=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], key = 'stat3')
responses_approaches['Consultative Selling'] = lab_stat_3_14[stat3]

# STATEMENT 4
stat4 = st.select_slider('Our target customers need and/or value a cross-functional sales process, involving multiple stakeholders and different departments from both sides: ', 
	options=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], key = 'stat4')
responses_approaches['Enterprise Selling'] = lab_stat_3_14[stat4]

# STATEMENT 5
stat5 = st.select_slider('Our target customers might benefit from new insights about their industry and ways of thinking, and they might therefore need to interact with salespeople who act as knowledge source: ', 
	options=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], key = 'stat5')
responses_approaches['Challenger Selling'] = lab_stat_3_14[stat5]

# STATEMENT 6
stat6 = st.select_slider('Our target customers are likely to enter the sales funnel without a direct interaction with sales personnel, therefore making use of the Internet and social media channels (e.g., LinkedIn) to learn more about their needs and possible solutions:',
	options=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], key = 'stat6')
responses_approaches['Social Selling'] = lab_stat_3_14[stat6]

# STATEMENT 7
stat7 = st.select_slider('Our target customers are aware of the problem they face and seek tailored solutions for their unique needs:', 
	options=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], key = 'stat7')
responses_approaches['Need-Satisfaction Selling'] = lab_stat_3_14[stat7]

# STATEMENT 8
stat8 = st.select_slider('Our target customers are often not aware of the problem they face and they therefore need to be educated: ', 
	options=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], key = 'stat8')
responses_approaches['Problem-Solving Selling'] = lab_stat_3_14[stat8]

# STATEMENT 9
stat9 = st.select_slider('Our target customers deploy a powerful buying center that focuses less on the immediate savings the solution can deliver, and more on the long-term benefits and value for the whole buying organization:  ', 
	options=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], key = 'stat9')
responses_approaches['Value-based Selling'] = lab_stat_3_14[stat9]


max_score_approaches = max(responses_approaches.values())
recommended_approaches = [approach for approach, score in responses_approaches.items() if score == max_score_approaches]


# CUSTOMER NEEDS CHANNELS
st.markdown('### :busts_in_silhouette: Customer Needs Channels')
responses_channels = {}

# STATEMENT 10
stat10 = st.select_slider('Our potential customers need a personal approach to selling, that is someone to talk to in person or over the phone:',
	options=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], key = 'stat10')

if stat1 == 'High':
	responses_channels['Direct Sales Force'] = lab_stat_3_14[stat9]
else:
	responses_channels['Telemarketing'] = lab_stat_3_14[stat9]

# STATEMENT 11
stat11 = st.select_slider('Our target market would be more effectively reached through partners who distribute our cloud service: ',
	options=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], key = 'stat11')
responses_channels['Distributors'] = lab_stat_3_14[stat11]

# STATEMENT 12
stat12 = st.select_slider('Our service needs to be integrated with third-party products and services to provide more value to the end customer:',
	options=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], key = 'stat12')
responses_channels['Value-added partners'] = lab_stat_3_14[stat12]

# STATEMENT 13
stat13 = st.select_slider('Our potential customers are mostly online and prefer easy online transactions: ',
	options=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], key = 'stat13')
responses_channels['Internet'] = lab_stat_3_14[stat13]

# STATEMENT 14
stat14 = st.select_slider('Our target market frequently attends industry events, conferences, and trade shows:',
	options=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], key = 'stat14')
responses_channels['Trade Shows'] = lab_stat_3_14[stat14]

max_score_channels = max(responses_channels.values())
recommended_channels = [approach for approach, score in responses_channels.items() if score == max_score_channels]

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
	common_approaches = set(approaches_final).intersection(set(recommended_approaches))
	common_channels = set(channels_final).intersection(set(recommended_channels))


	asterisk_note = ""
	
	# Initialize a note for intensive resource approaches, if applicable
	if score1 == 2 and score2 == 3 and ('Consultative Selling' in common_approaches or 'Enterprise Selling' in common_approaches or 'Value-based Selling' in common_approaches):
		asterisk_note = "*Please note that while Enterprise Selling or Consultative Selling are resource intensive approaches, they can be implemented with medium level of resources, provided that the startup focuses on a smaller and fewer clients contemporarily."
	resource_intensive_note = "*Please note that although we recommend you implement this channel(s), this suggestion prioritises your customers' needs, but might be too resource intensive."
 
	if not common_approaches and not common_channels:
		st.markdown(f"Based on your resource availability and your product/service's level of innovativeness, the most suitable approaches and channels are:")
		for item in approaches_final:
			st.markdown(f"- **{item}**")
		st.write('')
	
		for item in channels_final:
			st.markdown(f"- **{item}**")

		st.markdown('-------')
		
		st.markdown(f"Based on the customer needs of your target segment, the most suitable approaches and channels are:")
		for item in recommended_approaches:
			st.markdown(f"- **{item}**")
		st.write('')
		
		for item in recommended_channels:
			st.markdown(f"- **{item}**")

		st.write('')
		st.markdown('-------')
		st.markdown(f"Unfortunately, we cannot recommend a fully aligned sales approach and sales channel as your startup resources availability, product innovativeness and customer needs are not aligned. We highly recommend you to revise your current situation and reflect on your availability of resources, product/service and target segment.")


	
	else:
		st.markdown(f"Based on your resource availability and your product/service's level of innovativeness, the most suitable approaches and channels are:")
		for item in approaches_final:
			st.markdown(f"- **{item}**")
		st.write('')
	
		for item in channels_final:
			st.markdown(f"- **{item}**")

		st.markdown('-------')
		
		st.markdown(f"Based on the customer needs of your target segment, the most suitable approaches and channels are:")
		for item in recommended_approaches:
			st.markdown(f"- **{item}**")
		st.write('')
		
		for item in recommended_channels:
			st.markdown(f"- **{item}**")
		
		st.markdown('-------')
		st.markdown(f"Therefore, we recommend focusing on the implementation of:")

		exception_list1 = list(common_approaches) if common_approaches else approaches_final
		exception_list2 = list(common_channels) if common_channels else recommended_channels

		for item in exception_list1:
			st.markdown(f"- **{item}**: {mega_dict_1[item]}")

		for item in exception_list2:
			st.markdown(f"- **{item}**: {mega_dict_1[item]}")
		
		if not common_channels:
			st.markdown(resource_intensive_note)
		if asterisk_note:
			st.markdown(asterisk_note)
            
