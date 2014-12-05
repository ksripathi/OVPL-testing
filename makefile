DEST=build/

all:  publish

publish: init
	emacs --script elisp/publish.el

init:
	mkdir -p ${DEST}


server:
	python -m SimpleHTTPServer 6001

export:
	rsync -auvz ${DEST}presentation/* letshelp@devel.virtual-labs.ac.in:/var/www/2012-10-08-integration-sprint/

clean:
	rm -rf ${DEST}

archive:
	(cd ${DEST}; zip -r presentation.zip presentation)


