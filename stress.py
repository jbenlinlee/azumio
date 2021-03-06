from datetime import datetime
from pytz import timezone

basetz=timezone('UTC')
currtz=timezone('US/Eastern')

def intoint(a):
	return int(a)

daydict=dict()

with open('stress.csv','r') as f:
	f.readline()
	for inl in f:
		dat = inl[:-1].split(',')
		stress = int(dat[4])
		evtdate = map(intoint, dat[1].split('-'))
		evttime = map(intoint, dat[2].split(':'))
		evtdt = datetime(evtdate[0], evtdate[1], evtdate[2], evttime[0], evttime[1], evttime[2], 0, basetz)
		evtdttz = evtdt.astimezone(currtz)
		
		dtstr = evtdttz.strftime("%Y-%m-%d")
		if (dtstr in daydict.keys()):
			tdict = daydict[dtstr]
		else:
			tdict = dict()
			tdict['morning'] = -1
			tdict['evening'] = -1
			daydict[dtstr] = tdict

		if (evtdttz.time().hour < 12):
			# print evtdttz.isoformat() + ' ---> morning : ' + stress
			tdict['morning'] = stress
		else:
			# print evtdttz.isoformat() + ' ---> evening : ' + stress
			tdict['evening'] = stress

increasing = []
decreasing = []
maintaining = []
		
for d in daydict.keys():
	entry = daydict[d]

	if entry['morning'] == -1:
		entry['morning'] = entry['evening']

	if entry['evening'] == -1:
		entry['evening'] = entry['morning']

	ydelta = entry['evening'] - entry['morning']
	outstr = ",".join([d, str(entry['morning']), "0", str(ydelta)])

	if (ydelta == 0):
		# print str(ydelta) + " -> maintaining"
		maintaining.append(outstr)
	elif (ydelta > 0):
		# print str(ydelta) + " -> increasing"
		increasing.append(outstr)
	else:
		# print str(ydelta) + " -> decreasing"
		decreasing.append(outstr)

for p in increasing:
	print p

print
print

for p in decreasing:
	print p

print
print

for p in maintaining:
	print p