SPHINXOPTS ?=
SPHINXBUILD ?= uv run sphinx-build
SOURCEDIR = .
BUILDDIR = _build

.PHONY: html clean

html:
	$(SPHINXBUILD) -b html $(SOURCEDIR) $(BUILDDIR)/html $(SPHINXOPTS)

clean:
	rm -rf $(BUILDDIR)
