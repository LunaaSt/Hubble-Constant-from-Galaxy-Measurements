# Hubble-Constant-from-Galaxy-Measurements

**Analyzing 60 galaxies from Stellarium data with the aim of obtaining the Hubble constant and the age of the universe using computational methods in Python.**

This project includes Python code to:
- Save all the galaxy data into a `.txt` file.
- Generate a LaTeX-formatted table for easy copy-paste into documents.

## Project Structure

The analysis is divided into two main parts:

### 1. Hubble Constant and Age of the Universe
Using the redshift (`z`) and distances (`d`) of 60 galaxies, this section:
- Estimates the **Hubble constant** \( H_0 \)
- Computes the **age of the universe** using linear regression and Hubble's law.

### 2. Absolute Magnitude and Luminosity
Using the apparent magnitude (`m`) and distances of the same 60 galaxies, this section:
- Calculates the **absolute magnitude** \( M \)
- Computes the **luminosity** \( L \) of each galaxy relative to a reference luminosity.

## Output
- A `.txt` file containing the structured galaxy data.
- A complete LaTeX table with all relevant parameters.

## Requirements
- Python 3.x
- `pandas`, `numpy`, `matplotlib` (for analysis and plots)

