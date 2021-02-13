# pytinpy

## Usage

```
[username@hostname]$ python
Python 2.7.14 (default, Sep 22 2017, 15:49:07) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-18)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> client = TinderClient("myauthToken")
>>> user_list = client.get_recommendations()["results"]
>>> for user in user_list:
>>>     # do whatever you want ^^
