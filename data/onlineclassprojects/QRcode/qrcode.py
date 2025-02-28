import streamlit as st
import qrcode
from PIL import Image
from pyzbar.pyzbar import decode
import io
import cv2
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase

# Configure the Streamlit app with title, icon, and wide layout
st.set_page_config(page_title="QR Code Tool", page_icon="🔳", layout="wide")

# Class for real-time QR code scanning using webcam
class QRCodeScanner(VideoTransformerBase):
    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")  # Convert frame to NumPy array
        decoded_objects = decode(img)  # Decode QR codes from the frame
        for obj in decoded_objects:
            st.success(f"Decoded Text: {obj.data.decode('utf-8')}")  # Display decoded text
        return img  # Return the frame for display

# Function to generate a QR code from given text or URL
def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')  # Create QR code image
    return img

# Function to decode QR codes from an uploaded image
def decode_qr_code(uploaded_image):
    image = Image.open(uploaded_image)  # Open the image file
    decoded_objects = decode(image)  # Decode the QR code
    decoded_texts = [obj.data.decode('utf-8') for obj in decoded_objects]  # Extract text
    return decoded_texts

# App title and description
st.title("🔳 QR Code Encoder & Decoder")
st.markdown("### A simple tool to generate, decode, and scan QR codes in real-time.")

# Layout with two columns for generating and decoding QR codes
col1, col2 = st.columns(2)
with col1:
    st.subheader("Generate QR Code")
    input_text = st.text_input("Enter text or URL to generate QR Code")
    if st.button("Generate QR Code", use_container_width=True):
        if input_text:
            qr_image = generate_qr_code(input_text)
            img_bytes = io.BytesIO()
            qr_image.save(img_bytes, format='PNG')
            st.image(qr_image, caption="Generated QR Code")
            st.download_button("Download QR Code", img_bytes.getvalue(), "qrcode.png", "image/png")
        else:
            st.error("Please enter text or a URL")

with col2:
    st.subheader("Decode QR Code")
    uploaded_file = st.file_uploader("Upload a QR Code image", type=["png", "jpg", "jpeg"], help="Upload an image containing a QR code")
    if uploaded_file:
        st.image(uploaded_file, caption="Uploaded QR Code", use_column_width=True)
        decoded_texts = decode_qr_code(uploaded_file)
        if decoded_texts:
            st.success("Decoded Text:")
            for text in decoded_texts:
                st.code(text, language='plaintext')
        else:
            st.error("No QR code detected or could not decode.")

# Section for real-time QR code scanning using webcam
st.subheader("📷 Scan QR Code using Camera")
st.write("Use your webcam to scan QR codes in real-time.")
webrtc_streamer(key="qr_scanner", video_transformer_factory=QRCodeScanner)

# Display features of the tool
st.markdown("---")
st.markdown("### Features:")
st.markdown("✅ Generate QR codes from text or URLs")
st.markdown("✅ Decode QR codes from uploaded images")
st.markdown("✅ Scan QR codes in real-time using your webcam")
st.markdown("✅ Download generated QR codes")
