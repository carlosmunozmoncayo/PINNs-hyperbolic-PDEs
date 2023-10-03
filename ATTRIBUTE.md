# Attribute

## PINNs

Original Work: *Maziar Raissi, Paris Perdikaris, and George Em Karniadakis*

Github Repo : https://github.com/maziarraissi/PINNs  (Coyright notice preserved)

@article{raissi2017physicsI,
  title={Physics Informed Deep Learning (Part I): Data-driven Solutions of Nonlinear Partial Differential Equations},
  author={Raissi, Maziar and Perdikaris, Paris and Karniadakis, George Em},
  journal={arXiv preprint arXiv:1711.10561},
  year={2017}
}

@article{raissi2017physicsII,
  title={Physics Informed Deep Learning (Part II): Data-driven Discovery of Nonlinear Partial Differential Equations},
  author={Raissi, Maziar and Perdikaris, Paris and Karniadakis, George Em},
  journal={arXiv preprint arXiv:1711.10566},
  year={2017}
}

## Viscous Burgers' equation

The following implementation of PINNs for the viscous Burgers equation was used as a starting point for the present implementation**: https://github.com/jayroxis/PINNs

## CLAWPACK

The generation of reference and training solutions is done with CLAWPACK:

Clawpack Development Team (2020), Clawpack Version 5.7.1,
http://www.clawpack.org, doi: 10.5281/zenodo.4025432  (Coyright notice preserved)

@article{mandli2016clawpack,
    title={Clawpack: building an open source ecosystem for solving hyperbolic PDEs},
    author={Mandli, Kyle T and Ahmadia, Aron J and Berger, Marsha and Calhoun, Donna
    and George, David L and Hadjimichael, Yiannis and Ketcheson, David I
    and Lemoine, Grady I and LeVeque, Randall J},
    journal={PeerJ Computer Science},
    volume={2},
    pages={e68},
    year={2016},
    publisher={PeerJ Inc.},
    doi={10.7717/peerj-cs.68} }

## Shock capturing

A simple gradient-based shock-capturing technique is used following the ideas of Li Liu et al. (2022).
@article{liu2022discontinuity,
  title={Discontinuity Computing using Physics-Informed Neural Network},
  author={Liu, Li and Liu, Shengping and Xie, Hui and Xiong, Fansheng and Yu, Tengchao and Xiao, Mengjuan and Liu, Lufeng and Yong, Heng},
  journal={arXiv preprint arXiv:2206.03864},
  year={2022}
}

## Some ideas for the future
Enforcing conservative, TVD, and entropy-satisfying solutions, as attempted, e.g., by Patel et al. (2022).
@article{patel2022thermodynamically,
  title={Thermodynamically consistent physics-informed neural networks for hyperbolic systems},
  author={Patel, Ravi G and Manickam, Indu and Trask, Nathaniel A and Wood, Mitchell A and Lee, Myoungkyu and Tomas, Ignacio and Cyr, Eric C},
  journal={Journal of Computational Physics},
  volume={449},
  pages={110754},
  year={2022},
  publisher={Elsevier}
}


