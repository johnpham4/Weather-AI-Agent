function renderNewMessage(text, role) {
  const conversationContainer = document.getElementById("conversation")
  const newArticle = document.createElement("article")
  newArticle.classList.add(role === "assistant" ? "ai-message" : "user-message")
  const newParagraph = document.createElement("p")
  newParagraph.textContent = text
  newArticle.append(newParagraph)
  conversationContainer.append(newArticle)
  scrollToBottom()
}

function scrollToBottom() {
  requestAnimationFrame(() => {
      document.body.scrollIntoView({ behavior: "smooth", block: "end" })
  });
}

document.getElementById("form").addEventListener("submit", async (e) => {
  e.preventDefault()
  const input = document.getElementById("user-input")
  const query = input.value
  input.value = ""


  renderNewMessage(query, "user")

  // Gửi câu hỏi lên server
  const res = await fetch("http://localhost:8000/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query })
  })

  const data = await res.json()
  console.log("Response:", data)
  // Hiện phản hồi từ AI lên UI
  renderNewMessage(data.response, "assistant")
})
