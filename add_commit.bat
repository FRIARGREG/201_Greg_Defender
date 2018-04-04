cls

REM ################################################################
REM ##                                                            ##
REM ##                           GIT                              ##
REM ##   ADD AND COMMIT ALL FILES NOT ALREADY ON THE REPOSITORY   ##
REM ##                                                            ##
REM ################################################################

git config user.name "FRIARGREG"
git config user.email "friar.gregarious@gmail.com"
git config color.ui true
git config format.pretty oneline

git add .
git commit -a -m "### Automated Commit ### $TIME "

