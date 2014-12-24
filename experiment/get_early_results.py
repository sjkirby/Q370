from boto.mturk.connection import MTurkConnection
from hit_definitions import *

ACCESS_ID ='AKIAIP2Z2A5O4LOSZ72Q'
SECRET_KEY = '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'
HOST = 'mechanicalturk.amazonaws.com'
 
# mtc = MTurkConnection(aws_access_key_id=ACCESS_ID,
#                       aws_secret_access_key=SECRET_KEY,
#                       host=HOST)
 
# print mtc.get_account_balance()
 
from boto.mturk.question import *

mtc = MTurkConnection(aws_access_key_id=ACCESS_ID,
                      aws_secret_access_key=SECRET_KEY,
                      host=HOST)

def get_all_reviewable_hits(mtc):
    page_size = 100
    hits = mtc.get_reviewable_hits(page_size=page_size)
    print "Total results to fetch %s " % hits.TotalNumResults
    print "Request hits page %i" % 1
    total_pages = float(hits.TotalNumResults)/float(page_size)
    int_total= int(total_pages)
    if(total_pages-int_total>0):
        total_pages = int_total+1
    else:
        total_pages = int_total
    pn = 1
    total_pages = 25
    while pn < total_pages:
        print "Request hits page %i" % pn
        temp_hits = mtc.get_reviewable_hits(page_size=page_size,page_number=pn)
        hits.extend(temp_hits)
        pn = pn + 1
    return hits

def get_all(mtc):
    page_size = 50
    hits = mtc.search_hits(page_size=page_size)
    print "Total results to fetch %s " % hits.TotalNumResults
    print "Request hits page %i" % 1
    total_pages = float(hits.TotalNumResults)/float(page_size)
    int_total= int(total_pages)
    if(total_pages-int_total>0):
        total_pages = int_total+1
    else:
        total_pages = int_total
    pn = 1
    total_pages = 15
    while pn < total_pages:
        print "Request hits page %i" % pn
        temp_hits = mtc.search_hits(page_size=page_size,page_number=pn)
        hits.extend(temp_hits)
        pn = pn + 1
    return hits



hits = get_all(mtc)

vis = set()

resps = {}

dups = []
thit = None

lookingfor = set(finalround)

for hit in hits:
    thit = mtc.get_hit(hit.HITId)
    if hit.HITId not in lookingfor:
        assignments = mtc.get_assignments(hit.HITId)
        for assignment in assignments:
            vis.add(assignment.WorkerId)
        # mtc.set_reviewing(hit.HITId)
        continue
    assignments = mtc.get_assignments(hit.HITId)
    for assignment in assignments:
        ans = {}
        if assignment.WorkerId in vis:
            print 'duplicate',assignment.WorkerId
            dups.append(assignment.WorkerId)
        else:
            vis.add(assignment.WorkerId)
            ans['hit'] = hit.HITId
            for answer in assignment.answers[0]:
                ans[answer.qid] = answer.fields
            resps[assignment.WorkerId] = ans

# questions = {}

# for hit in hits:
#     thit = mtc.get_hit(hit.HITId)
#     if hit.HITId in questions:
#         if thit[0].Question != questions[hit.HITId]:
#             print hit.HITId


    # if(thit[0].Title not in 'Vocabulary Matching Survey Experiment - FIXED, working, and shorter!'):
    #     assignments = mtc.get_assignments(hit.HITId)
    #     for assignment in assignments:
    #         vis.add(assignment.WorkerId)
    #     # mtc.set_reviewing(hit.HITId)
    #     print thit[0].Title
    #     continue
    # else:
    #     print thit[0].Title
    # assignments = mtc.get_assignments(hit.HITId)
    # questions[hit.HITId]= thit[0].Question
    # for assignment in assignments:
    #     ans = {}
    #     if assignment.WorkerId in vis:
    #         print 'duplicate',assignment.WorkerId
    #         dups.append(assignment.WorkerId)
    #     else:
    #         vis.add(assignment.WorkerId)
    #         for answer in assignment.answers[0]:
    #             ans[answer.qid] = answer.fields
    #         resps[assignment.WorkerId] = ans


# print questions
print 'last_resps = ',resps



# for x in resps:
# 	print 'worker'
# 	for y in x:
# 		print y,x[y]