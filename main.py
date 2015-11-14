# -*- coding: UTF-8 -*-
#动态打印

from bottle import route, run

data=""

@route('/hello')
def hello(data):
    return data

def main():
    while True:
	    line2 = raw_input("continue print Y, quit print N ")
	    if line2=="Y":
	        data=raw_input("-->")
		    run(host='localhost', port=8080,debug=True)
	    elif line2=="N":
		    break

if __name__ == "__main__":
	main（）
