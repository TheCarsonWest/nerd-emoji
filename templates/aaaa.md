<%*
function callGemini(prompt, apiKey, callback) {
  const apiUrl = 'https://api.generativeai.google.com/v1beta2/models/gemini-2.0-flash:generateText'; // Or the appropriate Gemini API endpoint

  fetch(apiUrl, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${apiKey}`, // Important: Use your actual API key!
    },
    body: JSON.stringify({
      prompt: {
        text: prompt,
      },
      temperature: 0.7, // Example
      maxOutputTokens: 512, // Example
    }),
  })
  .then(response => {
      if (!response.ok) {
        return response.json().then(errorData => { // Parse error for better message
          throw new Error(`Gemini API error: ${response.status} - ${errorData.error.message || response.statusText}`);
        }).catch(() => { // Fallback if error parsing fails
          throw new Error(`Gemini API error: ${response.status} - ${response.statusText}`);
        });
      }
      return response.json();
    })
  .then(data => {
      // Process the response data. The structure will depend on the API.
      if (data.candidates && data.candidates.length > 0) {
        const generatedText = data.candidates.output;
        callback(null, generatedText); // Call the callback with the result
      } else if (data.results && data.results.length > 0) { // Older API versions
        const generatedText = data.results.text;
        callback(null, generatedText);
      } else {
        callback(null, "No text generated.");
      }
    })
  .catch(error => {
      console.error("Error calling Gemini API:", error);
      callback(error, null); // Call the callback with the error
    });
}

// Example usage (replace with your actual API key and prompt):
const apiKey = 'AIzaSyAfpYohLt9_38V4VwFrHqA1j1pt7ufxKP8'; // Replace with your actual API key
const userPrompt = "Write a short story about a talking dog.";

callGemini(userPrompt, apiKey, (err, generatedText) => {
  if (err) {
    console.error("Error:", err);
    // Handle the error appropriately
  } else if (generatedText) {
    console.log("Generated Text:", generatedText);
    // Do something with the generated text
  }
});
%>