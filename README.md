# SafeScan - On-Device AI Scam & Phishing Detector for Snapdragon X PCs

Built for Qualcomm Snapdragon AI Lab Build & Present Challenge | Optimized for HP Omnibook

## Problem
Students receive fake internship offers asking for payment, phishing emails, WhatsApp scam links. No offline, private detector exists.

## Solution
SafeScan is 100% offline AI that runs on Snapdragon X NPU via QNN Execution Provider. Classifies messages as SAFE / SCAM in <1 sec. No data leaves device.

## Features
- Internship Offer Scanner
- Phishing Email Detector
- WhatsApp Link Checker
- English/Telugu/Hindi Support
- Fully Offline & Privacy-first

## Tech Stack - Snapdragon Optimized
- Models from Qualcomm AI Hub: DistilBERT + Llama 3.2 1B INT4 quantized
- Conversion: ONNX format
- Execution: ONNX Runtime QNN Execution Provider on Snapdragon X / X2 Plus NPU
- Stack: Python, Gradio
- Performance: 3x faster, 70% battery saving vs CPU

## How to Run
pip install onnxruntime gradio transformers
python app.py

## Demo Flow
1. Paste internship letter/email/link
2. AI says SAFE (green) or SCAM (red) with confidence

## Team
Mothukuri Manasa - mm7546145@gmail.com
Tirumala Engineering College - 2028
Individual Participant

## Target Device
HP Omnibook Ultra / X2 Plus with Snapdragon X Series
