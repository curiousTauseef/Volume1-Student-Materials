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

mv $PYTHONESSENTIALS/grid.npy NumpyIntro/
mv $PYTHONESSENTIALS/FARS.npy MatplotlibIntro/
mv $PYTHONESSENTIALS/MLB.npy DataVisualization/
mv $PYTHONESSENTIALS/anscombe.npy DataVisualization/
mv $PYTHONESSENTIALS/countries.npy DataVisualization/
mv $PYTHONESSENTIALS/earthquakes.npy DataVisualization/

mv $VOLUME1/pi.npy LinearTransformations/
mv $VOLUME1/horse.npy LinearTransformations/
mv $VOLUME1/circle.npy LeastSquares_Eigenvalues/
mv $VOLUME1/ellipse.npy LeastSquares_Eigenvalues/
mv $VOLUME1/housing.npy LeastSquares_Eigenvalues/
mv $VOLUME1/dream.png ImageSegmentation/
mv $VOLUME1/hubble_image.jpg SVD_ImageCompression/
# mv $VOLUME1/cameraman.jpg NumericalDifferentiation/
mv $VOLUME1/matrix.txt PageRank/
mv $VOLUME1/ncaa2013.csv PageRank/

# Delete the temporary folder and return to the original folder.
cd ../
rm -rf $TEMPDIR
cd $START
