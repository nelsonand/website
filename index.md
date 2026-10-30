---
layout: home
title: Oak Nelson
share-description: "Oak Nelson works on plasma-informed engineering of fusion power plants at Columbia University."
---

<div class="hero">
  <div class="wrap">
    <div>
      <div class="eyebrow">Fusion energy · Plasma physics · Engineering design</div>
      <h1>Co-designing the plasma <em>and</em> the machine.</h1>
      <p>I'm Oak Nelson, a research scientist at Columbia University. I study how the way we operate a fusion plasma shapes the heat loads, structural limits, and design of future fusion power plants, and I build tools that help physicists and engineers make those decisions together.</p>
      <div class="cta">
        <a class="p" href="{{ '/projects/' | relative_url }}">Read about my research</a>
        <a class="s" href="{{ '/cv/' | relative_url }}">About me</a>
      </div>
    </div>
    <div class="art"><img src="{{ '/blog-projects/assets/img/diii-d_cut.webp' | relative_url }}" alt="Cutaway rendering of a negative triangularity plasma inside the DIII-D tokamak"></div>
  </div>
</div>

<div class="home">

<section>
  <div class="wrap">
    <div class="sh">
      <div><div class="kicker">Research</div><h2>Plasma-informed engineering of fusion power plants</h2></div>
      <a href="{{ '/projects/' | relative_url }}">Research overview →</a>
    </div>
    <p class="thesis">Engineering tools often treat the plasma as a fixed heat source, and plasma models usually stop at the plasma's edge. My work sits at that interface, where <b>the plasma operating regime becomes an engineering design variable</b>.</p>
    <div class="grid3">
      <a class="tc" href="{{ '/projects/#foundation' | relative_url }}">
        <div class="im" style="background-image:url('{{ '/blog-projects/assets/img/d3d_nt.jpeg' | relative_url }}')"></div>
        <div class="b"><div class="n">Foundation</div><h3>Designing the plasma to make engineering possible</h3><p>Negative triangularity, a reversed plasma shape that avoids the edge instabilities that send bursts of heat onto reactor walls.</p></div>
      </a>
      <a class="tc" href="{{ '/projects/#thrust-1' | relative_url }}">
        <div class="im" style="background-image:url('{{ '/blog-projects/assets/img/MANTA_cover.jpg' | relative_url }}')"></div>
        <div class="b"><div class="n">Thrust 1</div><h3>Risk-informed design of fusion power plants</h3><p>Design optimization that accounts for physics uncertainty, mission-specific requirements, and how plants will change over decades of operation.</p></div>
      </a>
      <a class="tc" href="{{ '/projects/#thrust-2' | relative_url }}">
        <div class="im" style="background-image:url('{{ '/blog-projects/assets/img/vvuq_pedestal_limits.png' | relative_url }}');background-color:#fff;background-size:contain"></div>
        <div class="b"><div class="n">Thrust 2</div><h3>Designing for power exhaust, from plasma to coolant</h3><p>Probabilistic heat-load boundary conditions, and plasma pulses designed around the thermal limits of the machine.</p></div>
      </a>
    </div>
  </div>
</section>

<section>
  <div class="wrap split">
    <div class="pubs">
      <div class="sh"><h2>Selected work</h2><a href="{{ '/publications/' | relative_url }}">Publications →</a></div>
      <div class="p"><div class="j">Nuclear Fusion · 2026</div><a class="t" href="https://doi.org/10.1088/1741-4326/ae27e6">Exploring the fusion power plant design space: comparative analysis of positive and negative triangularity tokamaks through optimization</a><div class="a">T. Slendebroek, <b>A. O. Nelson</b>, O. M. Meneghini, et al.</div></div>
      <div class="p"><div class="j">Plasma Physics and Controlled Fusion · 2024</div><a class="t" href="https://doi.org/10.1088/1361-6587/ad6708">MANTA: a negative-triangularity NASEM-compliant fusion pilot plant</a><div class="a">The MANTA Collaboration (student design team)</div></div>
      <div class="p"><div class="j">Physical Review Letters · 2023</div><a class="t" href="https://doi.org/10.1103/PhysRevLett.131.195101">Robust avoidance of edge-localized modes alongside gradient formation in the negative triangularity tokamak edge</a><div class="a"><b>A. O. Nelson</b>, L. Schmitz, C. Paz-Soldan, et al.</div></div>
    </div>
    <div class="news">
      <div class="sh"><h2>Recent</h2></div>
      {%- for item in site.data.news limit: 6 -%}
      <div class="n"><span class="d">{{ item.date }}</span><span>{% if item.url %}<a href="{{ item.url | relative_url }}">{{ item.text }}</a>{% else %}{{ item.text }}{% endif %}</span></div>
      {%- endfor -%}
    </div>
  </div>
</section>

<div class="band">
  <div class="wrap">
    <a href="{{ '/teaching/' | relative_url }}">
      <img src="{{ '/blog-projects/assets/img/MANTA_cover.jpg' | relative_url }}" alt="">
      <h3>Teaching</h3>
      <p>Project-based design courses where students integrate physics, thermal, structural, and cost constraints into a single fusion plant design.</p>
    </a>
    <a href="{{ '/students/' | relative_url }}">
      <img src="{{ '/blog-outreach/assets/img/StudentDay2022.jpg' | relative_url }}" alt="">
      <h3>Group &amp; mentoring</h3>
      <p>The Ph.D., master's, and undergraduate students I have had the privilege to advise, and what they have gone on to do.</p>
    </a>
    <a href="{{ '/outreach/' | relative_url }}">
      <img src="{{ '/blog-outreach/assets/img/plasma_outreach_CU.jpg' | relative_url }}" alt="">
      <h3>Service &amp; community</h3>
      <p>Building community for students and early-career scientists, and sharing fusion with the public.</p>
    </a>
  </div>
</div>

</div>
