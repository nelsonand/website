---
layout: page
title: Software & Tools
kicker: Research · Software
headline: Open tools for <em>fusion design</em>
subtitle: "Design studies are only as useful as they are reproducible. Wherever possible, my group builds on, contributes to, and releases open-source software so that other physicists, engineers, and students can use and check our work."
---

<div class="section" id="design">
  <div class="label"><div class="num">01</div><div class="t">Design</div></div>
  <div class="body">
    <h2>Equilibrium, coil, and plant design</h2>
    <div class="aims two">
      <div class="aim">
        <div class="n">Developer</div>
        <h3><a href="https://openfusiontoolkit.github.io/OpenFUSIONToolkit/">Open FUSION Toolkit / TokaMaker</a></h3>
        <p>A finite-element suite for plasma and fusion modeling, including the TokaMaker free-boundary equilibrium code. I contribute to development, and my students have used it for coil optimization <a href="https://doi.org/10.1063/5.0332786">[AIP Adv. 2026]</a>, analysis workflows, and porting the FEEQS code.</p>
        <div class="meta">2022–present · <a href="https://github.com/OpenFUSIONToolkit/OpenFUSIONToolkit">GitHub</a></div>
      </div>
      <div class="aim">
        <div class="n">User &amp; collaborator</div>
        <h3><a href="https://github.com/ProjectTorreyPines/FUSE.jl">FUSE</a></h3>
        <p>General Atomics' open-source integrated fusion plant design framework. With GA, we used FUSE for more than 200,000 integrated design evaluations comparing positive and negative triangularity plants <a href="https://doi.org/10.1088/1741-4326/ae27e6">[NF 2026]</a>.</p>
        <div class="meta">2024–present</div>
      </div>
      <div class="aim">
        <div class="n">Contributor</div>
        <h3><a href="https://github.com/cfs-energy/cfspopcon">cfspopcon</a></h3>
        <p>Commonwealth Fusion Systems' open-source plasma operating contour (POPCON) code. Undergraduate students in my group developed new physics modules, and a related project built a stellarator POPCON code.</p>
        <div class="meta">2024–present</div>
      </div>
      <div class="aim">
        <div class="n">Course tool</div>
        <h3>Open-source tools in the classroom</h3>
        <p>FUSE and TokaMaker are the backbone of the design projects in the <a href="{{ '/teaching/#courses' | relative_url }}">Fusion Energy Engineering</a> course I plan to teach, so that no student is limited by software licenses.</p>
      </div>
    </div>
  </div>
</div>

<div class="section" id="data">
  <div class="label"><div class="num">02</div><div class="t">Data</div></div>
  <div class="body">
    <h2>Data and analysis workflows</h2>
    <div class="aims two">
      <div class="aim">
        <div class="n">Developer</div>
        <h3>Automated kinetic equilibria on HPC</h3>
        <p>Automated kinetic equilibrium reconstruction and analysis pipelines running at NERSC <a href="https://doi.org/10.1016/j.fusengdes.2020.112163">[FED 2021]</a>, which grew into DIII-D's Integrated Research Infrastructure work to bring between-shot analysis from hours to minutes <a href="https://doi.org/10.3389/fphy.2024.1524041">[Frontiers 2025]</a>.</p>
      </div>
      <div class="aim">
        <div class="n">Co-developer</div>
        <h3>Machine learning for fusion data</h3>
        <p>Neural-network ELM forecasting with Argonne National Laboratory <a href="https://doi.org/10.1088/2632-2153/adfb41">[MLST 2025]</a>, multimodal super-resolution diagnostics <a href="https://doi.org/10.1038/s41467-025-63492-1">[Nat. Commun. 2025]</a>, and calibrated uncertainty for pedestal predictions <a href="{{ '/2026-10-16-vvuq/' | relative_url }}">(VVUQ post)</a>.</p>
      </div>
    </div>
  </div>
</div>

<div class="section" id="other">
  <div class="label"><div class="num">03</div><div class="t">Other</div></div>
  <div class="body">
    <h2>Other projects</h2>
    <ul class="dated">
      <li><span class="y">2023</span><span><a href="https://github.com/nelsonand/GARDN-M">GARDN-M</a>: a model for assessing and mitigating the carbon footprint of conference locations (<a href="{{ '/2023-03-02-gardnm/' | relative_url }}">post</a>)</span></li>
      <li><span class="y">2022–present</span><span>Open-source online tools for fusion energy pedagogy, including work with Next Step Fusion on <a href="https://fusiontwin.io/">web-based fusion simulation</a> (presented at the 2026 PlasmaNET Workshop)</span></li>
    </ul>
    <p style="margin-top:20px">More on <a href="https://github.com/{{ site.social-network-links.github }}">GitHub</a>.</p>
  </div>
</div>
