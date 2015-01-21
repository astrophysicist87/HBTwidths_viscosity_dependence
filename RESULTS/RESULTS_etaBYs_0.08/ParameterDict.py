controlParameterList = {
    'simulation_type'       :   'hydro',  # 'hybrid' or 'hydro'
    'niceness'              :   0,       # range from 0 to 19 for process priority, 0 for the highest priority
}

superMCParameters = {
    'which_mc_model'                :   5,
    'sub_model'                     :   1,
    'Aproj'			    :	197,
    'Atarg'			    :	197,
    'Npmin'                         :   278,
    'Npmax'                         :   1000,
    'bmin'                          :   0,
    'bmax'                          :   5.3,
    'ecm'                           :   200,
    'finalFactor'                   :   28.656,
    'alpha'                         :   0.14,
    'lambda'                        :   0.288,
    'nev'                           :   1,
    'shape_of_nucleons'		    :   1,
    'cutdsdy'			    :	0,
    'cc_fluctuation_model'	    :   0,
}

hydroParameters = {
    'vis'       :   0.08, #default is 0.08
    'T0'        :   0.6, # tau_0
    'Edec'      :   0.18,
}

iSSParameters = {
    'number_of_repeated_sampling'   :   1,
    'y_LB'                          :   -2.5,
    'y_RB'                          :   2.5,
}
