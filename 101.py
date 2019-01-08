import json

class Foo:
	def __init__(self):
		self.name = 'ricky'
		self.age = 21

chenruiqi = Foo()
res1 = chenruiqi.__dict__
res2 = json.dumps(chenruiqi.__dict__)

print(type(res1))
print(type(res2))

print(type(json.loads(res2)))