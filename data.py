import operator, json
from bson import json_util
from operator import itemgetter
from collections import OrderedDict
from datetime import datetime

# =======================================================================
# Monkey patch ElementTree
import xml.etree.ElementTree as ET

def _serialize_xml(write, elem, encoding, qnames, namespaces):
    tag = elem.tag
    text = elem.text
    if tag is ET.Comment:
        write("<!--%s-->" % ET._encode(text, encoding))
    elif tag is ET.ProcessingInstruction:
        write("<?%s?>" % ET._encode(text, encoding))
    else:
        tag = qnames[tag]
        if tag is None:
            if text:
                write(ET._escape_cdata(text, encoding))
            for e in elem:
                _serialize_xml(write, e, encoding, qnames, None)
        else:
            write("<" + tag)
            items = elem.items()
            if items or namespaces:
                if namespaces:
                    for v, k in sorted(namespaces.items(),
                                       key=lambda x: x[1]):  # sort on prefix
                        if k:
                            k = ":" + k
                        write(" xmlns%s=\"%s\"" % (
                            k.encode(encoding),
                            ET._escape_attrib(v, encoding)
                            ))
                #for k, v in sorted(items):  # lexical order
                for k, v in items: # Monkey patch
                    if isinstance(k, ET.QName):
                        k = k.text
                    if isinstance(v, ET.QName):
                        v = qnames[v.text]
                    else:
                        v = ET._escape_attrib(v, encoding)
                    write(" %s=\"%s\"" % (qnames[k], v))
            if text or len(elem):
                write(">")
                if text:
                    write(ET._escape_cdata(text, encoding))
                for e in elem:
                    _serialize_xml(write, e, encoding, qnames, None)
                write("</" + tag + ">")
            else:
                write(" />")
    if elem.tail:
        write(ET._escape_cdata(elem.tail, encoding))

ET._serialize_xml = _serialize_xml

from collections import OrderedDict

class OrderedXMLTreeBuilder(ET.XMLTreeBuilder):
    def _start_list(self, tag, attrib_in):
        fixname = self._fixname
        tag = fixname(tag)
        attrib = OrderedDict()
        if attrib_in:
            for i in range(0, len(attrib_in), 2):
                attrib[fixname(attrib_in[i])] = self._fixtext(attrib_in[i+1])
        return self._target.start(tag, attrib)

# =======================================================================

# helpers


def getTime(s):
	return datetime.strptime(s, '%Y-%m-%dT%H:%M:%SZ')

def tryFormat(s):
		try: 
			int(s)
			return int(s)
		except ValueError:
			try:
				getTime(s)
				return str(getTime(s))
			except ValueError:
				return s



fields = {'Track ID','Year','Date Added','Play Count','Skip Count','Name','Artist','Loved','score'}

# fields = {
# 'Track ID':'integer',
# 'Year':'integer',
# 'Date Added': 'date',
# 'Play Count':'integer',
# 'Skip Count':'integer',
# 'Name':'string',
# 'Artist':'string'
# # 'Genre':['string',5]
# }


# def getScroe(song):
# 	age = (datetime.now() - song['Date Added']).total_seconds()
# 	plays = song['Play Count']
# 	skips = song['Skip Count']
# 	return (plays-skips*2)/age * 10e5

# =======================================================================

tree = ET.parse('data/iTunes Music Library.xml', OrderedXMLTreeBuilder())
# root = tree.getroot()
datas = []

flag = False
tag = ''
for songs in tree.iterfind('dict/dict/dict'):
	data = {field:-1 for field in fields}
	for song in songs:
		if song.text == 'Loved':
			data['Loved'] = True
			continue
		if song.text in fields:
			flag = True
			tag = song.text
			continue
		if flag:
			data[tag] = tryFormat(song.text)
			flag = False
	# data['score'] = getScroe(data)
	datas.append(data)

# print datas


# temp = sorted(datas, key=itemgetter('score'), reverse=True)
# for e in temp[0:10]:
# 	print e['Name'],e['score']

with open('data.json', 'w') as outfile:
	json.dump(datas, outfile)
