README.rst: README.md
	pandoc README.md -o README.rst

clean:
	rm README.rst

