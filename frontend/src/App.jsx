import { useState } from "react";

function App() {
  // two pieces of memory: user input and gemini response
  const [response, setResponse] = useState("");
  const [message, setMessage] = useState("");

  /* 
    res = Send an HTTP POST Request to "/chat" endpoint with user input as JSON
    data = Converts Gemini AI's JSON response into a JavaScript object 
    returns the response
  */
  async function chat() {
    const res = await fetch(
      "http://127.0.0.1:8000/chat",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: message, })
      }
    );

    const data = await res.json();
    setResponse(data.response);
    setMessage("");
  }

  return (
    <div style={{ padding: "40px" }}>
      <h1>Career Interview Copilot</h1>
      
      <input
        type = "text"
        placeholder = "Enter your message"
        value = {message}
        onChange = {(e) => setMessage(e.target.value)}
      />

      <button onClick={chat}>
        Ask
      </button>

      <p>{response}</p>
    </div>
  );
}

export default App;