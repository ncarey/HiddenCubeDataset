HiddenCubeDataset
=================

Ubuntu Requirements:
Python 2.7
sudo apt-get install python-numpy
sudo apt-get install python-scipy
sudo apt-get install python-matplotlib

How to run:
  - Look at the ./run.sh script
  - make sure to set the HIDDENCUBE_HOME environment variable as this directory.
    - look at the run.sh script
  - To play a movie similar to what RSVP will show the subject:
    - mplayer mf://*.png  -loop 0 -fps 4
  - To print a movie similar to above but to a file:
    - mencoder mf://*.png -mf type=png:w=512:h=512:fps=4 -ovc x264 -x264encopts preset=slow:tune=film:threads=auto:crf
=18 -o 5Dhist.mov

