APP = app.pyz
FILES = *.py **/*.py *.txt *.yml

.PHONY: all

all: $(APP)

$(APP): $(FILES)
	python -m compileall .
	zip -r $(@) *.pyc **/*.pyc
	zip -u $(@) *.txt
	zip -u $(@) *.yml

clean:
	$(RM) *.pyc **/*.pyc

distclean: clean
	$(RM) $(APP)

