import vk
import getpass
from constants import APP_ID, API_VERSION


def get_user_login():
    login = input('Enter your VK login: ')
    if not login:
        exit('Login could not be empty. Leaving...')
    return login


def get_user_password():
    password = getpass.getpass(prompt='Enter VK password: ')
    if not password:
        exit('Password could not be empty. Leaving...')
    return password


def get_online_friends(app_id, login, password, api_version='3.0'):
    session = vk.AuthSession(
        app_id=app_id,
        user_login=login,
        user_password=password,
    )
    api = vk.API(session, version=api_version)
    all_friends = api.friends.get(
        fields=['first_name', 'last_name', ' online']
    )
    return list(filter(lambda friend: friend['online'], all_friends))


def output_friends_to_console(friends_online):
    if not friends_online:
        print('There are no friends online')
        return

    print('\nYour friends online:')
    for friend in friends_online:
        print('{} {}'.format(
            friend['first_name'],
            friend['last_name'])
        )


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(
        APP_ID,
        login,
        password,
        api_version=API_VERSION
    )
    output_friends_to_console(friends_online)
