import streamlit as st
from PIL import Image
import math
import os
import subprocess
if "page" not in st.session_state:
    st.session_state.page = "main"

def go_to(page_name):
    st.session_state.page = page_name

def intro_amplifier():
    st.title("🔊 Introduction to Amplifiers")
    st.markdown("---")
    st.subheader("📘 What is an Amplifier?")
    st.markdown("""
    An **amplifier** is an electronic device that increases the power, voltage, or current of a signal. 
    It plays a fundamental role in audio systems, communication devices, and many other electronic systems.
    """)

    st.subheader("🎯 Purpose of Amplifiers")
    st.markdown("""
    - Boost weak input signals.
    - Improve the quality of transmission in communication systems.
    - Drive loads like speakers or antennas.
    """)

    st.subheader("🧠 Basic Working Principle")
    st.markdown("""
    Amplifiers operate using active components such as **transistors** or **operational amplifiers (Op-Amps)**. 
    A small input signal is applied at the input terminal, and the amplifier outputs a much stronger signal,
    without altering the original shape (ideally).
    """)

    st.subheader("🔧 Common Types of Amplifiers")
    st.markdown("""
    - **Voltage Amplifiers**: Increase voltage level.
    - **Current Amplifiers**: Increase current level.
    - **Power Amplifiers**: Increase both current and voltage to boost power.

    Each type is designed for a specific purpose and has unique characteristics.
    """)

    st.info("In upcoming sections, we’ll dive deeper into the types, classes, and real-world applications of amplifiers.")
    st.button("🔙 Back" ,on_click=lambda:go_to("main"))





def amplifier_importance():
    st.title("⚡ Amplifier Importance")
    st.markdown("---")

    st.subheader("🔍 What is an Amplifier?")
    st.markdown("""
    An **amplifier** is an electronic circuit that increases the amplitude of a signal 
    (voltage, current, or power) **without altering its original content**.
    """)

    st.subheader("📈 Signal Amplification")
    st.markdown("""
    - **Amplifying Weak Signals**: Boosts weak electrical signals to usable levels.
    - **Essential in Audio Systems**: Amplifies signals from microphones or media players.
    """)

    st.subheader("🎧 Improving Signal Quality")
    st.markdown("""
    - Reduces **noise and distortion**.
    - Enhances signal **clarity**.
    - Critical in wireless communication to **minimize interference**.
    """)

    st.subheader("🌐 Enabling Diverse Applications")
    st.markdown("""
    Amplifiers are key components in:
    - 🎵 **Audio and video systems**
    - 📡 **Wireless communications**
    - 🏥 **Medical devices**
    - 🏭 **Industrial systems**
    - 📱 **Consumer electronics**
    """)

    st.subheader("🛠️ Signal Control")
    st.markdown("""
    Amplifiers play a role in **sensor devices** by amplifying signals from sensors so they 
    can be read and analyzed accurately.
    """)

    st.subheader("⚙️ Enhancing System Efficiency")
    st.markdown("""
    Amplification helps improve the **efficiency and performance** of electronic systems.
    """)

    st.subheader("🔁 Amplifier's Role in Signal Processing")
    st.markdown("""
    - **Before Processing**: Amplifies weak input signals.
    - **After Processing**: Amplifies output signals to drive components (e.g., speakers or motors).
    - **In Analog Circuits**: Used in filtering, modulation, detection, and signal comparison.
    """)

    st.subheader("🧩 Basic Amplifier Components")
    st.markdown("""
    - Transistors (**BJTs** or **FETs**)  
    - Resistors  
    - Capacitors  
    - **Power supply**  
    - Inductors (used in RF amplifiers)  
    - **Bias resistors**, **coupling capacitors**, and **bypass capacitors**
    """)
    st.info("In upcoming sections, we’ll dive deeper into the types, classes, and real-world applications of amplifiers.")
    st.button("🔙 Back" ,on_click=lambda:go_to("main"))



def amplifier_types():
    st.title("📚 Types of Amplifiers")
    st.markdown("---")

    st.subheader("🔊 Audio Amplifiers")
    st.markdown("""
    Audio amplifiers are designed to amplify low-level audio signals from sources like microphones or music players to levels suitable for driving speakers. They are essential in audio systems to ensure clear and powerful sound reproduction.
    """)
    st.markdown("[Learn more about audio amplifiers](https://www.analog.com/en/resources/technical-articles/types-of-audio-amplifiers.html)")

    st.subheader("📡 RF (Radio Frequency) Amplifiers")
    st.markdown("""
    RF amplifiers boost high-frequency signals for transmission and reception in wireless communication systems, such as cell phones, Wi-Fi, and radar systems. They are crucial for maintaining signal integrity over long distances.
    """)
    st.markdown("[Detailed guide on RF amplifiers](https://rahsoft.com/2024/07/12/rf-power-amplifiers-types-and-applications/)")

    st.subheader("⚡ Power Amplifiers")
    st.markdown("""
    Power amplifiers deliver high-power signals to drive loads like motors or large speakers. They are used in applications requiring significant power output, including audio systems, broadcasting, and industrial equipment.
    """)
    st.markdown("[Overview of power amplifier classes](https://en.wikipedia.org/wiki/Power_amplifier_classes)")

    st.subheader("🧠 Operational Amplifiers (Op-Amps)")
    st.markdown("""
    Operational amplifiers are versatile integrated circuits used in analog signal processing, filtering, and control systems. They perform mathematical operations on signals and are fundamental components in many electronic devices.
    """)
    st.markdown("[Introduction to operational amplifiers](https://www.electronicshub.org/different-types-and-applications-of-amplifiers/)")
    st.subheader("🛠️ Error Amplifiers")
    st.markdown("""
    An **error amplifier** is a type of amplifier commonly used in **feedback control systems**, especially in **power supply circuits**, like voltage regulators and switch-mode power supplies (SMPS).

    It compares a reference voltage to a feedback voltage (typically from the output), and amplifies the **difference (error)** between them to adjust the system accordingly. This helps maintain a **stable and accurate output voltage**.

    ### 🔍 Key Features:
    - High gain to ensure accurate regulation.
    - Used with **compensation networks** for system stability.
    - Often built into ICs like **LM317**, **TL431**, or **PWM controllers** (e.g., TL494).

    ### 📌 Applications:
    - Power management ICs.
    - Voltage regulators (both linear and switching).
    - Control loops in analog systems.

    """)
    st.markdown("[Read more about Error Amplifiers](https://www.ti.com/lit/an/slva662/slva662.pdf)")


    st.markdown("---")
    st.button("🔙 Back" ,on_click=lambda:go_to("main"))



def amplifier_characteristics():
    st.title("📐 Amplifier Characteristics")
    st.markdown("---")

    st.subheader("🔺 1. Gain")
    st.markdown("**1.1 Voltage Gain (Av):**")
    st.latex(r"A_v = \frac{V_{out}}{V_{in}}")

    st.markdown("**1.2 Gain in Decibels (dB):**")
    st.latex(r"Gain_{dB} = 20 \times \log_{10}(A_v)")

    st.subheader("📊 2. Frequency Dependency")
    st.markdown("""
    The gain of an amplifier may change with frequency, especially in active filters and operational amplifiers. This characteristic is crucial in determining the amplifier's bandwidth and overall performance.
    """)

    st.subheader("📈 3. Linearity")
    st.markdown("""
    Ideal amplifiers provide constant gain without distortion. Linearity ensures that the output signal is a scaled version of the input, preserving the waveform's shape.
    """)

    st.subheader("🔒 4. Stability")
    st.markdown("""
    An amplifier's gain should remain constant despite changes in temperature or over time. Stability is vital for consistent performance in varying environmental conditions.
    """)

    st.subheader("📉 5. Frequency Response")

    st.markdown("""
    - **Frequency Response Curve:**  
      Represents how the amplifier's gain changes with different frequencies. Typically plotted as gain versus frequency.

    - **Bandwidth:**  
      The range of frequencies over which the amplifier can operate effectively. Defined between the lower and upper cutoff frequencies.  


    - **Cutoff Frequencies:**  
      - **Lower Cutoff (f_L):** The frequency below which the gain starts to decrease significantly.  
      - **Upper Cutoff (f_H):** The frequency above which the gain starts to decrease.  
      These points are commonly referred to as the -3 dB points, where the gain falls to approximately 70.7% of its maximum value.
    """)

    st.markdown("---")
    st.markdown("🔗 **References:**")
    st.markdown("- [Amplifier Gain and Decibels - Learn About Electronics](https://www.learnabout-electronics.org/Amplifiers/amplifiers13.php)")
    st.markdown("- [Frequency Response Analysis of Amplifiers and Filters](https://www.electronics-tutorials.ws/amplifier/frequency-response.html)")
    st.markdown("- [Amplifier Gain | All About Circuits](https://www.allaboutcircuits.com/textbook/semiconductors/chpt-1/amplifier-gain/)")
    st.markdown("- [Gain (electronics) - Wikipedia](https://en.wikipedia.org/wiki/Gain_(electronics))")

    st.markdown("---")
    st.button("🔙 Back" ,on_click=lambda:go_to("main"))


def noise():
    st.subheader("🔊  Noise Figure (NF)")
    st.markdown("""
    **Noise Figure (NF):**  
    Measures how much noise an amplifier adds to the signal. It's defined as the ratio of the signal-to-noise ratio (SNR) at the input to the SNR at the output.
    """)

    st.latex(r"NF = \frac{\text{SNR}_{\text{input}}}{\text{SNR}_{\text{output}}}")

    st.markdown("NF is often expressed in decibels (dB):")

    st.latex(r"NF_{dB} = 10 \times \log_{10}(NF)")

    st.markdown("""
    **Ideal Noise Figure:**  
    - An ideal amplifier has a noise figure of 1 (or 0 dB), meaning no additional noise is introduced.

    **Impact of NF:**  
    - A higher noise figure means the amplifier introduces more noise, reducing signal quality.  
    - Critical in low-noise applications (e.g., radio receivers, audio systems).
    """)

    st.subheader("⚡ Efficiency")
    st.markdown("""
    **Efficiency:**  
    Indicates how effectively an amplifier converts input power to output power.
    """)

    st.latex(r"\text{Efficiency} (\%) = \left( \frac{P_{out}}{P_{in}} \right) \times 100")

    st.markdown("""
    Where:  
    - \( P_{out} \): Output power  
    - \( P_{in} \): Input power  

    **Ideal Efficiency:**  
    - A 100% efficient amplifier would convert all input power to output power.  
    - In practice, some power is always lost (e.g., as heat).
    """)
    st.markdown("---")  
    st.button("🔙 Back" ,on_click=lambda:go_to("main"))


def amplifier_applications():
    st.title("🔌 Practical Amplifier Applications")
    st.markdown("---")

    st.subheader("🏠 Consumer Electronics")

    st.markdown("""
    **1. Audio Amplifiers**  
    - **Purpose:** Boosts audio signals to drive speakers and produce sound.  
    - **Examples:** Home audio systems, TV speakers, portable speakers.

    **2. Headphone Amplifiers**  
    - **Purpose:** Increases audio signal strength for clearer sound in headphones.  
    - **Examples:** Personal audio devices, gaming consoles, high-end headphones.

    **3. Microphone Preamplifiers**  
    - **Purpose:** Amplifies the weak signal from microphones for recording.  
    - **Examples:** Professional audio recording setups, live sound systems.

    **4. Signal Amplifiers in Communication Devices**  
    - **Purpose:** Strengthens weak signals in mobile phones, radios, and satellites.  
    - **Examples:** Mobile phones, two-way radios, satellite receivers.

    **5. Power Amplifiers in Electric Appliances**  
    - **Purpose:** Powers electric motors in household appliances.  
    - **Examples:** Washing machines, fans, power tools.
    """)

    st.subheader("🏭 Industrial Systems")

    st.markdown("""
    **1. Signal Conditioning**  
    - **Purpose:** Amplify weak signals from sensors or transducers for accurate processing.  
    - **Example:** Temperature or pressure sensors in manufacturing systems.

    **2. Motor Control**  
    - **Purpose:** Control speed and torque of electric motors.  
    - **Example:** In robotics or conveyor belts.

    **3. Audio Systems for Communication**  
    - **Purpose:** Ensure clear and loud messages in factories.  
    - **Example:** Public address systems, alarms, intercoms.

    **4. Power Amplification**  
    - **Purpose:** Drive large loads and equipment with boosted electrical power.  
    - **Example:** Industrial automation systems, large actuators.

    **5. Signal Filtering**  
    - **Purpose:** Remove noise from industrial signals using amplifiers and filters.  
    - **Example:** Clean data from sensors for accurate control.
    """)

    st.subheader("🏥 Medical Devices")

    st.markdown("""
    **1. ECG Signal Amplification**  
    - **Purpose:** Strengthen heart signals for monitoring.  
    - **Example:** ECG machines for cardiac diagnosis.

    **2. EEG Signal Amplification**  
    - **Purpose:** Amplify tiny electrical brain signals.  
    - **Example:** Sleep studies, brain disorder diagnosis.

    **3. Hearing Aids**  
    - **Purpose:** Amplify sound for individuals with hearing loss.  
    - **Example:** Boost ambient sounds for better hearing.

    **4. Ultrasound Imaging**  
    - **Purpose:** Enhance return signals for clearer images.  
    - **Example:** Diagnose internal organs using echo signal amplification.
    """)

    st.subheader("🚀 Future of Amplifiers")

    st.markdown("""
    **Modern Development**

    - **Smaller and More Efficient:**  
      Compact and low-power amplifiers are key for wearables and portable devices.

    - **Integration with Digital Systems:**  
      Smart amplifiers will be embedded in digital circuits for AI and IoT applications.

    - **Higher Frequency Ranges:**  
      Support for higher frequencies is vital for 5G and next-gen wireless tech.

    **Digital Amplifiers**

    - **Higher Efficiency:**  
      Less power loss, more usable output = longer battery life.

    - **DSP Integration:**  
      Digital Signal Processing allows better sound quality and real-time tuning.

    - **Miniaturization:**  
      Enables use in compact devices like earbuds and smartwatches.

    **Nano-Amplifiers**

    - **Miniaturization:**  
      Perfect for medical implants and ultra-small devices.

    - **Energy Efficiency:**  
      Critical for battery-powered and low-power gadgets.

    - **High-Speed Performance:**  
      Great for quantum computing and 5G+ networks.

    - **Flexible and Biocompatible:**  
      Potential for use in wearables and internal medical tech.
    """)

    st.markdown("---")  
    st.button("🔙 Back" ,on_click=lambda:go_to("main"))

def funn():
    # Page title
    st.title('Amplifier Metrics: Noise Figure & Efficiency')

    # Noise Figure section
    st.header('Noise Figure (NF)')
    st.write("""
        **Noise Figure (NF)** measures how much noise an amplifier adds to the signal.
        It is defined as the ratio of the signal-to-noise ratio (SNR) at the input to the SNR at the output.
        
        **Formula**:  
        NF = (SNR_input / SNR_output)
        
        NF is often expressed in decibels (dB):  
        NF(dB) = 10 × log10(NF)
        
        **Ideal NF**:  
        The best amplifier has a noise figure of 1 (or 0 dB), meaning no additional noise is introduced.
        
        **Impact of NF**:  
        A higher NF means more noise is introduced by the amplifier, reducing signal quality.  
        This is critical in low-noise applications such as radio receivers and audio equipment.
    """)

    # Noise Figure calculation
    st.subheader('Calculate Noise Figure')
    SNR_input = st.number_input('Enter SNR at input (dB)', min_value=0.0, max_value=100.0, value=30.0)
    SNR_output = st.number_input('Enter SNR at output (dB)', min_value=0.0, max_value=100.0, value=20.0)

    # NF Calculation
    NF = 10**((SNR_input - SNR_output) / 10)
    NF_dB = 10 * math.log10(NF)
    st.success(f"🔋 Noise Figure: {NF:.2f} dB")
    st.success(f"🔋 Noise Figure (dB): {NF_dB:.2f} dB")
    st.markdown("-----")
    # Efficiency section
    st.header('Efficiency')
    st.write("""
        **Efficiency** measures how well an amplifier converts input power into useful output power.
        
        **Formula**:  
        Efficiency (%) = (P_out / P_in) × 100
        
        Where:  
        - P_out is the output power  
        - P_in is the input power
        
        **Ideal Efficiency**:  
        The ideal amplifier would have 100% efficiency, meaning all input power is converted to useful output power.  
        In reality, no amplifier is perfectly efficient.
    """)

    # Efficiency calculation
    st.subheader('Calculate Efficiency')
    P_in = st.number_input('Enter input power (W)', min_value=0.01, max_value=100.0, value=10.0)
    P_out = st.number_input('Enter output power (W)', min_value=0.0, max_value=100.0, value=8.0)

    # Efficiency calculation
    if P_in != 0:
        efficiency = (P_out / P_in) * 100
        st.success(f"🔋 Efficiency: {efficiency:.2f} %")
    else:
        st.warning("Input power cannot be zero for efficiency calculation.")
    st.markdown("-----")
    st.button("🔙 Back" ,on_click=lambda:go_to("main"))


def regulator_calculation():
    try:
        st.title("🔧 Regulator Calculation")
        st.markdown("---")
        images = Image.open("unnamed.png")
        st.image(images, caption="Adjustable Voltage Regulator")
        st.markdown("---")
        st.markdown("""
        This tool calculates the output voltage of an **adjustable voltage regulator** .
        """)

        st.latex(r"V_{out} = V_{ref} \left(1 + \frac{R_2}{R_1} \right) + I_{adj} \times R_2")

        st.markdown("""
        Where:   
        - \( I_{adj} \) is typically very small (**~50µA**) and can be considered **optional**
        """)

        

        col1, col2, col3 = st.columns(3)

        with col1:
            R1 = st.number_input("Enter R1 (Ω)", min_value=0.01, value=1000.0, step=1.0)

        with col2:
            R2 = st.number_input("Enter R2 (Ω)", min_value=0.01, value=3000.0, step=1.0)

        with col3:
            include_Iadj = st.checkbox("Include Iadj?", value=False)
        Vref = st.number_input("Enter  Vref (V)", min_value=0.01, value=1.25, step=1.0)
        Iadj = 0
        if include_Iadj:
            Iadj = st.number_input("Enter Iadj (A)", min_value=0.0, value=0.00005, step=0.00001)

        
        Vout = Vref * (1 + R2 / R1) + Iadj * R2

        st.success(f"🔋 Output Voltage (Vout): {Vout:.2f} V")
        st.button("🔙 Back", on_click=lambda: go_to("main"))
    except Exception as e:
        st.error(f"Error in calculation: {e}")
def open_proteus_file(file_path):
        os.startfile(file_path)


def show_proteus_page():
    st.title("🔌 Proteus Simulation")
    st.markdown("---")
    st.markdown("### ⚡ Proteus Circuit Design")

    st.image("circuit_preview.png", caption="Simulation Circuit Preview")

    if st.button("🚀 Open in Proteus"):
        file_path = "pro.DSN" 
        if os.path.exists(file_path):
            open_proteus_file(file_path)
        else:
            st.error("⚠️ File not found. Please make sure  exists.")



if st.session_state.page == "main":
    st.title("🎯 Signal Processing App")
    st.markdown("### Welcome!")
    st.title(" DR. Mohamed Fouad")
    st.markdown(
        "This web application is designed to describe various operational models, providing insights into system performance and behavior. "
        "Explore the modules to understand how different parameters affect the system."
    )

    st.markdown("### 📶 Choose The Topic:")
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.button("🔄 Introduction to Amplifiers ", on_click=lambda: go_to(intro_amplifier()))
    with col2:  
        st.button("📶 Amplifier Importance", on_click=lambda: go_to(amplifier_importance()))
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.button("🚀 Amplifier Types", on_click=lambda: go_to(amplifier_types()))
    with col2:  
        st.button("🛰️ Amplifier Characteristics", on_click=lambda: go_to(amplifier_characteristics()))
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.button("🔄 Noise & Efficiency", on_click=lambda: go_to(noise()))
    with col2:  
        st.button("📦 Applications", on_click=lambda: go_to(amplifier_applications()))
    st.markdown("---")
    st.markdown("### 🛎️ Apps")
    col1, col2 = st.columns(2)
    with col1:
        st.button("🔄 Regulator Calculation", on_click=lambda: go_to("regulator"))
    with col2:  
        st.button("📦 Noise & Efficiency", on_click=lambda: go_to("Noise_Efficiency"))
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.button("📦 Download file", on_click=lambda: go_to("f"))
    with col2:  
        st.button("🔄 Open Proteus", on_click=lambda: go_to("proteus"),disabled=True)



elif st.session_state.page == "regulator":
    regulator_calculation()

elif st.session_state.page == "Noise_Efficiency":
    funn()
elif st.session_state.page == "proteus":
    st.title("🔄 Proteus Simulation")
    st.markdown("---")
    st.markdown("### Proteus Simulation")
    show_proteus_page()
    st.button("🔙 Back", on_click=lambda: go_to("main"))
elif st.session_state.page == "f":
    st.title("📦 Download File")
    st.markdown("---")
    st.markdown("### Download the Proteus file")
    st.markdown("Click the button below to download the Proteus file for the circuit simulation.")
    st.markdown("### Proteus File: pro.DSN")
    st.markdown("This file contains the circuit design for the adjustable voltage regulator.")

    with open("pro.DSN", "rb") as file:
        st.download_button(
            label="📥 Download Proteus File",
            data=file,
            file_name="pro.DSN",
            mime="application/octet-stream"
        )
    st.button("🔙 Back" ,on_click=lambda:go_to("main"))




