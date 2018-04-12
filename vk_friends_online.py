import vk
import getpass
from constants import APP_ID, API_VERSION


def get_user_login():
    return input('Enter your VK login: ')


def get_user_password():
    return getpass.getpass(prompt='Enter VK password: ')


def get_online_friends(app_id, login, password, api_version='3.0'):
    session = vk.AuthSession(
        app_id=app_id,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session, version=api_version)
    ids_of_online_friends = api.friends.getOnline()
    online_friends = api.users.get(user_ids=ids_of_online_friends)
    return online_friends


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
    if not login:
        exit('Login could not be empty. Leaving...')

    password = get_user_password()
    if not password:
        exit('Password could not be empty. Leaving...')

    friends_online = get_online_friends(
        APP_ID,
        login,
        password,
        api_version=API_VERSION
    )
    output_friends_to_console(friends_online)
