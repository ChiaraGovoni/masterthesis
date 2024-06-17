# Import libraries
import streamlit as st

def get_sales_approaches_resources(score):
    if score == 3:
        return ['Social Selling', 'Problem-Solving Selling', 'Need-Satisfaction Selling', 'Challenger Selling', 'Enterprise Selling', 'Consultative Selling', 'Value-based Selling' ]
    elif score == 2:
        return ['Social Selling', 'Problem-Solving Selling', 'Need-Satisfaction Selling', 'Challenger Selling', 'Enterprise Selling', 'Consultative Selling', 'Value-based Selling']
    elif score == 1:
        return ['Social Selling', 'Need-Satisfaction Selling']

def get_sales_channels_resources(score):
    if score == 3:
        return ['Internet', 'Telemarketing', 'Value-added intermediaries', 'Distributors', 'Trade Shows', 'Direct Sales Force']
    elif score == 2:
        return ['Internet', 'Telemarketing', 'Value-added intermediaries', 'Distributors', 'Trade Shows']
    elif score == 1:
        return ['Internet', 'Telemarketing', 'Value-added intermediaries', 'Distributors', 'Trade Shows']

def get_sales_approaches_innovation(score1, score2, approaches1):
    if score1 == 3:
        if score2 == 3:
            return ['Consultative Selling', 'Enterprise Selling', 'Value-based Selling']
        elif score2 == 2:
            return ['Consultative Selling','Problem-Solving Selling', 'Challenger Selling', 'Value-based Selling']
        elif score2 == 1:
            return ['Need-Satisfaction Selling', 'Problem-Solving Selling', 'Social Selling']
    elif score1 == 2:
        if score2 == 3:
            return ['Enterprise Selling', 'Consultative Selling', 'Value-based Selling', 'Challenger Selling']
        elif score2 == 2:
            return ['Challenger Selling', 'Problem-Solving Selling', 'Need-Satisfaction Selling', 'Social Selling']
        elif score2 == 1:
            return ['Social Selling', 'Need-Satisfaction Selling', 'Problem-Solving Selling']
    elif score1 == 1:
        if score2 == 3 or score2 == 2:
            return ['Need-Satisfaction Selling', 'Social Selling']
        elif score2 == 1:
            return ['Social Selling']

def get_sales_channels_innovation(score1, score2, channels1):
    if score1 == 3:
        if score2 == 3:
            return ['Direct Sales Force','Telemarketing']
        elif score2 == 2:
            return ['Value-added intermediaries', 'Distributors', 'Telemarketing']
        elif score2 == 1:
            return ['Value-added intermediaries', 'Trade Shows','Internet']
    elif score1 == 2:
        if score2 == 3:
            return ['Telemarketing', 'Internet', 'Trade Shows']
        elif score2 == 2:
            return ['Telemarketing', 'Value-added intermediaries', 'Distributors', 'Internet', 'Trade Shows']
        elif score2 == 1:
            return ['Internet', 'Value-added intermediaries', 'Distributors', 'Trade Shows']
    elif score1 == 1:
        if score2 == 3:
            return ['Internet', 'Trade Shows', 'Telemarketing']
        elif score2 == 2:
            return ['Trade Shows', 'Internet', 'Value-added intermediaries', 'Distributors']
        elif score2 == 1:
            return ['Internet', 'Trade Shows', 'Value-added intermediaries', 'Distributors']

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
st.markdown('This DSS was developed with to offer guidance to startups operating in the Cloud Computing sector and facing the so-called “Pioneer Problem”. This term describes the difficulties that innovative start-ups encounter in defining effective sales strategies in markets that are often new or little explored, where traditional paths may not be sufficient or adequate. Our DSS seeks to mitigate this problem by providing a structured framework for strategic orientation, helping startups identify the most promising sales approaches and channels based on their specific resources, product/service innovativeness level and customer needs. The code is the result of in-depth qualitative research carried out by interviewing sales experts and startup founders in the Cloud Computing sector. These conversations provided valuable insights that helped shape the decision tree at the heart of our tool. The tool framework has been further enriched and validated through a careful analysis of existing academic literature, thus ensuring that it is anchored in established practices as well as fundamental sales theories. One of the salient aspects that emerged during the validation phase of the tool concerns the importance of using this tool in a group context. It is strongly recommended that you complete the questionnaire as a team as this stimulates dialogue and collective reflection.In summary, the Sales DSS for Cloud Computing Startups does not aim to provide definitive answers but rather to guide startups through a process of self-reflection and strategic planning. It is a flexible tool, designed to adapt to the dynamic realities of Cloud Computing, offering startups a compass to more confidently navigate a complex and ever-changing market.') 

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
stat3 = st.select_slider('Our target customers need a consultative approach to selling, where we would acts as a long-term ally and help them achieve their strategic goals:', 
	options=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], key = 'stat3')
responses_approaches['Consultative Selling'] = lab_stat_3_14[stat3]

# STATEMENT 4
stat4 = st.select_slider('Our target customers need a cross-functional sales process, involving multiple departments from both sides (marketing, product, operations) to co-create value:', 
	options=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], key = 'stat4')
responses_approaches['Enterprise Selling'] = lab_stat_3_14[stat4]

# STATEMENT 5
stat5 = st.select_slider('Our target customers might benefit from new insights and ways of thinking about their industry. They might therefore need to interact with salespeople who act as new knowledge sources:', 
	options=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], key = 'stat5')
responses_approaches['Challenger Selling'] = lab_stat_3_14[stat5]

# STATEMENT 6
stat6 = st.select_slider('Our target customers are likely to enter the sales funnel without a direct interaction with sales personnel, therefore making use of the Internet and social media channels (e.g., LinkedIn) to learn more about their needs and possible solutions:',
	options=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], key = 'stat6')
responses_approaches['Social Selling'] = lab_stat_3_14[stat6]

# STATEMENT 7
stat7 = st.select_slider('Our target customers are often aware of the problem they face, its extent, and its implications. They seek tailored solutions for their unique needs:', 
	options=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], key = 'stat7')
responses_approaches['Need-Satisfaction Selling'] = lab_stat_3_14[stat7]

# STATEMENT 8
stat8 = st.select_slider('Our target customers are often not aware of the problem they face, its extent, and its implications.  They therefore need to be educated: ', 
	options=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], key = 'stat8')
responses_approaches['Problem-Solving Selling'] = lab_stat_3_14[stat8]

# STATEMENT 9
stat9 = st.select_slider('Our target customers need to see not only how the solution addresses their needs, but also how it brings value in terms of increased profits for the buying firm: ', 
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
	responses_channels['Direct Sales Force'] = lab_stat_3_14[stat10]
else:
	responses_channels['Telemarketing'] = lab_stat_3_14[stat10]

# STATEMENT 11
stat11 = st.select_slider('Our target market would be more effectively reached through partners who distribute our cloud service:',
	options=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], key = 'stat11')
responses_channels['Distributors'] = lab_stat_3_14[stat11]

# STATEMENT 12
stat12 = st.select_slider('For our target customer to purchase our product, it has to be commercialised through partners that enhance its value by adding  features or service:',
	options=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], key = 'stat12')
responses_channels['Value-added partners'] = lab_stat_3_14[stat12]

# STATEMENT 13
stat13 = st.select_slider('Our potential customers prefer the convenience and flexibility of easy online transactions:',
	options=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], key = 'stat13')
responses_channels['Internet'] = lab_stat_3_14[stat13]

# STATEMENT 14
stat14 = st.select_slider('Our target market frequently attends industry events, conferences, and trade shows:',
	options=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], key = 'stat14')
responses_channels['Trade Shows'] = lab_stat_3_14[stat14]

max_score_channels = max(responses_channels.values())
recommended_channels = [approach for approach, score in responses_channels.items() if score == max_score_channels]

mega_dict_1 = {
        'Consultative Selling': "Adopting a consultative selling approach means not only to provide a solution, but also helping customers achieve their own strategic goals. Consequently, in this case, salespeople fulfil three key roles during the sales process. Firstly, they act as ‘strategic orchestrators’, as they coordinate the selling firm’s resources to address customer challenges and opportunities. Secondly, they serve as ‘business consultants’, as they become experts in their field to educate clients about their own product, and the competitive landscape they face. Finally, they act as ‘long-term allies’, as they provide support to customers even if there are no immediate sales prospects. Because of this, as a sales approach, it is not only quite resource consuming and may therefore result in a particularly long sales cycle, but it may also be difficult to scale. The DSS recommended a consultative selling approach because: (1) you stated that your target customer need the selling firm to act as a long term partner that helps them achieve their own strategic goals and/or; (2) you stated that your sales department possesses a sufficient level of human and financial resources or is willing to invest in acquiring them and/or; (3) you stated the product you are offering presents a relatively high level of innovativeness and complexity.",
        'Enterprise Selling': "Enterprise selling is an extended form of consultative selling, where added value is not just delivered to the buyer, but co-created. This approach aims at establishing an integrated partnership where several departments and stakeholders from both organisations participate in the sales process. Thus, the seller and buyer firms engage in a deeper and cross-functional collaboration. In other words, enterprise selling goes beyond interactions between the sales department and the buying center as it involves additional departments such as marketing, operations, and product development from both the selling and buying firms. Because of this, as a sales approach it is quite resource consuming, and the sales cycle may be particularly long. The DSS recommended an enterprise selling approach because: (1) You stated that your target customer need a cross functional sales process, where multiple departments from both sides are involved to co-create value and/or; (2) you stated that your sales department possesses a sufficient level of human and financial resources or is willing to invest in acquiring them and/or; (3) you stated the product you are offering presents a relatively high level of innovativeness and complexity.",
        'Challenger Selling': "The core idea behind the Challenger Sale approach is to create constructive tension during the interaction with potential customers. This relatively new sales approach emerged because today's information rich B2B environment, buyers tend to analyse problems and solutions in a more meticulous way, which enhances their leverage during the sales pitch. This is mainly due to the fact that product and services are becoming increasingly complex and costly. The challenger sale approach therefore challenges customers to re-evaluate their ideas and beliefs about their industry, therefore facilitating an openness to new ideas. Consequently, salespeople act as 'knowledge brokers,' by understanding their customers' businesses and providing additional and relevant information. The DSS recommended a challenger selling approach because: (1) you stated that your target customer might benefit from new insights and ways of thinking about their industry and need salespeople to act as knowledge sources; and/or (2) you stated that your sales department possesses a sufficient level of human and financial resources or is willing to invest in acquiring them and/or; (3) you stated the product you are offering presents a relatively high level of innovativeness and complexity.",
        'Value-based Selling': "As the name would suggest, value-based selling develops around the core idea that, within B2B contexts, customers make a purchase either to create added value, that is either boosted revenue or reduced costs. Consequently, the role of the salespeople would be to demonstrate how the price the customer pays translates into benefits in terms of economic, service, technical, and social factors, and by communicating their monetary value for the buying firm. In other words, the selling organisation should focus their effort on the identification of value drivers in the customers’ operations, so that to understand how to contribute to their value creation process and have an impact on their overall businesses, and not just on solving the needs and pains of the customers. To do so, it is imperative for salespeople to fully understand the business model of the client, their situation, and the competitive landscape they face. They then need to clearly communicate a compelling, measurable, and impactful value proposition, as well as, in case of a successful deal, monitor and verify the delivery of value. The DSS recommended a value based selling approach because: (1) you stated that your target customer need to see not only how the solution addresses their needs, but also how it brings value in terms of increased profits for the buying firm and/or; (2) you stated that your sales department possesses a sufficient level of human and financial resources or is willing to invest in acquiring them and/or; (3) you stated the product you are offering presents a relatively high level of innovativeness and complexity.",
        'Problem-Solving Selling': "The problem-solving selling approach is based on the concept that customers may not fully comprehend or even recognise the scope and implications of their problems they might face. Consequently, the role of the salesperson is to first educate the buyers about the issues they face. They should then propose alternative solutions and present their offer. This approach may demand substantial resources, particularly in terms of time to understand the problem and make the prospective customer aware of it, making it sometimes impractical for both the seller and the buyer firms. The DSS recommended a problem solving selling approach because: (1) you stated that your target customer are often not aware of the problem they face, the extent of it, and its implications, and that they therefore need to be educated. (2) you stated that your sales department possesses a sufficient level of human and financial resources or is willing to invest in acquiring them.",
        'Need-Satisfaction Selling': "The underlying idea behind the need satisfaction selling approach is that customers buy to fulfil a specific need. In this case, the role of the salesperson is to identify this need and illustrate how the products or services satisfy that particular need, therefore providing a personalised approach and solution. The main advantage of this approach is that it allows prospective customers to feel they are making informed decisions independently, therefore decreasing the likelihood of them engaging defensive strategies during the sales process. The DSS recommended a need satisfaction selling approach because: (1) you stated that your target customer are often  aware of the problem they face, the extent of it, and its implications, and that they therefore seek tailored solutions for their needs and/or; (2) you stated that your sales department possesses a relatively low level of human and financial resources.",
        'Social Selling': "Social selling is a relatively new sales approach that involves the use of social and digital platforms to understand, engage and connect with both potential and existing customers. In other words, this approach primarily leverages the Internet and social media channels to interact directly with potential buyers. Social selling is becoming increasingly relevant as today’s buyers, also in B2B environments, often enter the sales funnel independently. As a matter of fact, a recent study indicates that over 80% of buyers acknowledges the influence of social media content on their purchasing decisions. Because of this, social selling is becoming increasingly relevant in B2B contexts. Furthermore, it enables reaching a broad market share at a relatively low cost and minimal resource demands. The DSS recommended a social selling approach because: (1) you stated that your target customer often use the Internet and social media channels (e.g., LinkedIn) to learn more about their needs and possible solutions and/or; (2) you stated that your sales department possesses a relatively low level of human and financial resources.",
        'Direct Sales Force': "A direct sales force is one of the most important sales channels in B2B interactions. It is the sales channel with the highest 'channel touch', i.e., where interactions between seller and buyer are most frequent, intense, and varied in their nature. Consequently, a direct sales force usually provides a very high level of added value to the buyer throughout the sales process. Obviously, however, this results in a very high cost per transaction, so sales force is considered by far the most expensive sales channel to operate. For this reason, it is used in the case of particularly complex products and services, where the sales cycle is very long. The DSS recommended a direct sales force because: (1) you stated that your target customer need a personal approach to selling, that is someone to talk to in person or over the phone and/or; (2) you stated that your sales department possesses a sufficient level of human and financial resources or is willing to invest in acquiring them and/or; (3) you stated the product you are offering presents a relatively high level of innovativeness and complexity.",
        'Telemarketing': "When using telemarketing the activities for engaging and interacting with both potential and existing customers are performed through the telephone. Compared to other sales channels, telemarketing offers three key benefits. Firstly, as it allows the selling firm to reach a wider customer base more frequently and at a relatively lower cost, it may boost revenue growth. Secondly, telemarketing is usually significantly cheaper than a direct sales force and thus enables a more effective and efficient customer segmentation. Thirdly, it provides customers with a more flexible and responsive option for interacting with the selling firm, potentially leading to an improved customer satisfaction and brand loyalty. The DSS recommended telemarketing because: (1) you stated that your target customer need a personal approach to selling, that is someone to talk to in person or over the phone and/or; (2) you stated that your sales department possesses a relatively low level of human and financial resources and/or;  (3) you stated the product you are offering presents a relatively high level of innovativeness and complexity.",
        'Value-added intermediaries': "Value added intermediaries are a particular kind of distributors that enhance the product by adding features, services, or by bundling it with complementary products before marketing it. In other words, they increase the value of your offering, which could not satisfy the needs of the target customers alone. The DSS recommend value added intermediaries as a sales channel because you stated that for your target customer to purchase the product, it should to be commercialised through partners that enhance its value by adding features or services.",
        'Distributors': "Distributors are intermediaries that take the product to market on behalf of the selling organization by using their own salesforce or other channels. The main reason why firms could opt for partnering  up with distributors would be to capture a larger market share at a relatively lower cost, especially in cases where the potential customer base is widely dispersed. This very often also results in added value for customers, who benefit from an enhanced and more effective customer service. The DSS recommended distributors as a sales channel because: (1) you stated that your target market would be more effectively reached through partners who distribute our cloud service and/or; (2) you stated that your sales department possesses a relatively low level of human and financial resources.",
        'Internet': "The Internet has gained more and more importance as a sales channel during the years. As a matter of fact, potential customers often enter the sales funnel independently, without interacting with selling personnel, by simply researching for solutions online. If we consider cost per transaction, the Internet is, by far, the most cost-effective sales channel and it offers three benefits compared to the others. Firstly, it expands the market reach of the selling firm at little variable costs. Secondly, it improves customer service and allows for more frequent interactions, therefore potentially enhancing customer loyalty. Finally, it relieves the most expensive sales channels of the ‘burden’ of small or routine transactions, allowing them to focus on more high-end accounts. The DSS recommended the Internet as a sales channel because: (1) you stated that your target customer prefer the convenience and flexibility of easy online transactions and/or; (2) you stated that your sales department possesses a relatively low level of human and financial resources.",
        'Trade Shows': "Trade shows are industry-specific events provide companies with an opportunity to showcase their products and services to potential, as well as existing customers. They can and should be seen as a physical platform that connects selling and buying organisations over a limited period of time. Because of this, it cannot be considered as the primary sales channel, but it may serve as an important component of a firm’s channel mix. As a matter of fact, trade shows can be useful in multiple ways, not only to close deals, but also for testing new products and gathering new information about the market, the competitive environment, and the evolving customer needs. The DSS recommended trade shows as a sales channel because you stated that your target customer frequently attends industry events, conferences, and trade shows."
    }

# Create a submit button
if st.button("Submit"):
	common_approaches = set(approaches_final).intersection(set(recommended_approaches))
	common_channels = set(channels_final).intersection(set(recommended_channels))


	asterisk_note = ""
	
	# Initialize a note for intensive resource approaches, if applicable
	if score1 == 2 and score2 == 3 and ('Consultative Selling' in common_approaches or 'Enterprise Selling' in common_approaches):
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
            
