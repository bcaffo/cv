#!/bin/bash
git pull
pdflatex cv.tex
bibtex cv1
bibtex cv2
bibtex cv3
bibtex cv4
bibtex cv5
pdflatex cv.tex
pdflatex cv.tex
#git commit -a -m "auto build pdf"
#git push origin master
