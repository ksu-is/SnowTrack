
# SnowTrack Project Roadmap

## Project Overview

SnowTrack is a Python application designed to organize photographs from remote cameras in Alaska, record snow depth measurements, and track snow accumulation over time.

The project will be developed individually for IS 3020 Application Development I.

## Sprint 1 - Project Setup and Research
Due: November 18, 2026

- [x] Complete Exercise 6 project proposal.
- [x] Enter SnowTrack in the Teams Projects spreadsheet.
- [x] Join the KSU-IS GitHub organization.
- [x] Create the SnowTrack GitHub team.
- [x] Create the SnowTrack repository.
- [x] Connect the team to the repository.
- [x] Update and commit README.md.
- [x] Research an existing Python image-viewing program.
- [x] Read and attempt to run the example code.
- [x] Document code evaluation findings.
- [ ] Complete Sprint 1 Review and Log.

## Existing Python Code Evaluation

### Code Evaluated

Tkinter image viewer using the Pillow library.

Source:
https://pillowpython.com/guides/show-image/

Example file: tk_viewer.py

### Purpose

Evaluate existing Python code that opens and displays photographs in a graphical window. This functionality could be used in SnowTrack to display images collected from remote snow-monitoring cameras.

### Evaluation Tasks

- [x] Locate an existing Python image-viewing example.
- [x] Read and review the source code.
- [x] Attempt to run the program in Visual Studio Code.
- [x] Identify useful functions for SnowTrack.
- [x] Record results and problems encountered.

### Evaluation Results

I reviewed an existing Python example that uses Tkinter and Pillow to display a photograph.

The program uses Image.open() to load a photograph, thumbnail() to resize it, and ImageTk.PhotoImage() to display it in a Tkinter window.

My first attempt to run the program produced a ModuleNotFoundError because the Pillow library was not installed.

I installed Pillow 13.0.0 using pip and ran the program again.

The second attempt was successful. A Tkinter window opened and displayed a photograph from a snow-monitoring camera showing two different types of staff gauges.

This example could be useful for developing SnowTrack's image-viewing functionality. However, it currently displays only one photograph and does not provide controls for browsing images or recording measurements.

I plan to use this example as a starting point and expand its functionality during Sprint 2.

## Sprint 2 - Application Development
Due: November 30, 2026

- [ ] Create the main Python application.
- [ ] Develop a graphical interface using Tkinter.
- [ ] Add the ability to select and open image files.
- [ ] Display photographs in the application.
- [ ] Add manual snow depth measurement entry.
- [ ] Save measurements to a CSV file.
- [ ] Make at least six significant code commits.
- [ ] Update the roadmap as development progresses.
- [ ] Complete Sprint 2 Review and Log.

## Sprint 3 - Testing and Improvements
Due: December 4, 2026

- [ ] Test the application using sample photographs.
- [ ] Add graphs showing snow depth changes over time.
- [ ] Improve the interface and error handling.
- [ ] Explore automatic gauge recognition using OpenCV.
- [ ] Continue committing code improvements.
- [ ] Create the project PowerPoint slide.
- [ ] Upload the slide to D2L and GitHub.

## Final Presentation
Due: December 14, 2026

- [ ] Prepare a demonstration of SnowTrack.
- [ ] Explain the Python tools and libraries used.
- [ ] Demonstrate completed application features.
- [ ] Present the project using Microsoft Teams.

## Project Status

Sprint 1 setup and research are complete.

The SnowTrack GitHub team and repository have been created within the KSU-IS organization. The README.md has been updated and committed, and an existing Tkinter/Pillow image-viewing example has been reviewed and successfully tested using a snow-monitoring photograph.

The next step is to commit these evaluation findings to GitHub and complete the Sprint 1 Review and Log in D2L.
