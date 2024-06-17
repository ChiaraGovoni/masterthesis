import panel as pn

from decisions_functions import get_survey_controller, Survey
pn.extension()

survey_controller = [get_survey_controller()]

button = pn.widgets.Button(name='Submit & Next', button_type='primary')

counter = [0]

bs = pn.widgets.Button.param.button_style.objects[1]
p = pn.widgets.Button.param.button_type.objects[2]

def survey_question_panel(survey: Survey) -> pn.Column:
    question_row_items = []
    for i, question in enumerate(survey.questions):
        if survey.answers[i] is None:
            question_row_items.append(
                pn.Column(pn.pane.Markdown(f'#### {question}:'), pn.widgets.RadioButtonGroup(name="Answer", button_style=bs, button_type=p, options=survey.options, value=survey.default_val), button)
            )
            break
        else:
            question_row_items.append(
                pn.Column(pn.pane.Markdown(f'#### {question}:'), pn.widgets.RadioButtonGroup(name="Answer", button_style=bs, button_type=p, options=survey.options,disabled=True, value=survey.answers[i]))
            )
            #question_row_items.append(pn.Row(pn.pane.Markdown(f'{#### question}:\n {survey.val_to_option(survey.answers[i])}')))
    return pn.Column(*question_row_items)
        


def tab_panel(survey: Survey) -> pn.Column:
    return pn.Column(
        pn.pane.Markdown(survey.introduction),
       survey_question_panel(survey)
    )

def survey_placeholder() -> pn.Column:
    return pn.Row(pn.pane.Markdown('Survey not available yet. Please complete the previous survey.'))


survey_panels = [None]

tab_title_map = {
    "SalesApporachChannels": "Part 1: Sales Apporach & Channels",
    "CustomerNeedsApproaches": "Part 2: Customer Needs & Approaches",
    "CustomerNeedsChannels": "Part 3: Customer Needs & Channels",
}

survey_tabbs = pn.Tabs(
    active=0,
    tabs_location='left',
)

introduction = """
# Welcome to the Sales DSS for Cloud Computing Startups!
This DSS was developed with to offer guidance to startups operating in the Cloud Computing sector and facing the so-called “Pioneer Problem”. This term describes the difficulties that innovative start-ups encounter in defining effective sales strategies in markets that are often new or little explored, where traditional paths may not be sufficient or adequate.
Our DSS seeks to mitigate this problem by providing a structured framework for strategic orientation, helping startups identify the most promising sales approaches and channels based on their specific resources, product/service innovativeness level and customer needs.
The code is the result of in-depth qualitative research carried out by interviewing sales experts and startup founders in the Cloud Computing sector. These conversations provided valuable insights that helped shape the decision tree at the heart of our tool. The tool framework has been further enriched and validated through a careful analysis of existing academic literature, thus ensuring that it is anchored in established practices as well as fundamental sales theories.
One of the salient aspects that emerged during the validation phase of the tool concerns the importance of using this tool in a group context. It is strongly recommended that you complete the questionnaire as a team as this stimulates dialogue and collective reflection.
In summary, the Sales DSS for Cloud Computing Startups does not aim to provide definitive answers but rather to guide startups through a process of self-reflection and strategic planning. It is a flexible tool, designed to adapt to the dynamic realities of Cloud Computing, offering startups a compass to more confidently navigate a complex and ever-changing market.
"""


start_button = pn.widgets.Button(name='Start Survey', button_type='primary')
intro_panel = pn.Column(pn.pane.Markdown(introduction), start_button)

survey_tabbs.append(("Introduction", intro_panel))
results = pn.Column(pn.pane.Markdown("When the survey is completed, the results will be displayed here."), start_button)

def start_survey(event):
    survey_controller[0] = get_survey_controller()
    survey_panels[0] =  {survey: pn.Column() for survey in survey_controller[0].surveys}
    survey_tabbs.clear()
    survey_tabbs.extend(
            [("Introduction", intro_panel)] + [(tab_title_map[key.__class__.__name__], _panel) for key, _panel in survey_panels[0].items()]
        + [("Results", results)])  
    
    survey_tabbs.active = 1
    start_button.name = "Restart Survey"
    
    survey_controller[0].advance(None)
    update_survey_panel()

start_button.on_click(start_survey)




def update_survey_panel():
    #if not survey_controller[0].completed:
    survey_tabbs.active = survey_controller[0].active_survey_ix + 1
    ix = 0
    for survey, panel in survey_panels[0].items():

        panel.clear()

        if ix > survey_controller[0].active_survey_ix:
            panel.extend([survey_placeholder()])
        else:
            panel.extend([tab_panel(survey)])
        ix += 1

def get_surver_question_answer(survey: Survey) -> int:
    
    if not survey.completed:
        return survey_panels[0][survey][0][1][survey._next_question][1].value
    return ""
    

#update_survey_panel()
# Set the active tab to the introduction tab
#survey_tabbs.active = 0

def progress_survey(event):
    if not survey_controller[0].completed:
        answer = get_surver_question_answer(survey_controller[0].active_survey)
        survey_controller[0].advance(answer)
        
        
    update_survey_panel()
    if survey_controller[0].completed:
        results.clear()
        results.append(pn.pane.Markdown(f"# Results:\n {survey_controller[0].get_outcome()}"))
        results.append(start_button)
        button.disabled = True
        # set the active tab to the results tab
        survey_tabbs.active = len(survey_controller[0].surveys) + 1

button.on_click(progress_survey)

pn.template.FastListTemplate(
    site="",
    title="Sales DSS - for Cloud Computing Startups",
    
    main=[
survey_tabbs],
).servable()