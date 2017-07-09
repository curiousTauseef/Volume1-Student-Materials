#!/bin/bash
# Download the data files for this volume and put them in the right folders.

SOURCE="https://github.com/Foundations-of-Applied-Mathematics/Data.git"
GIT="https://git-scm.com"
TEMPDIR="_DATA_"`date +%s`"_"
PYTHONESSENTIALS="$TEMPDIR/PythonEssentials"
VOLUME1="$TEMPDIR/Volume1"

# Check that git is installed.
command -v git > /dev/null ||
{ echo -e "\nERROR: git is required. Download it at $GIT.\n"; exit 1; }

# Download the data using git sparse checkout and git lfs.
mkdir $TEMPDIR
cd $TEMPDIR
git init --quiet
echo -e "\nInitializing Download ...\n"
git remote add -f origin $SOURCE
git config core.sparseCheckout true
echo "PythonEssentials" >> .git/info/sparse-checkout
echo "Volume1" >> .git/info/sparse-checkout
git pull origin master
cd ../

# Migrate the files from the temporary folder.
set +e
echo -e "\nMigrating files ..."

mv $PYTHONESSENTIALS/grid.npy NumpyIntro/
mv $PYTHONESSENTIALS/FARS.npy MatplotlibIntro/
mv $PYTHONESSENTIALS/hello_world.txt Exceptions_FileIO/
mv $PYTHONESSENTIALS/cf_example1.txt Exceptions_FileIO/
mv $PYTHONESSENTIALS/cf_example2.txt Exceptions_FileIO/
mv $PYTHONESSENTIALS/MLB.npy DataVisualization/
mv $PYTHONESSENTIALS/anscombe.npy DataVisualization/
mv $PYTHONESSENTIALS/countries.npy DataVisualization/
mv $PYTHONESSENTIALS/earthquakes.npy DataVisualization/

mv $VOLUME1/horse.npy LinearTransformations/
mv $VOLUME1/circle.npy LeastSquares_Eigenvalues/
mv $VOLUME1/ellipse.npy LeastSquares_Eigenvalues/
mv $VOLUME1/housing.npy LeastSquares_Eigenvalues/
mv $VOLUME1/dream.png ImageSegmentation/
mv $VOLUME1/dream_gray.png ImageSegmentation/
mv $VOLUME1/monument.png ImageSegmentation/
mv $VOLUME1/monument_gray.png ImageSegmentation/
mv $VOLUME1/hubble.jpg SVD_ImageCompression/
mv $VOLUME1/hubble_gray.jpg SVD_ImageCompression/
mv $VOLUME1/faces94.zip FacialRecognition/
mv $VOLUME1/plane.npy Differentiation/
mv $VOLUME1/stability_data.npy Conditioning_Stability/
mv $VOLUME1/matrix.txt PageRank/
mv $VOLUME1/ncaa2013.csv PageRank/
mv $VOLUME1/social_network.csv DrazinInverse/

# Delete the temporary folder.
rm -rf $TEMPDIR
echo -e "\nDone.\n"
