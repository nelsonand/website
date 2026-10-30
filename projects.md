---
layout: page
title: Research
kicker: Research
headline: Plasma-informed engineering of <em>fusion power plants</em>
subtitle: "Fusion engineering and plasma physics must be co-designed. The plasma sets the boundary conditions for the hardest engineering problems in a fusion plant, so choosing how to operate the plasma is itself one of the most powerful design decisions we can make."
---

<div class="figure">
  <img src="{{ '/blog-projects/assets/img/MANTA_cover.jpg' | relative_url }}" style="max-height:440px" alt="Exploded rendering of the MANTA fusion pilot plant">
  <div class="cap">Exploded view of MANTA, a negative triangularity fusion pilot plant designed by a multi-university student team I advised <a href="https://doi.org/10.1088/1361-6587/ad6708">[PPCF 2024]</a>.</div>
</div>

<div class="section" id="motivation">
  <div class="label"><div class="num">01</div><div class="t">Motivation</div></div>
  <div class="body">
    <h2>Fusion's remaining obstacles are engineering problems</h2>
    <p>Commercial fusion energy is among the most ambitious engineering challenges ever undertaken, and the field has entered a decisive decade. The National Academies call for a U.S. pilot plant producing net electricity in the 2035–2040 timeframe <a href="https://doi.org/10.17226/25991">[NASEM 2021]</a>, the Department of Energy has released a national <a href="https://www.energy.gov/node/4853442">Fusion Science &amp; Technology Roadmap</a>, and private companies are now designing, financing, and building real machines.</p>
    <p>As fusion moves from experiment to power plant, its most pressing obstacles have become increasingly interdisciplinary, with strong elements of mechanical engineering: removing extreme, transient heat loads from plasma-facing components, keeping structures intact over a long component lifetime, and optimizing plant designs that remain viable despite deep uncertainty in the underlying physics.</p>
    <p>These problems share one feature: <strong>their boundary conditions are set by the plasma</strong>. Engineering tools typically treat the plasma as a fixed, idealized heat source, while plasma physics models typically stop at the plasma's edge. My research lives at this interface.</p>
  </div>
</div>

<div class="section" id="foundation">
  <div class="label"><div class="num">02</div><div class="t">Foundation</div></div>
  <div class="body">
    <h2>Designing the plasma to make engineering possible</h2>
    <div class="thrust">
      <div>
        <p>My Ph.D. work at Princeton developed automated, integrated models of the tokamak edge <a href="https://doi.org/10.1016/j.nme.2020.100883">[NME 2021]</a>. At Columbia, I have helped lead the international effort on <strong>negative triangularity (NT)</strong>, a reversed plasma shape that robustly eliminates edge-localized modes, the instabilities responsible for repeated bursts of heat onto reactor walls <a href="https://doi.org/10.1103/PhysRevLett.131.195101">[PRL 2023]</a>, <a href="https://doi.org/10.1088/1361-6587/ad6a83">[PPCF 2024]</a>.</p>
        <p>The DIII-D NT team I was part of received the 2026 APS John Dawson Award for this work. I now lead the joint EU/US working group on NT, led the first NT experiments on MAST-U in the UK <a href="https://doi.org/10.1088/1741-4326/ad89db">[NF 2024]</a>, and supported early NT development on ASDEX Upgrade in Germany.</p>
      </div>
      <div class="thrust-img"><img src="{{ '/blog-projects/assets/img/NTPT_cartoon.jpg' | relative_url }}" alt="Negative and positive triangularity plasma cross-sections" style="background:#fff"><figcaption>Positive (left) and negative (right) triangularity plasma shapes.</figcaption></div>
    </div>
    <h3>From physics to power plant design</h3>
    <p>Much of my recent work translates these physics lessons into integrated plant designs:</p>
    <ul>
      <li><strong>Pilot plant concepts.</strong> I advised the student teams that designed the MANTA and CENTAUR pilot plants, which use NT to deliver 450 MW of fusion power with tolerable wall heat fluxes <a href="https://doi.org/10.1088/1361-6587/ad6708">[MANTA 2024]</a>, <a href="https://doi.org/10.1088/1361-6587/ae9eea">[CENTAUR 2026]</a>.</li>
      <li><strong>Industry design work.</strong> I developed vertical stability control requirements for Commonwealth Fusion Systems' SPARC tokamak <a href="https://doi.org/10.1088/1741-4326/ad58f6">[NF 2024]</a>, currently lead pulse design for their ARC power plant <a href="https://schedule.aps.org/dppgec/2026/events/DPP-RO03/6">[APS-DPP 2026]</a>, and lead power plant design for Maritime Fusion <a href="https://arxiv.org/abs/2605.04190">[arXiv 2026]</a>. I have also contributed to plant design at Tokamak Energy and Kyoto Fusioneering.</li>
      <li><strong>Data-driven methods.</strong> Throughout, I use machine learning and data-driven methods to bridge present-day experiments and future machines, from neural-network ELM forecasting <a href="https://doi.org/10.1088/2632-2153/adfb41">[MLST 2025]</a> to multimodal super-resolution diagnostics <a href="https://doi.org/10.1038/s41467-025-63492-1">[Nat. Commun. 2025]</a>.</li>
    </ul>
  </div>
</div>

<div class="section" id="thrust-1">
  <div class="label"><div class="num">03</div><div class="t">Thrust 1</div></div>
  <div class="body">
    <h2>Risk-informed design of fusion power plants</h2>
    <p>Fusion plant design is constrained as much by cost and reliability as by physics, which makes <strong>predictive design under deep physics uncertainty</strong> the central difficulty. In a study I co-led with General Atomics, we performed more than 200,000 integrated design evaluations with open-source software to compare conventional designs with NT <a href="https://doi.org/10.1088/1741-4326/ae27e6">[NF 2026]</a>. Both concepts delivered similar cost and performance, but a modest change in a few uncertain plasma constraints eliminated every viable conventional design while the NT designs remained robust. Plant design must be risk-informed.</p>
    <div class="aims">
      <div class="aim"><div class="n">Aim 1.1</div><h3>Uncertainty-aware, multi-fidelity optimization</h3><p>Embed calibrated physics uncertainties <a href="https://doi.org/10.1088/1361-6587/aeb570">[PPCF 2026]</a> into integrated plant optimization using robust and reliability-based methods and ML surrogates. Produce design targets with confidence bands, and use value-of-information analysis to choose the experiments that retire the most design risk.</p></div>
      <div class="aim"><div class="n">Aim 1.2</div><h3>Mission-driven and AI-assisted design</h3><p>Formalize requirements-driven design for different fusion missions, from grid-scale plants to process heat and marine power, where mass, footprint, and materials lifetime may replace cost as the objective. Explore agentic AI for design-space exploration <a href="https://arxiv.org/abs/2610.00492">[arXiv 2026]</a>.</p></div>
      <div class="aim"><div class="n">Aim 1.3</div><h3>Design for maintainability and evolution</h3><p>First-of-a-kind plants may run for decades while physics and technology evolve. Apply design-for-changeability and real-options methods to quantify the value of replaceable components, upgradeable subsystems, and adaptable divertors and heating systems.</p></div>
    </div>
  </div>
</div>

<div class="section" id="thrust-2">
  <div class="label"><div class="num">04</div><div class="t">Thrust 2</div></div>
  <div class="body">
    <h2>Designing for power exhaust, from plasma to coolant</h2>
    <div class="thrust">
      <div>
        <p>Power exhaust is <a href="https://www.osti.gov/servlets/purl/1995209">widely recognized</a> as a critical gap on the path to fusion energy. Tokamak divertors must handle steady heat fluxes comparable to a rocket nozzle throat (~10 MW/m²), deposited on a strip a few millimeters wide and sustained for years, along with transient events that can exceed melting limits.</p>
        <p>Yet heat removal systems are usually designed against static, idealized heat loads. <strong>Predictive thermal-fluid models are only as reliable as their plasma boundary conditions</strong>, and predicting that boundary condition is the core of my plasma expertise.</p>
      </div>
      <div class="thrust-img"><img src="{{ '/blog-projects/assets/img/vvuq_pedestal_limits.png' | relative_url }}" alt="Pedestal stability limits with uncertainty bands" style="background:#fff"><figcaption>Calibrated uncertainty in edge plasma predictions feeds directly into heat-load boundary conditions.</figcaption></div>
    </div>
    <div class="aims">
      <div class="aim"><div class="n">Aim 2.1</div><h3>Uncertainty-quantified heat-load boundary conditions</h3><p>ML-accelerated pipelines that map plasma scenarios to probabilistic, time-resolved heat-flux maps on plasma-facing surfaces, validated against existing tokamaks and released as open-source tools that thermal engineers can couple to conjugate heat transfer and structural analysis.</p></div>
      <div class="aim"><div class="n">Aim 2.2</div><h3>Thermally constrained plasma pulse design</h3><p>Embed reduced thermal-hydraulic models of plasma-facing components directly in scenario design, so that surface temperature, coolant margin to critical heat flux, and accumulated fatigue act as real-time constraints on how a plasma is ramped, sustained, and terminated.</p></div>
      <div class="aim"><div class="n">Aim 2.3</div><h3>Thermal dynamics of pulsed fusion plants</h3><p>Model the full chain from plasma pulse to first wall, blanket, coolant, and power cycle to characterize thermal transients and fatigue, size thermal energy storage, and set cycle-fatigue limits for future plants.</p></div>
    </div>
  </div>
</div>

<div class="section" id="approach">
  <div class="label"><div class="num">05</div><div class="t">Approach</div></div>
  <div class="body">
    <h2>Funding, partners, and open tools</h2>
    <p>This work is computational, built on high-quality data from tokamak user facilities around the world, and supported by a mix of DOE Fusion Energy Sciences programs and industry contracts with private fusion companies (details on my <a href="{{ '/cv/#funding' | relative_url }}">About page</a>). Each aim is scoped to be the foundation of a student-led thesis, with internships and collaborations at national laboratories and fusion companies.</p>
    <p>I am grateful to work with collaborators across private industry (General Atomics, Commonwealth Fusion Systems, Tokamak Energy, Next Step Fusion, Kyoto Fusioneering, Maritime Fusion) and public research institutions (Princeton Plasma Physics Laboratory, Princeton University, MIT, UKAEA, and the Max Planck Institute for Plasma Physics).</p>
    <p>Wherever possible, we develop and release tools openly. See <a href="{{ '/software/' | relative_url }}">Software &amp; Tools</a>.</p>
  </div>
</div>

<div class="section" id="projects">
  <div class="label"><div class="num">06</div><div class="t">Projects</div></div>
  <div class="body">
    <h2>Project write-ups</h2>
    <p>Longer, plain-language descriptions of individual projects:</p>
    {% include post-list.html category="projects" %}
  </div>
</div>
