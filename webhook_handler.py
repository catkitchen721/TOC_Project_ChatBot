import json
import sys
#sys.path.append('home/TOC-Project-2019/demo_example')
from bottle import route, run, request, static_file
from send_msg import send_text_message
from fsm import TocMachine


machine = TocMachine(
    states=[
        'user',
        'astroState',
        'ariesState',
        'taurusState',
        'geminiState',
        'cancerState',
        'leoState',
        'virgoState',
        'libraState',
        'scorpioState',
        'sagittariusState',
        'capricornState',
        'aquariusState',
        'piscesState',
        'backState',
        'subUser',
        'beautyState'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': ['user', 'subUser'],
            'dest': 'astroState',
            'conditions': 'is_going_to_astroState'
        },
        {
            'trigger': 'advance',
            'source': ['user', 'subUser'],
            'dest': 'beautyState',
            'conditions': 'is_going_to_beautyState'
        },
        {
            'trigger': 'advance',
            'source': ['astroState', 'backState'],
            'dest': 'ariesState',
            'conditions': 'is_going_to_ariesState'
        },
        {
            'trigger': 'advance',
            'source': ['astroState', 'backState'],
            'dest': 'taurusState',
            'conditions': 'is_going_to_taurusState'
        },
        {
            'trigger': 'advance',
            'source': ['astroState', 'backState'],
            'dest': 'geminiState',
            'conditions': 'is_going_to_geminiState'
        },
        {
            'trigger': 'advance',
            'source': ['astroState', 'backState'],
            'dest': 'cancerState',
            'conditions': 'is_going_to_cancerState'
        },
        {
            'trigger': 'advance',
            'source': ['astroState', 'backState'],
            'dest': 'leoState',
            'conditions': 'is_going_to_leoState'
        },
        {
            'trigger': 'advance',
            'source': ['astroState', 'backState'],
            'dest': 'virgoState',
            'conditions': 'is_going_to_virgoState'
        },
        {
            'trigger': 'advance',
            'source': ['astroState', 'backState'],
            'dest': 'libraState',
            'conditions': 'is_going_to_libraState'
        },
        {
            'trigger': 'advance',
            'source': ['astroState', 'backState'],
            'dest': 'scorpioState',
            'conditions': 'is_going_to_scorpioState'
        },
        {
            'trigger': 'advance',
            'source': ['astroState', 'backState'],
            'dest': 'sagittariusState',
            'conditions': 'is_going_to_sagittariusState'
        },
        {
            'trigger': 'advance',
            'source': ['astroState', 'backState'],
            'dest': 'capricornState',
            'conditions': 'is_going_to_capricornState'
        },
        {
            'trigger': 'advance',
            'source': ['astroState', 'backState'],
            'dest': 'aquariusState',
            'conditions': 'is_going_to_aquariusState'
        },
        {
            'trigger': 'advance',
            'source': ['astroState', 'backState'],
            'dest': 'piscesState',
            'conditions': 'is_going_to_piscesState'
        },
        {
            'trigger': 'go_back',
            'source': [
                'ariesState',
                'taurusState',
                'geminiState',
                'cancerState',
                'leoState',
                'virgoState',
                'libraState',
                'scorpioState',
                'sagittariusState',
                'capricornState',
                'aquariusState',
                'piscesState'
            ],
            'dest': 'backState'
        },
        {
            'trigger': 'go_subUser',
            'source': [
                'backState'
            ],
            'dest': 'subUser',
            'conditions': 'is_going_to_subUser'
        },
        {
            'trigger': 'go_back',
            'source': [
                'beautyState',
            ],
            'dest': 'subUser'
        },
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)

@route("/webhook", method="POST")
def webhook_handler():
    body = request.json
    print('REQUEST BODY: ')
    print(json.dumps(body, indent=2))
    send_back_id = body.get('entry')[0].get('messaging')[0].get('sender').get('id')
    get_text = body.get('entry')[0].get('messaging')[0].get('message').get('text')

    if body['object'] == "page":
        event = body['entry'][0]['messaging'][0]
        print('主要區')
        print(machine.state)
        if machine.state == 'backState':
            machine.go_subUser(event)
            machine.advance(event)
        else:
            machine.advance(event)
        return 'OK'

@route('/show-fsm', methods=['GET'])
def show_fsm():
    machine.get_graph().draw('fsm.png', prog='dot', format='png')
    return static_file('fsm.png', root='./', mimetype='image/png')

run(host="localhost", port=5000, debug=True)
