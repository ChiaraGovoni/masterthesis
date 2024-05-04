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

def get_customer_needs_approaches():
    responses = {}
    print("Please rate the following statements on a scale of 1 (strongly disagree) to 5 (strongly agree):")
    responses['Consultative Selling'] = int(input("Our target customers need a consultative approach to selling, where we would acts as a long-term ally and help them achieve their strategic goals: "))
    responses['Enterprise Selling'] = int(input("Our target customers need a cross-functional sales process, involving multiple departments from both sides (marketing, product, operations) to co-create value: "))
    responses['Challenger Selling'] = int(input("Our target customers might benefit from new insights and ways of thinking about their industry. They might therefore need to interact with salespeople who act as new knowledge sources:  "))
    responses['Social Selling'] = int(input("Our target customers are likely to enter the sales funnel without a direct interaction with sales personnel, therefore making use of the Internet and social media channels (e.g., LinkedIn) to learn more about their needs and possible solutions: "))
    responses['Need-Satisfaction Selling'] = int(input("Our target customers are often aware of the problem they face, its extent, and its implications. They seek tailored solutions for their unique needs: "))
    responses['Problem-Solving Selling'] = int(input("Our target customers are often not aware of the problem they face, its extent, and its implications.  They therefore need to be educated: "))
    responses['Value-based Selling'] = int(input("Our target customers need to see not only how the solution addresses their needs, but also how it brings value in terms of increased profits for the buying firm: "))
    
    max_score = max(responses.values())
    recommended_approaches = [approach for approach, score in responses.items() if score == max_score]
    return recommended_approaches

def get_customer_needs_channels(score1):
    responses = {}
    print("Please rate the following statements on a scale of 1 (strongly disagree) to 5 (strongly agree):")
    if score1 == 3:
        responses['Direct Sales Force'] = int(input("Our potential customers need a personal approach to selling, that is someone to talk to in person or over the phone: "))
    responses['Telemarketing'] = int(input("Our potential customers need a personal approach to selling, that is someone to talk to in person or over the phone: ")) if score1 < 3 else responses['Direct Sales Force']
    responses['Distributors'] = int(input("Our target market would be more effectively reached through partners who distribute our cloud service: "))
    responses['Value-added intermediaries'] = int(input("For our target customer to purchase our product, it has to be commercialised through partners that enhance its value by adding  features or service: "))
    responses['Internet'] = int(input("Our potential customers prefer the convenience and flexibility of easy online transactions: "))
    responses['Trade Shows'] = int(input("Our target market frequently attends industry events, conferences, and trade shows: "))
    
    max_score = max(responses.values())
    recommended_channels = [channel for channel, score in responses.items() if score == max_score]
    return recommended_channels

def generate_final_recommendation(init_approaches, init_channels, customer_approaches, customer_channels, score1, score2):
    common_approaches = set(init_approaches).intersection(set(customer_approaches))
    common_channels = set(init_channels).intersection(set(customer_channels))
    
    # Initialize a note for intensive resource approaches, if applicable
    asterisk_note = ""
    if score1 == 2 and score2 == 3 and ('Consultative Selling' in common_approaches or init_approaches or 'Enterprise Selling' in common_approaches or init_approaches or 'Value-based Selling' in common_approaches or init_approaches):
        asterisk_note = "*Please note that while Enterprise Selling or Consultative Selling and Value-based Selling are resource intensive approaches, they can be implemented with medium level of resources, provided that the startup focuses on a smaller customer base or fewer clients contemporarily."

    resource_intensive_note = "*Please note that although we recommend you implement this channel(s), this suggestion prioritises your customers' needs, but might be too resource intensive."
    unmet_customer_needs_note = "*Please note that the recommended approaches might not entirely meet customer needs."
    
    # Construct the final message based on the inputs and analyses
    if not common_approaches and not common_channels:
        message = f"Based on your resource availability and your product/service's level of innovativeness, the most suitable approaches and channels are: {init_approaches} and {init_channels}.\n"
        message += f"Based on the customer needs of your target segment, the most suitable approaches and channels are: {customer_approaches} and {customer_channels}.\n"
        message += "Unfortunately, we cannot recommend a fully aligned sales approach and sales channel as your startup resources availability, product innovativeness and customer needs are not aligned. We highly recommend you to revise your current situation and reflect on your availability of resources, product/service and target segment."
    else:
        message = f"Based on your resource availability and your product/service's level of innovativeness, the most suitable approaches and channels are: {init_approaches} and {init_channels}.\n"
        message += f"Based on the customer needs of your target segment, the most suitable approaches and channels are: {customer_approaches} and {customer_channels}.\n"
        message += f"Therefore, we recommend focusing on the implementation of: {list(common_approaches) if common_approaches else init_approaches} and {list(common_channels) if common_channels else customer_channels}."

        if not common_channels:
            message += "\n" + resource_intensive_note
        if not common_approaches:
            message += "\n" + unmet_customer_needs_note
        if asterisk_note:
            message += "\n" + asterisk_note
    
    message += "\n\nWhy did you get these results and what do they mean?:\n"
    
    explanations = {
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

    # Print the explanations for each recommended approach and channel
    for approach in common_approaches:
        message += f"\n{explanations[approach]}\n"
    for channel in common_channels:
        message += f"\n{explanations[channel]}\n"
        
    return message
    
def interactive_survey_final():
    print("Welcome to the Sales DSS for Cloud Computing Startups !\n")
    print("This DSS was developed with to offer guidance to startups operating in the Cloud Computing sector and facing the so-called “Pioneer Problem”. This term describes the difficulties that innovative start-ups encounter in defining effective sales strategies in markets that are often new or little explored, where traditional paths may not be sufficient or adequate.")
    print("Our DSS seeks to mitigate this problem by providing a structured framework for strategic orientation, helping startups identify the most promising sales approaches and channels based on their specific resources, product/service innovativeness level and customer needs. ")
    print("The code is the result of in-depth qualitative research carried out by interviewing sales experts and startup founders in the Cloud Computing sector. These conversations provided valuable insights that helped shape the decision tree at the heart of our tool. The tool framework has been further enriched and validated through a careful analysis of existing academic literature, thus ensuring that it is anchored in established practices as well as fundamental sales theories. ")
    print("One of the salient aspects that emerged during the validation phase of the tool concerns the importance of using this tool in a group context. It is strongly recommended that you complete the questionnaire as a team as this stimulates dialogue and collective reflection.") 
    print("In summary, the Sales DSS for Cloud Computing Startups does not aim to provide definitive answers but rather to guide startups through a process of self-reflection and strategic planning. It is a flexible tool, designed to adapt to the dynamic realities of Cloud Computing, offering startups a compass to more confidently navigate a complex and ever-changing market.")
    
    print("Rate your availability of both financial and human resources (especially in your commercial team):")
    print("1: Low, 2: Medium, 3: High")
    score1 = int(input("Your rating (1-3): "))
    approaches1 = get_sales_approaches_resources(score1)
    channels1 = get_sales_channels_resources(score1)
    
    print("Rate the innovativeness and complexity of your product:")
    print("1: Low, 2: Medium, 3: High")
    score2 = int(input("Your rating (1-3): "))
    approaches_final = get_sales_approaches_innovation(score1, score2, approaches1)
    channels_final = get_sales_channels_innovation(score1, score2, channels1)
    
    customer_approaches = get_customer_needs_approaches()
    customer_channels = get_customer_needs_channels(score1)
    
    final_recommendation= generate_final_recommendation(approaches_final, channels_final, customer_approaches, customer_channels, score1, score2)
    print(final_recommendation)
    

interactive_survey_final()
