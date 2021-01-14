import requests
from requests import Response
from playsound import playsound
from art import text2art

def status(r) -> None:
	with open("lj.txt","r",encoding="utf-8") as f:
			print("".join(f.readlines()))
	if r == 200:
		playsound('ok.mp3',block=False)
	elif r >= 200 and r < 300:
		playsound('yeah.mp3',block=False)
	elif r >= 400 and r < 500:
		playsound('what.mp3',block=False)
	elif r >= 500:
		playsound('what2.mp3',block=False)
	print(text2art(str(r),font='bolger',chr_ignore=True))


def get(url, params=None, **kwargs) -> Response:
	r = requests.request('get', url, params=params, **kwargs)
	status(r.status_code)
	return r

def post(url, data=None, json=None, **kwargs) -> Response:
	r = requests.request('post', url, data=data, json=json, **kwargs)
	status(r.status_code)
	return r

def options(url, **kwargs) -> Response:
	r = requests.request('options', url, **kwargs)
	status(r.status_code)
	return r

def head(url, **kwargs):
	r = requests.request('head', url, **kwargs)
	status(r.status_code)
	return r 

def put(url, data=None, **kwargs):
	r = requests.request('put', url, data=data, **kwargs)
	status(r.status_code)
	return r

def delete(url, **kwargs) -> Response: 
	r = requests.request('delete', url, **kwargs)
	status(r.status_code)
	return r

def patch(url, data=None, **kwargs) -> Response:
	r = requests.request('patch', url, data=data, **kwargs)
	status(r.status_code)
	return r