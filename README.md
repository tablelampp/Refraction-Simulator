# Refraction Simulator

**Created by:** Yonas Asmelash  
**Date:** 11/28/2022  

## Description

This Python-based **Refraction Simulator** uses the `turtle` graphics library to visually demonstrate the physics of **light refraction and reflection** at the boundary between two mediums with different refractive indices.

Users can input:
- The color of the light ray  
- The indices of refraction for both mediums (`n1` and `n2`)  
- The angle of incidence (in degrees)

The program then:
- Draws the boundary between the two media  
- Illustrates the **incident ray**, **reflected ray**, and (if applicable) the **refracted ray**  
- Uses **Snell’s Law** to compute the angle of refraction  
- Handles **total internal reflection** cases when applicable

## Screenshots


## Requirements

- Python 3.x
- No external libraries needed (uses built-in `turtle` and `math`)

## How to Run

1. Ensure Python is installed.
2. Run the script using any Python IDE or terminal:
   ```bash
   python refraction_simulator.py
