import time,datetime,os,string,random


def fake_token():
    first = ('').join(random.choices(string.ascii_letters + string.digits, k=24))
    second = ('').join(random.choices(string.ascii_letters + string.digits + "-" + "_", k=6))
    end = ('').join(random.choices(string.ascii_letters + string.digits + "-" + "_", k=25))
    token = f"OT{first}.{second}.{end}"
    return token

def fake_id():
    result = ""
    for i in range(18):
        result += random.choice(string.digits)
    return result

def fake_username():
    with open('names.txt', 'r') as f:
        names = f.readlines()
    name= random.choice(names).strip()
    return name
    
def fake_discrimination():
    result = ""
    for i in range(4):
        result += random.choice(string.digits)
    return result

def fake_user():
    username=fake_username()
    dis=fake_discrimination()
    result=f'{username}#{dis}'
    return result

def fake_emailname():
    result=""
    for i in range(random.randint(5,10)):
        result+=random.choice(string.ascii_letters)
    for i in range(random.randint(3,5)):
        result+=random.choice(string.digits)
    return result

def fake_email():
    domain=['gmail.com','yahoo.com','hotmail.com','outlook.com']
    email_name=fake_emailname()
    email=f'{email_name}@{random.choice(domain)}'
    return email

def fake_email_password():
    result=""
    for i in range(random.randint(8,12)):
        result+=random.choice(string.ascii_letters+string.digits)
    return result

os.system('cls')
os.system(f'title wasreal token generator')
while True:
    os.system(f'color {random.randint(1,9)}')
    delay = random.randint(1, 5)
    verify_time=random.random()*3
    cap_time=random.random()*3
    name_info=fake_username()
    dis_info=fake_discrimination()
    full_info=f'{name_info}#{dis_info}'
    email=fake_email()
    password=fake_email_password()

    print(f'{datetime.datetime.now()}ㅣ[wasreal token gen start]')
    time.sleep(random.randint(3,4))
    print(f'{datetime.datetime.now()}ㅣ[wasreal token gen] name: {name_info}')
    time.sleep(random.randint(3,4))
    print(f'{datetime.datetime.now()}ㅣ[wasreal token gen] captcha solving...')
    time.sleep(cap_time)
    print(f'{datetime.datetime.now()}ㅣ[wasreal token gen] captcha solved!({cap_time} s)')
    print(f'{datetime.datetime.now()}ㅣ[wasreal token gen] email: {email}')
    print(f'{datetime.datetime.now()}ㅣ[wasreal token gen] email password: {password}')
    print(f'{datetime.datetime.now()}ㅣ[wasreal token gen] email_info: {email} l {password}')
    print(f'{datetime.datetime.now()}ㅣ[wasreal token gen] email verifying...')
    
    time.sleep(verify_time)
    print(f'{datetime.datetime.now()}ㅣ[wasreal token gen] email verified!({verify_time} s)')
    time.sleep(random.randint(3,4))
    print(f'{datetime.datetime.now()}ㅣ[wasreal token gen] info: {full_info}')
    time.sleep(random.randint(3,4))
    print(f'{datetime.datetime.now()}ㅣ[wasreal token gen] token: {fake_token()}')
    time.sleep(random.randint(1,2))
    print(f'{datetime.datetime.now()}ㅣ[wasreal token gen] account: {email} l {password} l {fake_token()}')
    time.sleep(random.randint(3,4))
    print(f'{datetime.datetime.now()}ㅣ[wasreal token gen] save in tokens.txt !')
    with open('tokens.txt', 'a') as f:
        f.write(f'{email}:{password}:{fake_token()}\n')
    print(f'{datetime.datetime.now()}ㅣ[wasreal token gen] done!')
    print('='*15)
    time.sleep(delay)



