import db_helper

# TODO: add date time
logData = [
      {"id": "1", "userSessionId": "123", "req": "With 500$ which devices can i buy ?", "res": "you can buy ...."},
      {"id": "2", "userSessionId": "123", "req": "if i'm new to photography, should i pick <camera model> ?", "res": "To using this you should have some basic knowledge about photography like : ... <Lists of things to know>"},
      {"id": "3", "userSessionId": "123", "req": "what is ISO, exposure ,... <some others properties of photography>", "res": "Explaining some ideas..."},
      {"id": "4", "userSessionId": "123", "req": "I'd like to take some sceneries photos, which device should i take ?", "res": "Here are some model that suitable for request <list some devices>"},
]
templateReq = [
    {"id": '1', "req": "buy product",               "action": "ask for which product"},
    {"id": '2', "req": "check receipt",             "action": "check bill id and send to customer"},
    {"id": '3', "req": "create bill",               "action": "generate bill"},
    {"id": '4', "req": "contact human assistant",   "action": "contact store owner"},
]

if __name__ == "__main__":
    if 1:
        db_helper.dropCollection('Chatbot','log')
        db_helper.dropCollection('Chatbot','templateReq')
        
    db_helper.addData('Chatbot','log',logData)
    db_helper.addData('Chatbot','templateReq',templateReq)
