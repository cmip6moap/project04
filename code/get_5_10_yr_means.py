'''
first and last 5 or 10 year means for ssp126 simulations

northern cluster: gauges  5-29 , 
southern cluster: gauges 30-35

use python --> pickle.load() to open

organised:
['simulation name',np.array(first mean, last mean, first std, last std)]
         ^
     as in JR's 
       output
'''


from glob import glob
import numpy as np
import xarray as xr
import pickle

fileDirectory = '/gws/pw/j05/cop26_hackathons/bristol/project04/raw_data/CMIP6/gheight/ScenarioMIP/ssp126/'
simNames      =['ACCESS-CM2_ssp126_r1i1p1f1',
                'ACCESS-CM2_ssp126_r2i1p1f1',
                'ACCESS-CM2_ssp126_r3i1p1f1',
                'ACCESS-ESM1-5_ssp126_r1i1p1f1',
                'ACCESS-ESM1-5_ssp126_r2i1p1f1',
                'ACCESS-ESM1-5_ssp126_r3i1p1f1',
                'BCC-CSM2-MR_ssp126_r1i1p1f1',
                'CAMS-CSM1-0_ssp126_r1i1p1f1',
                'CAMS-CSM1-0_ssp126_r2i1p1f1',
                'CESM2-WACCM_ssp126_r1i1p1f1',
                'CIESM_ssp126_r1i1p1f1',
                'CMCC-CM2-SR5_ssp126_r1i1p1f1',
                'CMCC-ESM2_ssp126_r1i1p1f1',
                'CNRM-CM6-1_ssp126_r1i1p1f2',
                'CNRM-CM6-1_ssp126_r2i1p1f2',
                'CNRM-CM6-1_ssp126_r3i1p1f2',
                'CNRM-CM6-1_ssp126_r4i1p1f2',
                'CNRM-CM6-1_ssp126_r5i1p1f2',
                'CNRM-CM6-1_ssp126_r6i1p1f2',
                'CanESM5_ssp126_r10i1p1f1',
                'CanESM5_ssp126_r10i1p2f1',
                'CanESM5_ssp126_r1i1p1f1',
                'CanESM5_ssp126_r1i1p2f1',
                'CanESM5_ssp126_r2i1p1f1',
                'CanESM5_ssp126_r2i1p2f1',
                'CanESM5_ssp126_r3i1p1f1',
                'CanESM5_ssp126_r3i1p2f1',
                'CanESM5_ssp126_r4i1p1f1',
                'CanESM5_ssp126_r4i1p2f1',
                'CanESM5_ssp126_r5i1p1f1',
                'CanESM5_ssp126_r5i1p2f1',
                'CanESM5_ssp126_r6i1p1f1',
                'CanESM5_ssp126_r6i1p2f1',
                'CanESM5_ssp126_r7i1p1f1',
                'CanESM5_ssp126_r7i1p2f1',
                'CanESM5_ssp126_r8i1p1f1',
                'CanESM5_ssp126_r9i1p1f1',
                'CanESM5_ssp126_r9i1p2f1']
suffix        = '_gn_gheight.nc'

def get_first_last_n_yr_means(simID, years = 10, cluster = 'Northern'):
    # get data from Jonathan's output
    simName   = simNames[simID]
    file      = fileDirectory + simName + suffix
    dataset   = xr.load_dataset(file)
    # mean over northern gauges
    if cluster == 'Northern':
	gheight   = dataset['gheight'].sel(gauges=slice(5,29))
    else:
    	gheight   = dataset['gheight'].sel(gauges=slice(30,36))
    gheight   = gheight.mean(dim='gauges')
    # mean and std over first 10 years
    time      = np.array(dataset['time'])
    numMonths = years*12
    frstTs    = time[:numMonths]
    lastTs    = time[-numMonths:]
    frstHs    = gheight.sel(time=slice(frstTs[0],frstTs[-1]))
    lastHs    = gheight.sel(time=slice(lastTs[0],lastTs[-1]))
    return [simName,
            np.array([frstHs.mean(dim='time').values, 
                      lastHs.mean(dim='time').values,
                      frstHs.std(dim='time').values, 
                      lastHs.std(dim='time').values])]

yearsList = [5,10]
clusters  = ['Northern','Southern']

for years in yearsList:
    for cluster in clusters:

        saveFile  = 'ssp126_'+ cluster +'_cluser_first_last_' + str(years) + '_years_mean' 
        saveArray = []
        for i in range(len(simNames)):
            saveArray.append(get_first_last_n_yr_means(i, years, cluster))

        pickle.dump(saveArray, open( saveFile+'.p', 'wb' ))