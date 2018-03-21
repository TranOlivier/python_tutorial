import re

#regex = r"/(\w*)/(\w*):(.*)"
#teststr = '/bin/test:lumberjack'
#match = re.match(regex, teststr)

#matches = re.finditer(regex, teststr)
#print(enumerate(matches))

#for matchnum, x in enumerate(matches):

#    print(matchnum)
#    matchnum += 1
#    print(matchnum)


regex = r"(\w*),(.*)\n?"

test_str = ("valeur, 456\nvaleur, 32\nvaleur, 5")

matches = re.finditer(regex, test_str)

for matchNum, match in enumerate(matches):
    matchNum = matchNum + 1

    #print("Match {matchNum} was found : {match}".format(matchNum=matchNum, match=match.group()))

    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1

        print("Group {groupNum} found: {group}".format(groupNum=groupNum, group=match.group(groupNum)))