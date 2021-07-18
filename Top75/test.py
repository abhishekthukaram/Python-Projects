import requests

def check_session():
    request_url = "https://app-uswest4.central.arubanetworks.com/users/settings"
    #session = requests.Session()
    header = {'cookie':'acp_cluster_id=uswest4; session=ecb9754f92cd2d42_60ec8b53.EZhJnGAlc7WcpLp_6fSIjfhpWZs; csrftoken=##6ed5baca8eefcd1182e1fc260bbf060f8004529e'}
    session_response = requests.get(request_url, headers=header)
    print(session_response.content)
    if session_response.status_code == 200:
        print("Sucess Login")

check_session()

users = {
0: { "user": ['f1', 'l1'], "phone": '5109991220', "email": 'u1@company.com'},
1: { "user": ['f2', 'l2'], "phone": '5109991221', "email": 'u2@company.com'},
2: { "user": ['f3', 'l3'], "phone": '5109991223', "email": 'u3@company.com' },
3: { "user": ['f4', 'l4'], "phone": '', "email": 'u4@company.com' },
4: { "user": ['f5', 'l5'], "phone": '', "email": 'u6@company.com' }
}

phones = [
{'f4': '9258542323',
'f5': '8258542324',
'f3': '7258542325'
}
]

#users[0]['phone']

def check_users(users, phones):
    new_users = {}
    for index in users.keys():
        if users[index]["phone"] == "":
            update = users[index]
            print(update['user'])
            if update['user'][0] in phones[0].keys():
                print("NUMBER", phones[0][update['user'][0]])
                update['phone'] = phones[0][update['user'][0]]
                new_users[index] = users[index]
                print("UPDATED")
        else:
            new_users[index] = users[index]
    return new_users

print (check_users(users, phones))