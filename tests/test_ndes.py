import jax
import jax.numpy as jnp
import jax.random as jr
import diffrax as dfx

from sbiax.ndes import CNF, MAF

"""
    Test NDEs: CNFs and MAFs.
"""


def test_cnf():
    key = jr.key(0)

    solver = getattr(dfx, "Euler")()
    parameter_dim = 2

    cnf = CNF(
        event_dim=parameter_dim, 
        context_dim=parameter_dim, 
        width_size=8,
        depth=0,
        solver=solver,
        activation=jax.nn.tanh,
        dt=0.1, 
        t1=1.0, 
        dropout_rate=0.,
        exact_log_prob=True,
        scaler=None,
        key=key
    )

    y = jnp.ones((parameter_dim,)) 

    x = cnf.sample_and_log_prob(key, y)
    p_x_y = cnf.log_prob(x, y)


def test_maf():
    key = jr.key(0)

    parameter_dim = 2

    maf = MAF(
        event_dim=parameter_dim, 
        context_dim=parameter_dim, 
        width_size=32,
        depth=2,
        nn_depth=3,
        n_layers=5,
        activation=jax.nn.tanh,
        scaler=None,
        key=key
    )

    y = jnp.ones((parameter_dim,)) 

    x = maf.sample_and_log_prob(key, y)
    p_x_y = maf.log_prob(x, y)