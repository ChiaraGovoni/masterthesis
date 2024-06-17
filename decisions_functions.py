from abc import ABC, abstractmethod
from dashboard import get_sales_approaches_innovation, get_sales_channels_innovation, generate_final_recommendation

class Survey(ABC):
    introduction:str = """## Please answer the following questions to help us understand your business better.
    """
    questions:list[str] = []
    answers: list[int] = []
    options: dict[str, int] = {'Low': 1, 'Medium': 2, 'High': 3}
    default_val: int = 2

    current_question: str = None

    def __init__(self) -> None:
        self._next_question = -1
        self.answers = [None] * len(self.questions)
        self.current_question = None

    def val_to_option(self, val:int) -> str:
        # Find val in self.options
        for key, value in self.options.items():
            if value == val:
                return key

    def next_question(self, answer:int|None=None) -> str:

        if self._next_question > -1:

            self.answers[self._next_question] = answer

        self._next_question += 1
        if self._next_question >= len(self.questions):
            self.current_question = None

            
        else:
            self.current_question = self.questions[self._next_question]
        return self.current_question
    
    @property
    def completed(self) -> bool:
        return not any(answer is None for answer in self.answers)
    
    @abstractmethod
    def get_outcome(self) -> dict:
        pass

    def reset(self):
        self._next_question = -1
        self.answers[:] = [None] * len(self.questions)
        self.current_question = None

class SalesApporachChannels(Survey):
    introduction="""## Please rate the following statements"""
    
    questions = [
        'Rate your availability of both financial and human resources (especially in your commercial team)',
        'Rate the innovativeness and complexity of your product'
    ]

    def get_outcome(self) -> dict:
        return {
            'Sales Approaches': get_sales_approaches_innovation(self.answers[0], self.answers[1], None), 
            'Sales Channels': get_sales_channels_innovation(self.answers[0], self.answers[1], None)
        }

class CustomerNeedsApproaches(Survey):
    
    introduction="""
    ## Please rate your agreement to the following statements:
    """
    options: dict[str, int] = {'Strongly Disagree': 1, 'Disagree': 2, 'Neutral': 3, 'Agree': 4, 'Strongly Agree': 5}
    default_val: int = 3

    questions = [
        "Our target customers need a consultative approach to selling, where we would acts as a long-term ally and help them achieve their strategic goals",
        "Our target customers need a cross-functional sales process, involving multiple departments from both sides (marketing, product, operations) to co-create value",
        "Our target customers might benefit from new insights and ways of thinking about their industry. They might therefore need to interact with salespeople who act as new knowledge sources",
        "Our target customers are likely to enter the sales funnel without a direct interaction with sales personnel, therefore making use of the Internet and social media channels (e.g., LinkedIn) to learn more about their needs and possible solutions",
        "Our target customers are often aware of the problem they face, its extent, and its implications. They seek tailored solutions for their unique needs",
        "Our target customers are often not aware of the problem they face, its extent, and its implications.  They therefore need to be educated",
        "Our target customers need to see not only how the solution addresses their needs, but also how it brings value in terms of increased profits for the buying firm"
    ]

    def get_outcome(self) -> dict:
        approaches = [
            'Consultative Selling',
            'Enterprise Selling',
            'Challenger Selling',
            'Social Selling',
            'Need-Satisfaction Selling',
            'Problem-Solving Selling',
            'Value Based Selling'
        ]
        
        max_score = max(self.answers)
        recommended_approaches = [approach for approach, score in zip(approaches, self.answers) if score == max_score]
        return recommended_approaches

class CustomerNeedsChannels(Survey):
    introduction="""
    ## Please rate you agreement to the following statements:
    """
    
    options: dict[str, int] = {'Strongly Disagree': 1, 'Disagree': 2, 'Neutral': 3, 'Agree': 4, 'Strongly Agree': 5}
    default_val: int = 3

    questions = [
            
            
            "For our target customer to purchase our product, it has to be commercialised through partners that enhance its value by adding  features or service",
            "Our potential customers prefer the convenience and flexibility of easy online transactions",
            "Our target market frequently attends industry events, conferences, and trade shows",
        ]

    def __init__(self, sales_approach_channels) -> None:
        self.score_prev = None
        self.sales_approach_channels = sales_approach_channels
        self._sales_appraoch_score_decisions_made = False
        self._next_question = -1
        self.answers = [None] * (len(self.questions) +1)
        self.current_question = None


    def next_question(self, answer: int | None = None) -> str:
        if not self._sales_appraoch_score_decisions_made:
            self._sales_appraoch_score_decisions_made = True
          
            if self.sales_approach_channels.answers[0] == 3:
                self.questions = ["Our potential customers need a personal approach to selling, that is someone to talk to in person or over the phone"] + self.questions
            else:
                self.questions = ["Our target market would be more effectively reached through partners who distribute our cloud service"] + self.questions
                
        
        return super().next_question(answer)
    
    def get_outcome(self) -> dict:
        channels = [
            'Direct Sales Force',
            'Telemarketing',
            'Distributers',
            'Value-added intermediaries',
            'Internet',
            'Trade Shows'
        ]

        max_score = max(self.answers)
        recommended_channels = [channel for channel, score in zip(channels, self.answers) if score == max_score]
        return recommended_channels
            
class SurveyController:
    def __init__(self, surveys: list[Survey]) -> None:
        self.surveys = surveys
        self.active_survey_ix = 0
        self.active_survey: Survey = surveys[self.active_survey_ix]
        
    @property
    def completed(self) -> bool:
        return all(survey.completed for survey in self.surveys)

    def advance(self, answer:int):
        #self.active_survey.answers[self.active_survey._next_question] = answer
        
        question = self.active_survey.next_question(answer)
        
        if self.completed:
            return ""
        
        if self.active_survey.completed:
            # Advance to the next survey
            self.active_survey_ix += 1
            self.active_survey = self.surveys[self.active_survey_ix]

            if self.active_survey_ix == 2:
                self.active_survey.score_prev = self.surveys[0].answers[0]

            question = self.active_survey.next_question()

        return question

    def get_outcome(self) -> str:
        init_approaches = self.surveys[0].get_outcome()['Sales Approaches']
        init_channels = self.surveys[0].get_outcome()['Sales Channels']
        customer_approaches = self.surveys[1].get_outcome()
        customer_channels = self.surveys[2].get_outcome()
        score1 = self.surveys[0].answers[0]
        score2 = self.surveys[0].answers[1]
        return generate_final_recommendation(init_approaches, init_channels, customer_approaches, customer_channels, score1, score2)
    
    def reset(self):
        self.active_survey_ix = 0
        self.active_survey = self.surveys[self.active_survey_ix]
        for survey in self.surveys:
            survey.reset()

def get_survey_controller():
    sales_approach_channels = SalesApporachChannels()
    return SurveyController([
        sales_approach_channels,
        CustomerNeedsApproaches(),
        CustomerNeedsChannels(sales_approach_channels)
    ])