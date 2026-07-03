# BrainSignal Simulator

## 1. Project Overview

BrainSignal Simulator is a modular computational framework for simulating dynamical systems, biological neurons, and neural computation models. It unifies continuous-time differential equation systems and discrete neural network computation under a single simulation engine.

The project supports:

- Chaotic dynamical systems (Lorenz system)
- Biophysical neuron models (LIF, Izhikevich)
- Artificial neural networks (ANN)
- Spiking neural networks (SNN extension ready)
- Multiple numerical integration methods (Euler, RK4, Adaptive RK, Leapfrog, Verlet)

The architecture is designed to be extensible for research in computational neuroscience and numerical simulation.

---



## 2. Directory Structure

- `app/main.py` – FastAPI entry point
- `api/` – REST endpoints
- `core/` – simulation engine, scheduler, logger
- `models/` – differential equation models
- `neural/` – ANN and SNN models
- `solvers/` – numerical integration methods
- `math/` – symbolic expression system
- `data/` – simulation results and datasets
- `schemas/` – request/response validation
- `services/` – business logic layer
- `storage/` – persistence layer (JSON-based)
- `frontend/` – visualization UI

---

## 3. Mathematical Models

### 3.1 Lorenz System

dx/dt = σ (y - x)  
dy/dt = x (ρ - z) - y  
dz/dt = x y - β z  

State vector:

[x, y, z]


Behavior:
- chaotic attractor
- non-linear sensitivity
- continuous time evolution

---

### 3.2 LIF Neuron

dV/dt = (-(V - V_rest) + R * I) / τ  

Where:
- V: membrane potential
- V_rest: resting potential
- R: resistance
- I: input current
- τ: time constant

Spike condition:

if V >= threshold → reset


State:

[V]


---

### 3.3 Izhikevich Neuron

dV/dt = 0.04V² + 5V + 140 - u + I  
du/dt = a(bV - u)

State:

[V, u]


Behavior types:
- tonic spiking
- bursting
- chaotic firing

---

### 3.4 Artificial Neural Network (ANN)

Discrete update rule:

x_{t+1} = W · x_t

Simplified implementation:

x(t+1) = Σ (w_i * x_i)

State:

[x]


ANN bypasses ODE solvers and uses direct forward computation.

---

## 4. Numerical Solvers

### 4.1 Euler Solver

x_{n+1} = x_n + dt * f(x, t)

Used for:
- fast approximation
- neural models (LIF, Izhikevich in low precision mode)

---

### 4.2 RK4 Solver

k1 = f(x, t)  
k2 = f(x + dt/2 k1, t + dt/2)  
k3 = f(x + dt/2 k2, t + dt/2)  
k4 = f(x + dt k3, t + dt)

x_{n+1} = x_n + dt/6 (k1 + 2k2 + 2k3 + 2k4)

Used for:
- Lorenz system
- high precision neuron models

---

### 4.3 Adaptive RK Solver

Adaptive step control:

error = |x_high - x_low|

If error > tolerance → reduce dt  
If error < tolerance → increase dt

Used for:
- stiff systems
- dynamic stability simulation

---

### 4.4 Additional Solvers (implemented)

- Leapfrog Solver (energy-preserving systems)
- Verlet Solver (physics-based integration)
- Improved Euler Solver (Heun method)

---

## 5. Core Simulation Engine

SimulationEngine is responsible for:

- time evolution
- state storage
- model execution
- solver dispatching

Execution flow:

1. Model initialized
2. Solver attached
3. Scheduler generates time steps
4. At each step:
   - ANN → direct forward computation
   - ODE → solver integration
5. State stored in history
6. SimulationResult returned

---

## 6. ANN Execution Mode

ANN bypass logic:

- no differential equations
- no solver usage
- direct step update

Input generation:

x = [base, base * 0.9, base * 0.8]

Output:

x(t+1) = ANN.forward(x)

---

## 7. API Specification

### POST /simulation/run

Request:

```json
{
  "model": "lorenz",
  "solver": "rk4",
  "T": 10,
  "dt": 0.01,
  "params": {}
}
```
Response:
```json
{
  "model": "LorenzSystem",
  "solver": "RK4Solver",
  "time": [...],
  "states": [
    {"x": 1.0, "y": 2.0, "z": 3.0}
  ]
}
```
## 8. Data Layer
### SimulationResult

Stores:

- time_points
- states
- model metadata
- solver metadata

## 9. Math Engine

### Custom symbolic system includes:

- Variable
- Constant
- Binary expressions
- Evaluator
- Context

Used in:

LIF neuron equation evaluation
future symbolic models
## 10. Neural Layer
### ANN
- feedforward structure
- random weight initialization
- vector input processing
### SNN (planned extension)
- spike-based computation
- event-driven updates
- raster visualization support