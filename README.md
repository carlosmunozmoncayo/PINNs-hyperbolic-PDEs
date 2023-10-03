# PINNs-hyperbolic-PDEs
Simple implementation of Physics Informed Neural Networks for some systems of hyperbolic PDEs using **Pytorch**


-------------------------------------------

## Currently implemented systems:
- ### 1D Inviscid Burgers' equation
  ![Burgers](https://github.com/carlosmunozmoncayo/PINNs-hyperbolic-PDEs/assets/29715468/a8777f6d-e9f6-41b5-818c-4adafba9969c)
- ### 1D Shallow Water Equations with flat bottom
    - Entropy solution
      ![SWEs2](https://github.com/carlosmunozmoncayo/PINNs-hyperbolic-PDEs/assets/29715468/9e807cfc-1c72-4bc1-aa73-c84ffb8e68dd)

    - Entropy violating solution
      ![SWEs](https://github.com/carlosmunozmoncayo/PINNs-hyperbolic-PDEs/assets/29715468/80fb3791-026d-42cf-b5d9-575960bab068)


-------------------------------------------
## Attributes

https://github.com/maziarraissi/PINNs

https://github.com/jayroxis/PINNs

https://github.com/clawpack

Please take a look at the file ATTRIBUTE.md for more details.


-------------------------------------------
## Requirements
My specific setup is provided in the file **requirements.txt**, but the following Python libraries are required
- NumPy 
- Matplotlib
- PyTorch
- pyDOE
- scipy
- Jupyter Notebook
- CLAWPACK (If you want to set up a custom problem, data is provided for each system otherwise)





