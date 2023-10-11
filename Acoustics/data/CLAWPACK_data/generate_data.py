from acoustics_1d import setup as clawpack_setup
import numpy as np

def generate_claw():
    claw = clawpack_setup(nout=100)
    #claw.verbosity= 0
    claw.run()
    return claw

def construct_data_dictionaries(claw):
    frames = claw.frames
    data_dict = {}
    data_dict["x"] = (frames[0].state.grid.x.centers).reshape(-1,1)
    t_list = []
    usol_list = []
    for i in range(len(frames)):
        t_list.append(frames[i].t)
        usol_list.append(frames[i].state.q.T)

    data_dict["t"] = np.array(t_list).reshape(-1,1)
    data_dict["usol"] = np.array(usol_list) # shape (n_t, n_x, 2)
    data_dict["impedances"] = frames[0].state.aux[0,:]
    data_dict["soundspeeds"] = frames[0].state.aux[1,:]
    data_dict["interfaces"] = frames[0].state.aux[2,frames[0].state.aux[2,:]<1e9]
    data_dict["bulks"] = frames[0].state.aux[3,frames[0].state.aux[3,:]<1e9]
    data_dict["rhos"] = frames[0].state.aux[4,frames[0].state.aux[4,:]<1e9]
    return data_dict

def write_data_dict(filename="../Acoustics_data_CLAWPACK.npy"):
    #Meant to be run locally
    claw = generate_claw()
    data_dict = construct_data_dictionaries(claw)
    np.save(filename, data_dict)

def read_data_dict(filename="../Acoustics_data_CLAWPACK.npy"):
    #Meant to be run locally
    data_dict = np.load(filename, allow_pickle=True).item()
    return data_dict

if __name__ == "__main__":
    write_data_dict()