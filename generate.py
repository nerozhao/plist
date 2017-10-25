# -*- coding: utf-8 -*-
for i in range(2,51):
	filename = 'com.nerozhao.wchook%02d.plist' % i
	ipaname = 'com.nerozhao.wchook%02d.ipa' % i
	content = open('com.nerozhao.wchook01.plist', 'r').read().replace("com.nerozhao.wchook01.ipa", ipaname)
	open(filename, 'w').write(content)