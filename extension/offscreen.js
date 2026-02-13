// This script runs in the offscreen document and has access to audio APIs
chrome.runtime.onMessage.addListener(async (message) => {
  if (message.target === 'offscreen') {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    // Add your MediaRecorder logic here to send data back to popup.js
    console.log("Audio stream captured in offscreen document");
  }
});