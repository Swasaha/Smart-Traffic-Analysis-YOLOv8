from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import random  # Replace with actual data logic

# Data storage for each metric
traffic_counts = []
accuracy_data = []
loss_data = []
validation_data = []

# Traffic Flow Plot
def update_traffic(frame):
    traffic_count = random.randint(0, 100)  # Simulated data (replace with real YOLO data)
    traffic_counts.append(traffic_count)
    if len(traffic_counts) > 20:
        traffic_counts.pop(0)

    plt.cla()  # Clear the plot
    plt.plot(traffic_counts, label='Real-Time Traffic', marker='o', color='green')
    plt.xlabel('Time (s)')
    plt.ylabel('Vehicles Detected')
    plt.title('Traffic Flow')
    plt.legend()
    plt.tight_layout()

# Accuracy Plot
def update_accuracy(frame):
    accuracy = random.uniform(0.7, 1.0)  # Simulated data (replace with real model data)
    accuracy_data.append(accuracy)
    if len(accuracy_data) > 20:
        accuracy_data.pop(0)

    plt.cla()  # Clear the plot
    plt.plot(accuracy_data, label='Model Accuracy', marker='o', color='orange')
    plt.xlabel('Time (s)')
    plt.ylabel('Accuracy')
    plt.title('Accuracy Over Time')
    plt.legend()
    plt.tight_layout()

# Loss Plot
def update_loss(frame):
    loss = random.uniform(0.1, 0.5)  # Simulated data (replace with real model data)
    loss_data.append(loss)
    if len(loss_data) > 20:
        loss_data.pop(0)

    plt.cla()  # Clear the plot
    plt.plot(loss_data, label='Model Loss', marker='o', color='red')
    plt.xlabel('Time (s)')
    plt.ylabel('Loss')
    plt.title('Loss Over Time')
    plt.legend()
    plt.tight_layout()

# Validation Plot
def update_validation(frame):
    validation_score = random.uniform(0.65, 0.95)  # Simulated data (replace with real model data)
    validation_data.append(validation_score)
    if len(validation_data) > 20:
        validation_data.pop(0)

    plt.cla()  # Clear the plot
    plt.plot(validation_data, label='Validation Score', marker='o', color='purple')
    plt.xlabel('Time (s)')
    plt.ylabel('Score')
    plt.title('Validation Score Over Time')
    plt.legend()
    plt.tight_layout()

# Create separate figures for each graph
fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()
fig3, ax3 = plt.subplots()
fig4, ax4 = plt.subplots()

# Link update functions to animations
ani1 = FuncAnimation(fig1, update_traffic, interval=1000)
ani2 = FuncAnimation(fig2, update_accuracy, interval=1000)
ani3 = FuncAnimation(fig3, update_loss, interval=1000)
ani4 = FuncAnimation(fig4, update_validation, interval=1000)

# Show all figures
plt.show()
