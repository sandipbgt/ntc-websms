ntc-websms
==========

Commandline tool to send free SMS via http://www.meet.net.np

Installation
------------

- `ntc-websms` can be installed using pip
- You will need `python3` and `pip3`.

::

    $ sudo apt-get install python3-lxml
    $ sudo pip3 install ntc-websms

- Once installed, `ntc-websms` can be accessed using `meet` command from terminal.

Configuration
-------------

- Add `MEET_USERNAME="YOUR_MEET_USERNAME" and `MEET_PASSWORD="YOUR_MEET_PASSWORD"` environment variables to your bash profile.

Usage
-----

- To send sms
::

	$ meet --phone-number 98423XXXXX --message "Hi!. I am sending this sms using ntc-websms tool developed by Sandip Bhagat."

or 

::

  $ meet -p 98423XXXXX -m "Hi!. I am sending this sms using ntc-websms tool developed by Sandip Bhagat."

Advanced Usage
--------------

usage: meet [-h] -p PHONE_NUMBER -m MESSAGE

Commandline tool to send free SMS via http://www.meet.net.np

optional arguments:
  -h, --help            show this help message and exit
  -p PHONE_NUMBER, --phone-number PHONE_NUMBER
                        Reciever's phone number.
  -m MESSAGE, --message MESSAGE
                        Message body.

Contribution
------------

Feel free to create a Github issue. Also, you are more than welcome to submit
a pull request for a bug fix or additional feature.