from webob.multidict import MultiDict
# 可以存储多个相同的key
md = MultiDict()
md.add(1, 'magedu')
md.add(1, '.com')
md.add('a', 1)
md.add('a', 2)
md.add('b', '3')
md['b'] = '4'
md['d'] = 111
for pair in md.items():
    print(pair)

print('-'*10)
for pair in md['b']:
    print(pair)
print('-'*10)

print(md.getall('a'))
print(md.getone('d'))  # 只能有一个值,否则出错
print(md.get('b'))  # 返回一个值 print(md.get('c')) # 不会抛异常KeyError，返回None
