import os
import time

source = ['/Users/deebeat/Desktop/source/']
target_dir = '/Users/deebeat/Desktop/backup/'

target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'
today = target_dir + time.strftime('%Y-%m-%d')

now = time.strftime('%H%M%S')

comment = raw_input('Enter a comment: ')
if len(comment) == 0: # check if a comment was entered
	target = today + os.sep + now + '.zip'
else:
	target = today + os.sep + now + '_' + \
        comment.replace(' ', '_') + '.zip'

if not os.path.exists(today):
	os.mkdir(today)

target = today + os.sep + now + '.zip'

zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))

if os.system(zip_command) == 0:
	print"Back up to has been completed :):  Location: ", target
else:
	print"Backup FAILED"