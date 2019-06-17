# python version: 3.7.2
# author: bavdu
# email: bavduer@163.com
# date: 2019/06/14
# usage: closure
def logAnalysis(path):
    def accessLog(frequency):
        if type(frequency) != dict or len(frequency) != 0:
            prompt = 'Please Check variable must be list type and len equal zero.'
            return prompt
        with open(path, 'r+', encoding='utf8') as logfile:
            for line in logfile.readlines():
                if line.split()[0] not in frequency:
                    frequency[line.split()[0]] = 1
                else:
                    frequency[line.split()[0]] += 1
        return frequency
    return accessLog


log = logAnalysis('./access_log-20181111')
analysis = log({})

ipList = [element for element in analysis.items()]
for i in range(len(ipList)):
    for j in range(i, len(ipList)):
        if ipList[i][1] < ipList[j][1]:
            ipList[i], ipList[j] = ipList[j], ipList[i]
print(ipList[0:10])
