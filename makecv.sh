#!/bin/bash
pdflatex cv.tex
bibtex cv1
bibtex cv2
bibtex cv3
bibtex cv4
bibtex cv5
#bibtex cv6
pdflatex cv.tex
pdflatex cv.tex
#scp cv.pdf bcaffo@www.biostat.jhsph.edu:~bcaffo/public_html/downloads/cv.myVersion.pdf
