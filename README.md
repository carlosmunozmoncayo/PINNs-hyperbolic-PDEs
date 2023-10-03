# PINNs-hyperbolic-PDEs
Simple implementation of Physics Informed Neural Networks for some systems of hyperbolic PDEs using **Pytorch**


-------------------------------------------

## Currently implemented systems
- ### 1D Inviscid Burgers' equation
  ![Burgers](https://github.com/carlosmunozmoncayo/PINNs-hyperbolic-PDEs/assets/29715468/dc930538-bc51-425f-9729-09895025e0f4)

- ### 1D Shallow Water Equations with flat bottom
    - Entropy solution
      ![SWEs2](https://github.com/carlosmunozmoncayo/PINNs-hyperbolic-PDEs/assets/29715468/9a0f7f2d-4708-479b-b58e-1c36bfc7b03c)

    - Entropy violating solution
      ![SWEs](https://github.com/carlosmunozmoncayo/PINNs-hyperbolic-PDEs/assets/29715468/e196789a-f57b-490c-b9b2-036ca25b0624)



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





