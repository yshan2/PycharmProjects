def upup(name, parents, attr):
	newattr = {}
	for name ,value in attr.items():
		if not name.startswith("__"):
			newattr[name.upper()] = value

	return type(name, parents, newattr)


class Foo(object, metaclass=upup):
	bar = "bip"


print(hasattr(Foo, "bar"))
print(hasattr(Foo, "BAR"))

f = Foo()
print(f.BAR)
