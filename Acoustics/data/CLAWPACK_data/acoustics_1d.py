#!/usr/bin/env python
# encoding: utf-8

r"""
One-dimensional acoustics
=========================

Solve the (linear) acoustics equations:

.. math::
    p_t + K u_x & = 0 \\
    u_t + p_x / \rho & = 0.

Here p is the pressure, u is the velocity, K is the bulk modulus,
and :math:`\rho` is the density.

The initial condition is a Gaussian and the boundary conditions are periodic.
The final solution is identical to the initial data because both waves have
crossed the domain exactly once.
"""
from __future__ import absolute_import
from numpy import sqrt, exp, cos
from clawpack import riemann


def setup(use_petsc=False, kernel_language='Fortran', solver_type='sharpclaw',
          outdir='./_output', ptwise=False, weno_order=5,
          time_integrator='SSP104', disable_output=False, output_style=1, nout=100):

    if use_petsc:
        import clawpack.petclaw as pyclaw
    else:
        from clawpack import pyclaw

    if kernel_language == 'Fortran':
        riemann_solver = riemann.acoustics_variable_1D#riemann.acoustics_1D


    if solver_type == 'classic':
        solver = pyclaw.ClawSolver1D(riemann_solver)
        solver.limiters = pyclaw.limiters.tvd.MC
    elif solver_type == 'sharpclaw':
        solver = pyclaw.SharpClawSolver1D(riemann_solver)
        solver.weno_order = weno_order
        solver.time_integrator = time_integrator
        if time_integrator == 'SSPLMMk3':
            solver.lmm_steps = 4
    else:
        raise Exception('Unrecognized value of solver_type.')

    solver.kernel_language = kernel_language

    x = pyclaw.Dimension(-5.0, 5.0, 2000, name='x')
    domain = pyclaw.Domain(x)
    num_eqn = 2
    num_aux = 5
    #Third component will have the interfaces between the different materials
    #Fourth component will have the bulks between interfaces
    #Fifth component will have the densities between interfaces

    state = pyclaw.State(domain, num_eqn, num_aux)

    solver.bc_lower[0] = pyclaw.BC.extrap
    solver.bc_upper[0] = pyclaw.BC.extrap
    solver.aux_bc_lower[0] = pyclaw.BC.extrap
    solver.aux_bc_upper[0] = pyclaw.BC.extrap

    #rho = 1.0   # Material density
    #bulk = 2.0  # Material bulk modulus



    list_bulks = [1.,0.5,1.,1.]
    list_rhos = [1.,2.,1.,6.]
    list_impedances = [sqrt(rho*bulk) for rho,bulk in zip(list_rhos,list_bulks)]
    list_soundspeeds = [sqrt(bulk/rho) for rho,bulk in zip(list_rhos,list_bulks)]
    print(f"List of impedances: {list_impedances}")
    print(f"List of soundspeeds: {list_soundspeeds}")

    

    xc = domain.grid.x.centers

    #Split the domain into N regions, where N = len(list_bulks)
    N = len(list_bulks)
    interfaces_x = [xc[int(i*len(xc)/N)] for i in range(1,N)] #without the first and last points
    constraintL= []
    constraintR = []
    for interface in interfaces_x:
        constraintL.append(xc<interface)
        constraintR.append(xc>=interface)
    
    #First region
    state.aux[0, :] = list_impedances[0]*constraintL[0]
    state.aux[1, :] = list_soundspeeds[0]*constraintL[0]
    for i in range(len(constraintL)-1):
        state.aux[0, :] += list_impedances[i+1]*constraintL[i+1]*constraintR[i]
        state.aux[1, :] += list_soundspeeds[i+1]*constraintL[i+1]*constraintR[i]
    
    #Last region
    state.aux[0, :] += list_impedances[-1]*constraintR[-1]
    state.aux[1, :] += list_soundspeeds[-1]*constraintR[-1]


    #Saving some useful data to retrieve later
    state.aux[2,:] = 1e10 #big number, maybe Nan would be better
    state.aux[3,:] = 1e10 #big number, maybe Nan would be better
    state.aux[4,:] = 1e10 #big number, maybe Nan would be better

    #Fill interfaces in aux
    for i in range(len(interfaces_x)):
        state.aux[2, i] = interfaces_x[i]
    
    #Fill bulk and soundspeed in aux
    for j in range(len(list_bulks)):
        state.aux[3, j] = list_bulks[j]
        state.aux[4, j] = list_rhos[j]
    


    print(f"Interfaces: {state.aux[2,state.aux[2,:]<1e9]}")
    print(f"Bulks: {state.aux[3,state.aux[3,:]<1e9]}")
    print(f"Densities: {state.aux[4,state.aux[4,:]<1e9]}")

    beta = 4.
    gamma = 0
    delta_interface = interfaces_x[0]-xc[0]
    x0 = (interfaces_x[0]+xc[0])/2.

    state.q[0, :] = exp(-beta * (xc-x0)**2)*(xc<interfaces_x[0]) #* cos(gamma * (xc - x0))
    state.q[1, :] = state.q[0, :]/list_impedances[0]


    solver.dt_initial = domain.grid.delta[0]*0.1# / state.problem_data['cc'] * 0.1

    claw = pyclaw.Controller()
    claw.solution = pyclaw.Solution(state, domain)
    claw.solver = solver
    claw.outdir = outdir
    claw.output_style = output_style
    if output_style == 1:
        claw.tfinal = 10.0
        claw.num_output_times = nout
    elif output_style == 3:
        claw.nstep = 1
        claw.num_output_times = nout
    claw.keep_copy = True
    if disable_output:
        claw.output_format = None
    claw.setplot = setplot

    return claw


def setplot(plotdata):
    """
    Specify what is to be plotted at each frame.
    Input:  plotdata, an instance of visclaw.data.ClawPlotData.
    Output: a modified version of plotdata.
    """
    plotdata.clearfigures()  # clear any old figures,axes,items data

    # Figure for pressure
    plotfigure = plotdata.new_plotfigure(name='Pressure', figno=1)

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes()
    plotaxes.axescmd = 'subplot(211)'
    plotaxes.ylimits = [-3., 3.]
    plotaxes.title = 'Pressure'

    # Set up for item on these axes:
    plotitem = plotaxes.new_plotitem(plot_type='1d_plot')
    plotitem.plot_var = 0
    #plotitem.plotstyle = '-o'
    plotitem.color = 'b'
    plotitem.kwargs = {'linewidth': 2, 'markersize': 5}

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes()
    plotaxes.axescmd = 'subplot(212)'
    plotaxes.xlimits = 'auto'
    plotaxes.ylimits = [-3., 3.]
    plotaxes.title = 'Velocity'

    # Set up for item on these axes:
    plotitem = plotaxes.new_plotitem(plot_type='1d_plot')
    plotitem.plot_var = 1
    plotitem.plotstyle = '-'
    plotitem.color = 'b'
    plotitem.kwargs = {'linewidth': 2, 'markersize': 5}

    return plotdata


def run_and_plot(**kwargs):
    claw = setup(kwargs)
    claw.run()
    from clawpack.pyclaw import plot
    plot.interactive_plot(setplot=setplot)

if __name__ == "__main__":
    from clawpack.pyclaw.util import run_app_from_main
    output = run_app_from_main(setup, setplot)
