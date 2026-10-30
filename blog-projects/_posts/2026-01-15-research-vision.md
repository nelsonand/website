---
layout: post
title: "Plasma-Informed Engineering of Fusion Power Plants: My Research Vision"
cover-img: blog-projects/assets/img/MANTA_cover.jpg
thumbnail-img: blog-projects/assets/img/NTPT_cartoon.jpg
share-img: blog-projects/assets/img/NTPT_cartoon.jpg
category: projects
last-updated: 2026-10-30
---

Fusion energy has entered a decisive decade. The National Academies call for a U.S. pilot plant producing net electricity in the 2035–2040 timeframe, the Department of Energy has released a national roadmap to get there, and private companies are now designing, financing, and building real machines. As fusion moves from experiment to power plant, its most pressing obstacles have become **increasingly interdisciplinary, with strong elements of mechanical engineering**: removing extreme, transient heat loads from plasma-facing components, ensuring structural integrity and component lifetime under demanding operating conditions, and optimizing plant designs that remain viable despite deep uncertainty in the underlying physics.

These problems share a common feature: **their boundary conditions are set by the plasma**. Engineering tools typically treat the plasma as a fixed, idealized heat source, while plasma physics models typically stop at the edge of the plasma. My research lives at this interface. Its central thesis is that fusion engineering and plasma physics must be co-designed, because choosing the plasma operating regime is itself a powerful engineering design variable.

## Foundation: designing the plasma to make engineering possible

My career so far has focused on the boundary between a hot fusion core and the material walls that contain it. My Ph.D. work at Princeton developed automated, integrated models of the tokamak edge. At Columbia, I became part of the international effort on **negative triangularity (NT)**, a reversed plasma shape that robustly eliminates the edge instabilities responsible for repeated bursts of heat onto reactor walls. Our DIII-D team received the [2026 APS John Dawson Award](/2026-09-30-dawson-award/) for this work, and I now lead the joint EU/US working group on NT.

![NT vs PT comparison](/blog-projects/assets/img/NTPT_cartoon.jpg)
*Positive (left) and negative (right) triangularity plasma cross-sections. The geometric difference is simple; the engineering consequences are profound.*

Much of my recent work translates these physics lessons into integrated plant designs. I advised the student teams that designed the [MANTA and CENTAUR](/2023-10-29-nt-reactors/) pilot plants, developed vertical stability control requirements for Commonwealth Fusion Systems' SPARC tokamak, currently lead pulse design for their ARC power plant, and lead power plant design for Maritime Fusion.

## Thrust 1: risk-informed design of fusion power plants

Fusion plant design is constrained as much by cost and reliability as by physics. In a study I co-led with General Atomics, we performed more than 200,000 integrated design evaluations to compare conventional designs with NT. Both concepts delivered similar cost and performance, but a modest change in a few uncertain plasma constraints eliminated every viable conventional design while the NT designs remained robust. That result suggests that plant design must be *risk-informed*. My group will pursue this through three aims:

- **Uncertainty-aware, multi-fidelity design optimization:** embedding calibrated physics uncertainties (see my post on [validation and uncertainty quantification](/2026-10-16-vvuq/)) into plant optimization, and using value-of-information analysis to choose the experiments that retire the most design risk.
- **Mission-driven and AI-assisted design:** formalizing requirements-driven design for different fusion missions, from grid-scale plants to process heat and marine power, and exploring agentic AI for design-space exploration.
- **Design for maintainability and evolution:** quantifying the value of replaceable components and upgradeable subsystems for plants that may operate for decades while physics and technology evolve.

## Thrust 2: designing for power exhaust, from plasma to coolant

Tokamak divertors must handle steady heat fluxes comparable to a rocket nozzle throat, deposited on a strip a few millimeters wide and sustained for years, along with transient events that can exceed melting limits. Yet heat removal systems are usually designed against static, idealized heat loads. Predictive thermal-fluid models are only as reliable as their plasma boundary conditions, so my group will:

- build **uncertainty-quantified heat-load boundary conditions**, mapping plasma scenarios to probabilistic, time-resolved heat-flux maps that thermal engineers can couple to their own analyses;
- develop **thermally constrained plasma pulse design**, where surface temperature, coolant margin, and accumulated fatigue act as real-time constraints on how a plasma is ramped, sustained, and terminated; and
- model the **thermal dynamics of pulsed fusion plants** end to end, from plasma pulse to first wall, blanket, coolant, and power cycle.

## Why this matters

Fusion's commercialization depends on engineers who understand both plasmas and machines. My goal is to build a group whose students can move fluently between plasma physics, thermal and structural engineering, and data-driven design, because the problems at the frontier of fusion require all three at once. A longer description of each thrust is on my [Research](/projects/) page.

## Selected publications on this subject:

**[Exploring the fusion power plant design space: comparative analysis of positive and negative triangularity tokamaks through optimization](https://doi.org/10.1088/1741-4326/ae27e6)**<br />
Slendebroek, T., **Nelson, A. O.**, Meneghini, O. et al., _Nuclear Fusion_ **66**, 026032 (2026).

**[MANTA: a negative-triangularity NASEM-compliant fusion pilot plant](https://doi.org/10.1088/1361-6587/ad6708)**<br />
The MANTA Collaboration, _Plasma Physics and Controlled Fusion_ **66**, 105006 (2024).

**[Implications of vertical stability control on the SPARC tokamak](https://doi.org/10.1088/1741-4326/ad58f6)**<br />
**Nelson, A. O.**, Garnier, D. T., Battaglia, D. J., Paz-Soldan, C., Stewart, I., Reinke, M., Creely, A. J. & Wai, J., _Nuclear Fusion_ **64**, 086040 (2024).

**[Robust Avoidance of Edge-Localized Modes alongside Gradient Formation in the Negative Triangularity Tokamak Edge](https://doi.org/10.1103/PhysRevLett.131.195101)**<br />
**Nelson, A. O.**, Schmitz, L., Paz-Soldan, C., Thome, K. E., Cote, T. B., Leuthold, N., Scotti, F., Austin, M. E., Hyatt, A. & Osborne, T., _Physical Review Letters_ **131**, 195101 (2023).
