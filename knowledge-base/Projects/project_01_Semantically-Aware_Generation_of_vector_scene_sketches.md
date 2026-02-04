# Semantically-Aware Generation of Vector Scene Sketches

Category: Computer Vision / Multimodal Learning  
Level: MSc Dissertation  
Responsibility: End-to-end ownership (research, design, implementation, evaluation)  
Duration: MSc Final Project

---

## Problem Statement

Most image-to-sketch generation models focus on **foreground objects only** and struggle to represent **entire scenes** that include both foreground and background elements.  
Existing approaches such as CLIPaScene attempt scene-level sketching but suffer from **low accuracy and weak semantic understanding**, largely due to reliance on a CLIP visual encoder that is not specialised for sketches.

The core challenge was to improve **semantic understanding of sketches** while preserving **spatial relationships and scene context** in vector-based representations.

---

## Approach

This project proposes a modification to the CLIPaScene framework by **replacing the standard CLIP visual encoder with a specialised sketch encoder** designed for semantic sketch understanding.

The work combines ideas from two research directions:
- Scene-level vector sketch generation (CLIPaScene)
- Open-vocabulary semantic scene sketch understanding

### Key design choices:
- Retained CLIPaScene’s **differentiable vector rendering pipeline** using Bézier curves
- Replaced the CLIP visual encoder with a **ViT-based sketch encoder**
- Leveraged **value–value self-attention** to better capture semantic relationships in sparse sketches
- Preserved multi-level abstraction control (fidelity vs simplicity axes)

The modified encoder was evaluated using **sketch-based image retrieval (SBIR)** to measure semantic alignment between sketches and images.

---

## System Overview

High-level pipeline:
1. Input image is segmented into foreground and background
2. Initial vector strokes are generated using differentiable rendering
3. Sketches are encoded using a **specialised sketch encoder**
4. Semantic and geometric losses are computed
5. Stroke parameters are iteratively optimised
6. A matrix of sketches with varying abstraction levels is produced

This design allows the model to generate **editable, scalable vector scene sketches** while maintaining semantic coherence.

---

## Core Techniques & Tools

- Deep Learning with GPU compute
- Vision Transformers (ViT-B/16)
- CLIP-based multimodal representations
- Custom sketch encoder with modified attention mechanisms
- Differentiable rasterisation
- Sketch-based Image Retrieval (SBIR)
- Python, PyTorch

---

## Evidence of Skill

- Designed and implemented an end-to-end research-grade computer vision system
- Independently integrated and modified Transformer-based encoders
- Implemented Sketch-Based Image Retrieval (SBIR) **entirely from scratch** for evaluation
- Worked with multimodal representations (image–sketch–semantic space)
- Conducted empirical evaluation using retrieval-based metrics
- Analysed architectural incompatibilities and training instabilities
- Balanced abstraction, fidelity, and semantic accuracy in generative outputs


---

## Results & Findings

- The sketch encoder demonstrated **improved semantic alignment** compared to the standard CLIP visual encoder
- SBIR experiments showed better retrieval accuracy for complex scenes
- Attention maps revealed stronger focus on semantically relevant regions
- Identified key integration challenges such as:
  - Architectural mismatches
  - Loss balancing issues
  - Gradient stability problems

These findings establish a strong foundation for future work in scene-level sketch generation.

---

## Why This Project Matters

This project goes beyond a standard university assignment by:
- Addressing an **underexplored problem** in computer vision
- Combining and adapting **multiple research papers**
- Making architectural modifications rather than treating models as black boxes
- Demonstrating research maturity and system-level thinking

The work highlights the limitations of general-purpose vision encoders and shows how **domain-specific representations** can significantly improve performance in sketch-based systems.

---

## Future Directions

- Fully integrate the sketch encoder into the CLIPaScene training loop
- Explore improved loss formulations for stability
- Extend the system to interactive design and creative tools
- Investigate real-time sketch generation and editing

---

Reference:
- MSc Dissertation: *Semantically-Aware Generation of Vector Scene Sketches*, University of Surrey (2024) :contentReference[oaicite:0]{index=0}
