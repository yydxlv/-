# coding=utf_8
# �ڽ�����str()��repr() (representation������ʾ)�����Ų�������``�����Է�������ַ����ķ�ʽ��ȡ��������ݡ����͡���ֵ���Ե���Ϣ��
#  str()�����õ����ַ����ɶ��Ժã��ʱ�print���ã�����repr()�����õ����ַ���ͨ�������������»�øö���
# ͨ������� obj==eval(repr(obj)) �����ʽ�ǳ����ġ���������������һ��������Ϊ������������ʵ����ַ�����
__author__ = 'xilin'
# class D(object):
#     def __str__(self):
#         return "a __str__"
#
#     def __repr__(self):
#         return "a __repr__"
import html
import re
line='asdf fjdk; afed, fjek,asdf    foo'
fields=re.split(r'(;|,|\s)\s*', line)
values=fields[::2]
delimiters=fields[1::2]+['']
text="Today is 11/27/2012. PyCon starts 3/13/2013."
def make_element(name,value,**attrs):
    keyvals=['%s="%s"'% item for item in attrs.items()]
    keyval=[item for item in attrs.items()]
    print(['%s=%s'%("yyd", "xl")])
    print(keyval)
    print(keyvals)
    attr_str=''.join(keyvals)
    element='<{name}{attrs}>{value}</{name}>'.format(name=name,attrs=attr_str,value=html.escape(value))
    return element
if __name__=="__main__":
    # dr = D()
    # print(dr)
    # print("%s" % dr)
    # print("%r" % dr)

    # print(re.split(r'[;,\s]\s*', line))
    # print(fields)
    # print(values)
    # print(delimiters)
    # print(''.join(v+d for v,d in zip(values,delimiters)))   #  asdf fjdk;afed,fjek,asdf foo
    # print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))
    print(make_element('item','Albatross', size='large', quantity=6))