# program used to check if password is present in pwned database
#used pwned api

import hashlib
import requests



"""Returns number of times password was seen in pwned database.
    Args:
        password: password to check
    Returns:
        count: number of times the password was seen in the pwned database.
        count equal zero indicates that password has not been found.
    Raises:
        RuntimeError: if there was an error trying to fetch data from pwneddatabase.
"""

def password_look_up(password):
	sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
	url = 'https://api.pwnedpasswords.com/range/' + sha1_hash[:5]
	res = requests.get(url)
	if res.status_code != 200:
		raise RuntimeError('Error fetching "{}": {}'.format(url, res.status_code))

	for i in res.text.splitlines():
		a = i.split(':')
		if a[0] == sha1_hash[5:]:
			return int(a[1])

	return 0



def main():

	password = input("Enter password: ")
	count = password_look_up(password)
	if count == 0:
		print("GOOD password is not breached")
	else:
		print("BAD password is found breached" + str(count) + "times")



if __name__ == '__main__':
	main()