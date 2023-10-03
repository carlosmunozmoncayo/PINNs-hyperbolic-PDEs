from burgers_1d import setup as clawpack_setup
import numpy as np

def generate_claw():
    claw = clawpack_setup()
    claw.verbosity= 0
    claw.run()
    return claw

def construct_data_dictionaries(claw):
    frames = claw.frames
    data_dict = {}
    data_dict["x"] = (claw.frames[0].state.grid.x.centers).reshape(-1,1)
    t_list = []
    usol_list = []
    for i in range(len(frames)):
        t_list.append(frames[i].t)
        usol_list.append(frames[i].state.q[0])

    data_dict["t"] = np.array(t_list).reshape(-1,1)
    data_dict["usol"] = np.array(usol_list).T
    return data_dict

def write_data_dict():
    #Meant to be run locally
    claw = generate_claw()
    data_dict = construct_data_dictionaries(claw)
    np.save("../burgers_data_CLAWPACK.npy", data_dict)

def read_data_dict():
    #Meant to be run locally
    data_dict = np.load("../burgers_data_CLAWPACK.npy", allow_pickle=True).item()
    return data_dict

if __name__ == "__main__":
    write_data_dict()