#!/bin/bash
##this file compiles the CV for travis and pushes the results back to github
##got some of this from : https://gist.github.com/willprice/e07efd73fb7f13f917ea

## build the cv
pdflatex cv.tex
bibtex cv1
bibtex cv2
bibtex cv3
bibtex cv4
bibtex cv5
#bibtex cv6
pdflatex cv.tex
pdflatex cv.tex

##set up git
git config --global user.email "travis@travis-ci.org"
git config --global user.name "Travis CI"
git remote add origin https://${GH_TOKEN}@github.com/cv.git

##commit and push 
## have to checkout first since travis links to a specific checkout id
git checkout master
git add cv.pdf
git commit --message "Travis build: $TRAVIS_BUILD_NUMBER"
git push origin master
