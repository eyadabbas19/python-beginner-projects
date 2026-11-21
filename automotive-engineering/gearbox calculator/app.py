import streamlit as st
import math

st.set_page_config(
    page_title="V1 Engineering",
    page_icon="🏎️",
    layout="wide"
)

st.title("V1 Engineering")
st.subheader("Vehicle Gearbox Performance Calculator")

st.write("Calculate the mechanical performance of a vehicle gearbox.")

st.divider()

st.header("Motor Parameters")

col1, col2 = st.columns(2)

with col1:
    motor_torque = st.number_input(
        "Motor Torque (Nm)", min_value=0.0, value=250.0
    )

    motor_rpm = st.number_input(
        "Motor RPM", min_value=0.0, value=8000.0
    )

    gear_ratio = st.number_input(
        "Gearbox Ratio", min_value=0.01, value=8.0
    )

with col2:
    efficiency = st.number_input(
        "Efficiency (%)", min_value=0.0,
        max_value=100.0, value=90.0
    )

    wheel_radius = st.number_input(
        "Wheel Radius (m)", min_value=0.01, value=0.33
    )

if st.button("Calculate Performance"):

    efficiency_decimal = efficiency / 100

    wheel_torque = motor_torque * gear_ratio * efficiency_decimal
    wheel_rpm = motor_rpm / gear_ratio

    tractive_force = wheel_torque / wheel_radius

    angular_velocity = motor_rpm * (2 * math.pi / 60)

    input_power = motor_torque * angular_velocity
    output_power = input_power * efficiency_decimal

    st.divider()
    st.header("Performance Results")

    c1, c2, c3 = st.columns(3)

    c1.metric("Wheel Torque", f"{wheel_torque:.2f} Nm")
    c2.metric("Wheel Speed", f"{wheel_rpm:.2f} RPM")
    c3.metric("Tractive Force", f"{tractive_force:.2f} N")

    c4, c5 = st.columns(2)

    c4.metric("Input Power", f"{input_power / 1000:.2f} kW")
    c5.metric("Output Power", f"{output_power / 1000:.2f} kW")