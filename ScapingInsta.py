import requests
import datetime

def login(username, password):
    """Login to Instagram"""

    time = str(int(datetime.datetime.now().timestamp()))
    enc_password = f"#PWD_INSTAGRAM_BROWSER:0:{time}:{password}"

    session = requests.Session()
    # set a cookie that signals Instagram the "Accept cookie" banner was closed
    session.cookies.set("ig_cb", "2")
    session.headers.update({'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'})
    session.headers.update({'Referer': 'https://www.instagram.com'})
    res = session.get('https://www.instagram.com')

    csrftoken = None

    for key in res.cookies.keys():
        if key == 'csrftoken':
            csrftoken = session.cookies['csrftoken']

    session.headers.update({'X-CSRFToken': csrftoken})
    login_data = {'username': username, 'enc_password': enc_password}

    login = session.post('https://www.instagram.com/accounts/login/ajax/', data=login_data, allow_redirects=True)
    session.headers.update({'X-CSRFToken': login.cookies['csrftoken']})

    cookies = login.cookies
    print(login.text)

    session.close()


login('ziad_ouchary01', '18072001Ouchary.01')