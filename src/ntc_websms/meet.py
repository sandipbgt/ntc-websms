"""Commandline tool to send free SMS via http://www.meet.net.np"""

import sys
import os

import requests
from lxml import html
import argparse

class Session:

    def __init__(self):
        self.session = requests.sessions.Session()

    def get(self, url):
        return self.session.get(url)

    def post(self, url, data):
        return self.session.post(url, data)

class Meet:

    def __init__(self):
        self.login_url = 'http://www.meet.net.np/meet/action/login'
        self.send_sms_url = 'http://www.meet.net.np/meet//mod/sms/actions/send.php'
        self.session = Session()

    def login(self, username, password):
        if not username:
            print('Username is required')
            sys.exit(1)
        elif not password:
            print(' Password is required')
            sys.exit(1)

        payload = {
            'username': username,
            'password': password,
            'loginPage': 'true'
        }

        print("Logging in...")
        response = self.session.post(self.login_url, payload)
        f = open('f.html', 'w')
        f.write(response.text)
        tree = html.fromstring(response.content)
        try:
            message = tree.xpath('//li[@class="elgg-message elgg-state-error"]/text()')[0]
            print(message.strip())
            return False
        except IndexError:
            try:
                message = tree.xpath('//li[@class="elgg-message elgg-state-success"]/text()')[0]
                print(message.strip())
                return True
            except:
                pass

    def send_sms(self, phone_number, message):
        if not phone_number:
            print("Phone number is required.")
            sys.exit(1)
        elif not message:
            print("Message text is required.")
            sys.exit(1)

        payload = {
            'SmsLanguage': 'English',
            'recipient': phone_number,
            'message': message,
            'sendbutton': 'Send Now'
        }

        print("Sending SMS.")
        response = self.session.post(self.send_sms_url, payload)
        tree = html.fromstring(response.content)
        try:
            message = tree.xpath('//li[@class="elgg-message elgg-state-error"]/text()')[0]
            print(message.strip())
        except IndexError:
            try:
                message = tree.xpath('//li[@class="elgg-message elgg-state-success"]/text()')[0]
                print(message.strip())
            except:
                pass

def main():
    parser = argparse.ArgumentParser(description="Commandline tool to send free SMS via http://www.meet.net.np")

    parser.add_argument('-p', '--phone-number', help="Reciever's phone number.", action='store', required=True)
    parser.add_argument('-m', '--message', help="Message body.", action='store', required=True)

    args = parser.parse_args()

    meet = Meet()
    username = os.environ.get("MEET_USERNAME")
    password = os.environ.get("MEET_PASSWORD")

    if not username:
        print("Please set MEET_USERNAME environment variable first.")
        sys.exit(1)
    
    if not password:
        print("Please set MEET_PASSWORD environment variable first.")
        sys.exit(1)

    if meet.login(username, password):
        meet.send_sms(args.phone_number, args.message)

if __name__ == '__main__':
    main()