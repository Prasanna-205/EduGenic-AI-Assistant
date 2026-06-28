async function askAI() {
    const question = document.getElementById("question").value;

    const response = await fetch("http://127.0.0.1:8000/ask", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            question: question
        })
    });

    const data = await response.json();
    document.getElementById("answer").innerText = data.answer;
}
async function generateQuiz() {
    const question = document.getElementById("question").value;

    document.getElementById("answer").innerText = "Generating quiz...";

    const response = await fetch("http://127.0.0.1:8000/quiz", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            question: question
        })
    });

    const data = await response.json();
    document.getElementById("answer").innerHTML =
        data.answer.replace(/\n/g, "<br>");
}
async function summarizeText() {
    const question = document.getElementById("question").value;

    document.getElementById("answer").innerText = "Summarizing...";

    const response = await fetch("http://127.0.0.1:8000/summarize", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            question: question
        })
    });

    const data = await response.json();
    document.getElementById("answer").innerHTML =
        data.answer.replace(/\n/g, "<br>");
}
async function learningPath() {
    const question = document.getElementById("question").value;

    document.getElementById("answer").innerText = "Creating learning path...";

    const response = await fetch("http://127.0.0.1:8000/learning-path", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            question: question
        })
    });

    const data = await response.json();
    document.getElementById("answer").innerHTML =
        data.answer.replace(/\n/g, "<br>");
}