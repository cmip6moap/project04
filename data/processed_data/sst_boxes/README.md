Data processed by Katherine Turner for the Bristol CMIP6 Hackathon, 2-4 June 2021

This folder contains area files for CMIP6 models to calculate various SST indices for comparison with AMOC strength:

in the files that end with xx_SSTareas.nc

box_amv1: AMV1 index (0-60N, 50W-10E) to be calculated as a difference with the global mean
box_amv2: AMV2 index (40-60N, 50W-10E) to be calculated as a difference with the minus global mean

box_sd1 and box_sd2: SST_dipole index (45-80N, 70W-30E and 0-45S, 70W-30E) to be calculated as box_sd1 - box_sd2

in the files that end with xx_subpolarSSTareas.nc

box_sg: Subpolar gyre region as defined by Caeasar et al 2018
     these regions are a bit blagged (concavity around the southern tip of Greenland not fully copied from the Caesar et al txt file, and I use nearest neighbours for latitudes and mappings rather than linear interpolation)

The code (poorly written) can be found in /project04/notebooks/sst_boxes/create_sstboxes.ipynb
