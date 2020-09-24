def getLowestCommonManager(topManager, reportOne, reportTwo):
    return getOrgInfo(topManager, reportOne, reportTwo).lowestCommonManager


def getOrgInfo(manager, reportOne, reportTwo):
	num = 0
	for directReport in manager.directReports:
		orgInfo = getOrgInfo(directReport, reportOne, reportTwo)
		if orgInfo.lowestCommonManager is not None:
			return orgInfo
		num += orgInfo.numImportantRep
	if manager == reportOne or manager == reportTwo:
		num += 1
	lowestCommonManager = manager if num == 2 else None
	return OrgInfo(lowestCommonManager, num)

class OrgInfo:
	def __init__(self, lowestCommonManager, numImportantRep):
		self.lowestCommonManager = lowestCommonManager
		self.numImportantRep = numImportantRep


# This is an input class. Do not edit.
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []
