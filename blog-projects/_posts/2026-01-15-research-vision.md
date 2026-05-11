---
layout: post
title: "Building the Physics Foundation for Fusion Pilot Plants: My Research Program"
cover-img: blog-projects/assets/img/diag2diag_cover.png
thumbnail-img: blog-projects/assets/img/NTPT_cartoon.png
share-img: blog-projects/assets/img/NTPT_cartoon.png
category: projects
---

When I think about what it will take to build the world's first fusion pilot plant, I keep coming back to the same set of unsolved problems. We know the physics of ignition well enough to design a machine that can achieve it. What we don't yet know is how to build a machine that can sustain those conditions reliably — surviving the relentless heat loads on its walls, remaining stable against a zoo of instabilities, and doing all of this efficiently enough to produce net electrical power. Closing those gaps is what my research program is organized around.

My work falls into three connected thrusts that together address what I see as the central physics and engineering challenges on the path to pilot plants.

**The first thrust is developing and validating ELM-free plasma scenarios.** Edge-localized modes (ELMs) are periodic plasma instabilities that release enormous heat pulses onto tokamak walls — pulses that would rapidly damage the components of any device operating at fusion-relevant power levels. Existing ELM suppression techniques exist, but most are sensitive to plasma conditions and carry performance penalties. My primary focus has been on negative triangularity (NT), a simple change to the shape of the plasma cross-section that eliminates the trigger for ELMs entirely. Over the past several years, my group has demonstrated that NT ELM suppression is robust, compatible with high core performance, and persists even under conditions that would cause conventional ELMs to reappear. We have now extended this work to multiple tokamaks across three continents and are building the database needed to make confident pilot plant projections.

**The second thrust is stability and control modeling for whole-device operation.** A pilot plant is not a physics experiment — it is a machine that must operate continuously and safely across a wide envelope of conditions. This requires us to understand not just what plasma configurations are desirable, but which ones are reachable and maintainable via active control. My work on vertical stability control, equilibrium reconstruction, and MHD stability modeling directly addresses this need. I have worked closely with engineering teams at Commonwealth Fusion Systems and other private companies to ensure that the stability analysis methods we develop in the laboratory are directly applicable to the machines they are designing.

**The third thrust is developing the computational and data infrastructure to accelerate discovery.** Modern tokamak experiments generate enormous quantities of data, and the physics models needed to interpret that data are computationally expensive. Through the Integrated Research Infrastructure project at DIII-D and related data-science work, my group has built workflows that compress analysis timescales from hours to minutes and are beginning to make real-time physics-informed decision-making in the control room possible. We are also developing AI and machine learning tools that can find patterns in large experimental databases and help us extrapolate physics knowledge to new regimes.

![NT vs PT comparison](/blog-projects/assets/img/NTPT_cartoon.png)
*Negative (left) and positive (right) triangularity plasma cross-sections. The geometric difference is simple; the physics consequences are profound.*

These three thrusts are not independent. The same data infrastructure that accelerates ELM-free scenario development also enables faster stability analysis; the same physics understanding that underpins NT design also informs control algorithms. My goal is to build a research group that is fluent across all three — one that produces scientists who can move between fundamental plasma physics, applied engineering analysis, and computational methods development, because the problems at the frontier of fusion require all three simultaneously.

The next decade will, I believe, see the construction of the first burning plasma machines and the beginning of the pilot plant design era. I want my group to be central to that transition.

## Selected publications on this subject:

**[Robust Avoidance of Edge-Localized Modes alongside Pedestal Formation in the Negative Triangularity Tokamak Edge](https://doi.org/10.1103/PhysRevLett.131.195101)**<br />
**Nelson, A. O.**, Schmitz, L., Paz-Soldan, C., Thome, K. E., Cote, T. B., Leuthold, N., Scotti, F., Austin, M. E., Hyatt, A. & Osborne, T., _Physical Review Letters_ **131**, 195101 (2023).

**[Implications of vertical stability control on the SPARC tokamak](https://doi.org/10.1088/1741-4326/ad58f6)**<br />
**Nelson, A. O.**, Garnier, D. T., Battaglia, D. J., Paz-Soldan, C., Stewart, I., Reinke, M., Creely, A. J. & Wai, J., _Nuclear Fusion_ **64**, 086040 (2024).

**[Accelerating Discoveries at DIII-D With the Integrated Research Infrastructure](https://doi.org/10.3389/fphy.2024.1524041)**<br />
Bechtel Amara, T., Smith, S. P., Xing, Z. A., Neiser, T. F., **Nelson, A. O.** et al., _Frontiers of Physics_ **12**, 1524041 (2025).

**[Exploring the fusion power plant design space: comparative analysis of positive and negative triangularity tokamaks through optimization](http://arxiv.org/abs/2507.19668)**<br />
Slendebroek, T., **Nelson, A. O.**, Meneghini, O. et al., _Nuclear Fusion_ **66**, 026032 (2026).
