#!/usr/bin/env python
# encoding: utf-8
import eyed3
import sys

audiofile = eyed3.load(sys.argv[1])

def enc(tag):
		for f in (
				'album',
				'title',
				'artist',
				):
				fld = None
				exec "fld = tag.%s" % f
				if fld:
						try:
								fld.decode('utf-8')
						except UnicodeEncodeError:
								try: 
										exec "tag.%s= unicode(fld.encode(u'iso-8859-1'), u'cp1251')" % f
								except UnicodeEncodeError: pass
		for f in tag.user_text_frames:
				tag.user_text_frames.remove(f.description)
		#print tag.description
		return tag

audiofile.tag = enc(audiofile.tag)
audiofile.tag.save(encoding='utf-8')

sys.exit(0)
