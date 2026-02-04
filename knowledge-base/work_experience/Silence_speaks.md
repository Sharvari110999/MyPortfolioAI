# Professional Experience: Silence Speaks

Role: AI Engineer  
Duration: 9 months  
Team Size: 2–3 engineers  
Domain: Accessibility Technology, Computer Vision, Sign Language Avatars

---

## Context

Silence Speaks builds AI-driven systems to improve accessibility for the Deaf community through **sign-language–based avatar technology**. The core objective is to make communication and media consumption more inclusive by converting spoken or written content into sign language using animated avatars.

The work involved both **research-oriented exploration** and **productionisation**, with a focus on delivering systems that internal stakeholders could use without relying on complex command-line interfaces.

---

## Scope of Responsibility

I worked with **end-to-end ownership across the AI pipeline**, contributing from data processing and model adaptation through to deployment and infrastructure orchestration.

My responsibilities covered both **machine learning system design** and **engineering for production environments**.

---

## Core Technical Work

### End-to-End AI Pipeline
- Designed and maintained end-to-end pipelines for processing video-based sign language data
- Converted raw video inputs into structured JSON representations
- Built pre-processing and post-processing pipelines to support downstream model inference

### Computer Vision & Representation Learning
- Worked on pose and keypoint extraction using:
  - OpenPose
  - DWPose
  - MediaPipe
- Implemented **bone length normalisation** to ensure consistency across different signers and recordings
- Handled interpolation techniques to stitch and align motion sequences from multiple videos

### Model Adaptation & Experimentation
- Fine-tuned existing models rather than training from scratch
- Ran systematic **model version experimentation**
- Evaluated different configurations for quality, stability, and performance
- Worked with **real user data**, including noisy and imperfect inputs

### Inference & Performance Optimisation
- Optimised inference pipelines for latency and reliability
- Balanced quality vs performance constraints for practical usage
- Designed systems with real-time or near-real-time considerations

---

## System Deployment & Infrastructure

- Containerised services using **Docker**
- Orchestrated workloads using **Kubernetes**
- Deployed services on **Google Cloud Platform (GCP)** using:
  - GKE (Google Kubernetes Engine)
  - Cloud compute and storage
- Exposed inference pipelines through **FastAPI endpoints**
- Enabled internal stakeholders to use AI systems via production-style APIs rather than CLI tools

---

## Tools & Technologies

- Python
- PyTorch
- Stable Video Diffusion
- Pose estimation frameworks (OpenPose, DWPose, MediaPipe)
- FastAPI
- Docker & Kubernetes
- Google Cloud Platform (GCP, GKE, compute, storage)

Related repositories (public-facing components):
- Video preprocessing pipeline
- Pose estimation pipeline
- Stable video diffusion inference
- Video rendering application
- Video postprocessing pipeline

---

## Real-World Impact

The systems supported use cases such as:
- Converting spoken or written content into sign language
- Enabling media (e.g. movies) to be accompanied by sign-language avatars, similar to subtitles but in visual form
- Maintaining character consistency through avatar-based rendering

This work directly involved interaction with **sign language users**, grounding technical decisions in real accessibility needs.

---

## Constraints & Challenges

- Tight delivery timelines
- Noisy, real-world video data
- Evolving requirements during the transition from research to internal production
- Balancing research experimentation with engineering reliability
- Deploying and maintaining AI systems in cloud environments

---

## Key Learnings

This experience reinforced skills that go beyond university projects:

- Building **production-oriented AI pipelines**
- Shipping under tight deadlines
- Making trade-offs between research quality and system reliability
- Working with real users and real constraints
- Thinking in terms of systems, not just models

---

## What This Experience Demonstrates

- Strong **industry-ready AI engineering skills**
- Deep experience in **computer vision pipelines**
- Comfort working across research and production boundaries
- Ability to deploy and maintain AI systems in cloud environments
- Practical understanding of accessibility-focused AI applications
