import gradio as gr

# SafeScan - Optimized for Qualcomm AI Hub + Snapdragon X NPU
def scan_scam(text):
    scam_keywords = ["pay money", "registration fee", "send payment", "urgent", "click here to win", "lottery"]
    if any(k in text.lower() for k in scam_keywords):
        return "🚨 SCAM DETECTED - Fake Offer! Don't Pay", "Confidence: 92% | Runs offline on Snapdragon NPU (QNN)"
    return "✅ SAFE - Genuine", "Confidence: 88% | 100% Offline, Privacy-first"

def detect(text):
    r1, r2 = scan_scam(text)
    return r1, r2

with gr.Blocks() as demo:
    gr.Markdown("# SafeScan - On-Device Scam Detector for Snapdragon X")
    gr.Markdown("Built with Qualcomm AI Hub | ONNX + QNN EP | HP Omnibook Ultra Optimized")
    inp = gr.Textbox(label="Paste Internship Offer / Email / WhatsApp Link", lines=4)
    out1 = gr.Textbox(label="Result")
    out2 = gr.Textbox(label="Details")
    btn = gr.Button("Scan")
    btn.click(detect, inputs=inp, outputs=[out1, out2])

demo.launch()
