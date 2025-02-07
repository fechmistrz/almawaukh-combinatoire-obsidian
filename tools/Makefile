SHELL=/bin/bash

.PHONY: all clean prepare release

PDFLATEX_FLAGS = -shell-escape -halt-on-error -output-directory ../build/

define make_pdf
  export max_print_line=$$(tput cols); \
  cd src && pdflatex $(PDFLATEX_FLAGS) combinatoire.tex && cp combinatoire.bib ../build/combinatoire.bib; \
  cd ../build && bibtex combinatoire; \
  cd ../src && pdflatex $(PDFLATEX_FLAGS) combinatoire.tex && pdflatex $(PDFLATEX_FLAGS) combinatoire.tex;
endef

all: prepare chapter-all release

prepare:
	mkdir -p build

chapter-all: build/combinatoire.pdf

build/combinatoire.pdf: src/combinatoire.tex src/combinatoire.bib src/*/*.tex src/*.tex
	$(call make_pdf)

release:
	for i in build/*combinatoire.pdf; do \
		if [[ "$$i" -nt "$$(basename "$$i")" ]]; then \
			cp "$$i" .; \
		fi; \
	done

deploy: all
	pdftops combinatoire.pdf combinatoire-password.ps
	ps2pdf -sUserPassword=AnnaWitkowska -sOwnerPassword="Qz,EcT.bYn;iM193492312" combinatoire-password.ps almawaukh-combinatoire.pdf
	rsync "almawaukh-combinatoire.pdf" "merridew@s57.mydevil.net:/home/merridew/domains/merridew.usermd.net/public_html/pdf/almawaukh-combinatoire.pdf"
	rm combinatoire-password.ps almawaukh-combinatoire.pdf

clean:
	rm -rf build *.pdf
