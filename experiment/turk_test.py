from boto.mturk.connection import MTurkConnection

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
 
title = 'Vocabulary Matching Survey Experiment - FIXED, working, and shorter!'
description = ('Help a student with a cognitive science experiment while learning new vocabulary!')
keywords = 'survey, demographics, cognitive science, vocabulary, multiple choice'
 
for i in range(300,330):
	mtc.create_hit(question=ExternalQuestion('https://googledrive.com/host/0B8upNGuUglRbR1BhYWZqTE5vcm8/out'+str(i)+'.html',730),
               max_assignments=3,
               title=title,
               description=description,
               keywords=keywords,
               reward=0.37)