HiddenCubeDataset
=================

Ubuntu Requirements:
Python 2.7
sudo apt-get install python-numpy
sudo apt-get install python-scipy
sudo apt-get install python-matplotlib

- IMPORTANT:
  - set a HIDDENCUBE_HOME environment variable to the path to the directory containing this README
    - export HIDDENCUBE_HOME=/path/to/this/directory  (note no slash on the end)

- Explanation of directory file structure:

 - $HIDDENCUBE_HOME/ 
   - Base directory. Contains bash shell scripts that show how to run the main python scripts

 - $HIDDENCUBE_HOME/datasets/
   - directory that holds each different dataset directory

 - $HIDDENCUBE_HOME/datasets/<dataset name>/
   - <dataset name> is the unique user-specified name of a particular dataset
     - matches the -n/--name option for the main generateDataset.py script
   - all dataset-specific information will be inside this directory

 - $HIDDENCUBE_HOME/datasets/<dataset_name>/images/
   - this directory contains all visualizations of rotations performed on the simulated dataset
   - images generated in the initial dataset creation AND later similar rotation explorations are stored here
   - images in this folder are named after their "score"
     - The score is the principal angle between the specific rotation performed on the simulated dataset and the transpose of the rotation used to create the simulated dataset.

  - $HIDDENCUBE_HOME/datasets/<dataset_name>/info/
    - this directory is used to contain text information about rotations performed on the simulated dataset
    - simulatedDataset.txt contains the matrix representing the simulated dataset.
    - simulated_rotation_matrix.txt contains the rotation matrix applied to the wireframe cube that created the simulated dataset.
    - X.XXXXXXXXXXXX_rotation_matrix.txt contains the rotation matrix applied to the simulated dataset used to create the X.XXXXXXXXXXXX.png image
    - X.XXXXXXXXXXXX_seed_matrix.txt contains the normally random seed matrix used to generate a random rotation matrix.  This file is used when generating similar rotation matricies.

  - $HIDDENCUBE_HOME/datasets/<dataset name>/X.XXXXXXXXXXXX_similar_rotations/
    - This directory contains images of rotations created using the similar rotation function.  
    - X.XXXXXXXXXXXX is the principal angle of the rotation that we generate similar rotations to
    - NOTE: images in this folder are also located in the $HIDDENCUBE_HOME/datasets/<dataset name>/images/ directory

  - $HIDDENCUBE_HOME/benchmark
    - contains a benchmarking script and a graph depicting parallel performance

  - $HIDDENCUBE_HOME/scripts
    - contains scripts essential to generating simulated datasets and similar rotations


- How to run the scripts
  - The scripts/generateDataset.py script can be run in two modes: generate dataset and generate similar rotations
  - Running in 'generate dataset' mode
    - export HIDDENCUBE_HOME=/path/to/HiddenCubeDataset
    - python scripts/generateDataset.py --name <dataset name> 
TODO

  - Running in 'similar rotations' mode
TODO


How to run:
  - Look at the ./run.sh script
  - make sure to set the HIDDENCUBE_HOME environment variable as this directory.
    - look at the run.sh script
  - To play a movie similar to what RSVP will show the subject:
    - mplayer mf://*.png  -loop 0 -fps 4
  - To print a movie similar to above but to a file:
    - mencoder mf://*.png -mf type=png:w=512:h=512:fps=4 -ovc x264 -x264encopts preset=slow:tune=film:threads=auto:crf
=18 -o 5Dhist.mov

