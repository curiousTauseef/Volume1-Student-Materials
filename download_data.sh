#!/bin/bash
# Download the data files for this repo and put them in the right folders.

GIT="https://git-scm.com"
GITLFS="https://git-lfs.github.com"
TEMPDIR="__TEMP_DATA_DOWNLOAD__"
PYTHONESSENTIALS="../$TEMPDIR/PythonEssentials"
VOLUME1="../$TEMPDIR/Volume1"

set +e

# Check that git and git-lfs are installed.
command -v git ||
{ echo -e "\nERROR: git is required. Download it at $GIT.\n"; exit 1; }
command -v git-lfs ||
{ echo -e "\nERROR: git-lfs is required. Download it at $GITLFS.\n"; exit 1; }

# Make a temporary neighboring repository for the data download.
START=`pwd`
cd ../
mkdir $TEMPDIR
cd $TEMPDIR

# Download the data using git sparse checkout and git lfs.
git init
git-lfs install
git remote add -f origin https://github.com/Foundations-of-Applied-Mathematics/Data.git
git config core.sparseCheckout true
echo "PythonEssentials" >> .git/info/sparse-checkout
echo "Volume1" >> .git/info/sparse-checkout
echo -e "\nInitializing Download\n"
git pull origin master

# Copy the files over from the temporary folder.
cd $START

mv $PYTHONESSENTIALS/grid.npy NumpyIntro/grid.npy
mv $PYTHONESSENTIALS/FARS.npy MatplotlibIntro/FARS.npy
mv $PYTHONESSENTIALS/MLB.npy DataVisualization/MLB.npy
mv $PYTHONESSENTIALS/anscombe.npy DataVisualization/anscombe.npy
mv $PYTHONESSENTIALS/countries.npy DataVisualization/countries.npy
mv $PYTHONESSENTIALS/earthquakes.npy DataVisualization/earthquakes.npy

mv $VOLUME1/pi.npy LinearTransformations/pi.npy
mv $VOLUME1/horse.npy LinearTransformations/horse.npy
mv $VOLUME1/circle.npy LeastSquares_Eigenvalues/circle.npy
mv $VOLUME1/ellipse.npy LeastSquares_Eigenvalues/ellipse.npy
mv $VOLUME1/housing.npy LeastSquares_Eigenvalues/housing.npy
mv $VOLUME1/dream.png ImageSegmentation/dream.png
mv $VOLUME1/hubble_image.jpg SVD_ImageCompression/hubble_image.jpg
# mv $VOLUME1/cameraman.jpg NumericalDifferentiation/cameraman.jpg
mv $VOLUME1/matrix.txt PageRank/matrix.txt
mv $VOLUME1/ncaa2013.csv PageRank/ncaa2013.csv

# Delete the temporary folder and return to the original folder.
cd ../
rm -rf $TEMPDIR
cd $START
