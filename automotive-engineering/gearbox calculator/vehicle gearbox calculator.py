import math
print("Vehicle Gearbox Calculator")

motor_torque= float(input("Enter the motor torque (Nm): "))
motor_rpm= float(input("Enter the motor RPM: "))
gear_ratio= float(input("Enter the gear ratio: "))
efficiency= float(input("Enter the efficiency (as a decimal): "))
wheel_radius= float(input("Enter the wheel radius (m): "))

efficiency = efficiency / 100
wheel_torque = motor_torque * gear_ratio * efficiency
wheel_rpm = motor_rpm / gear_ratio
tractive_force = wheel_torque / wheel_radius
angular_velocity = (wheel_rpm * 2 * math.pi) / 60
input_power = motor_torque * angular_velocity
output_power = input_power * efficiency

print("Results:")
print(f"Wheel Torque: {wheel_torque:.2f} Nm")
print(f"Wheel speed: {wheel_rpm:.2f} RPM")
print(f"Tractive Force: {tractive_force:.2f} N")
print(f"Input Power: {input_power/1000:.2f} kW")
print(f"Output Power: {output_power/1000:.2f} kW")