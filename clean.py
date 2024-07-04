#!/usr/bin/env python3
import os,sys,time  , subprocess

if __name__ == '__main__' :
	images = [a for a in os.listdir('.') if a.endswith('.png')]
	for img in images :
		fn, ext = img .split('.')
		cmd = 'identify %s' % img 
		
		r = subprocess.run(  ['identify' , img ]  , stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
		content = r.stdout.strip()
		if '600x600' not in content :
			print ('hey! %s '% img )