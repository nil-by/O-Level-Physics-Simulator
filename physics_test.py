import time

# Physics Variables
acceleration_gravity = 9.8  # m/s^2
initial_velocity = 20  # m/s (dropped at initial velocity 20 m/s)
time_elapsed = 0.0  # seconds
time_interval = 0.5  # calculate every 0.5s

print("--- STARTING GRAVITY SIMULATION ---")
# Calculate speed as an object drops for 4 seconds
while time_elapsed <= 4.0:
    # Formula: v = u + at
    current_velocity = initial_velocity + (
        acceleration_gravity * time_elapsed
    )

    print(f"Time: {time_elapsed:.1f}s | Speed: {current_velocity:.2f} m/s")

    time_elapsed += time_interval
    time.sleep(0.3)  