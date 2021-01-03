# analyze all assignment statuses
fh = open('replAssignments.txt')
assignmentCount = {'total':0, 'complete':0, 'drafts':0, 'no progress':0, 'ungraded':0}
for line in fh:
    if line.startswith('Completed'):
        assignmentCount['complete'] += 1
        assignmentCount['total'] += 1
    elif line.startswith('Draft'):
        assignmentCount['drafts'] += 1
        assignmentCount['total'] += 1
    elif line.startswith('No progress'):
        assignmentCount['no progress'] += 1
        assignmentCount['total'] += 1
    elif line.startswith('Submitted'):
        assignmentCount['ungraded'] += 1
        assignmentCount['total'] += 1

for key in assignmentCount:
        print(key + ': ' + str(assignmentCount[key]))
