# My O-Level Physics Project Journal

## Day 1: May 29, 2026
* **Goal:** Set up the coding workshop environment and verify Python execution.
* **What I Did:** Installed GitHub Desktop, created a public repository, opened it in VS Code, and ran a basic terminal script for the formula v = u + at.
* **Problems Faced:** Felt overwhelmed by the setup process, but successfully linked the desktop client to the cloud repository.
* **Next Step:** Learn how to draw a window on the screen using Pygame to move an actual visual object.

## Day 2: May 31, 2026
* **Goal:** Turn text-based calculations into a moving visual simulation.
* **What I Did:** Installed Pygame, opened a graphics window, drew a blue ball using coordinates, and wrote two lines of logic (`ball_y += ball_velocity_y` and `ball_velocity_y += 0.1`) to simulate constant acceleration due to gravity.
* **Struggles:** Felt frustrated at the start looking at complex Pygame setup syntax, but it clicked once I realized the screen is just an X-Y math grid.
* **Next Step:** The ball currently falls forever off the screen. Next session, I want to add a solid floor using O-Level boundaries so the ball bounces back up!
* **Breakthrough Concept:** Realized that in a computer loop, the 't' in v = u + at is hidden. Because the loop updates frame-by-frame, delta_t equals 1, making it mathematically invisible in the line 
## Day 2 (Update): May 31, 2026
* **The Realization:** Challenged the hidden time variable logic. Realized that treating a loop as a whole unit of 1 creates fake physics locked to monitor speeds.
* **The Upgrade:** Introduced an explicit time step variable (`dt = 0.016`) representing 1/60th of a second, and real Earth gravity (`gravity = 9.8`). 
* **The Logic Click:** Rewrote the engine room using true O-Level mechanics (`ball_y += ball_velocity_y * dt` and `ball_velocity_y += gravity * dt`). 60 loops now perfectly equal 1 real-world second. It felt messy and overwhelming at first, but the math fully checks out.
