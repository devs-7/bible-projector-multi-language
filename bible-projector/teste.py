import base64

q = 'No princípio'
q = base64.encodestring(q.encode())
# q = q[2:-1]
print(q.decode())
