#!/usr/bin/env python

import time

def remove_tags(instr):
        res = []
        cur =  0

	i = 0        
	#print '## len = ', len(instr)        
        while cur < len(instr):
		i+= 1
		if i > 100:
			print 'fails instr', instr
			return
                start =  end =  0
                start = instr.find("<", cur)

                #print 'a_start=',start, 'cur=', cur, 'res=', res
  
		# no tags              
                #if start == -1 and len(res) == 0:
                if start == -1:
                        return res + instr[cur:].strip().split(' ')

		
		#print 'cur=', cur, 'start=', start, 'instr[cur] =>', instr[cur]
                if cur < start or start == -1:
                        if instr[cur] in '<>\n\r ':
				#print 'advance cur'
                                cur += 1
                        if cur < start:
                                tstr = instr[cur:start]
                                tstrs = tstr.strip().split(' ')
                                #print 'tstrs = ' , tstrs
                                for s in tstrs:
                                        s = s.replace("\n", "")
                                        if len(s) > 0:
                                                res.append(s)
                end = instr.find(">", start)
		if end > 0:
                	cur = end + 1
                	#print 'cur_1=', cur, 'endch = ', instr[end]
		#time.sleep(1)
        return res

if False:
	print remove_tags('''<h1>Title</h1><p>This is a
			    <a href="http://www.udacity.com">link</a>.<p>''')
	#>>> ['Title','This','is','a','link','.']

	print remove_tags('''<table cellpadding='3'>
			     <tr><td>Hello</td><td>World!</td></tr>
			     </table>''')
	#>>> ['Hello','World!']

	print remove_tags("<hello><goodbye>")
	#>>> []

	print remove_tags('This sentence has no tags.')
	print remove_tags('<br />This line starts with a tag')
	print remove_tags('This <i>line</i> has <em>lots</em> of <b>tags</b>.')

print remove_tags("A <img src='here.img' alt='nothing'>picture,</a> a cat and a mouse! ")

