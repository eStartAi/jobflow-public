import { useEffect, useState } from "react";

export default function App() {
  const [jobs, setJobs] = useState([]);
  const [aiOutput, setAiOutput] = useState("");
  const [showModal, setShowModal] = useState(false);

  useEffect(() => {
    fetch("http://158.220.123.227:5000/jobs")
      .then(res => res.json())
      .then(data => setJobs(data))
      .catch(err => console.error("Fetch error:", err));
  }, []);

  // 🤖 Generate Resume
  const generateAI = async (job) => {
    try {
      const res = await fetch("http://158.220.123.227:5000/generate", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ job })
      });

      const data = await res.json();

      if (data.success) {
        setAiOutput(data.output);
        setShowModal(true);
      } else {
        alert("❌ AI Failed");
      }
    } catch (err) {
      console.error(err);
      alert("❌ Request failed");
    }
  };

  // 💬 Generate Answers
  const generateAnswers = async (job) => {
    try {
      const res = await fetch("http://158.220.123.227:5000/answers", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ job })
      });

      const data = await res.json();

      if (data.success) {
        setAiOutput(data.output);
        setShowModal(true);
      } else {
        alert("❌ AI Failed");
      }
    } catch (err) {
      console.error(err);
      alert("❌ Request failed");
    }
  };

  // 🚀 Mark Applied
  const apply = (title) => {
    alert(`🚀 Marked Applied: ${title}`);
  };

  return (
    <div
      style={{
        background: "#0f172a",
        minHeight: "100vh",
        padding: 20,
        color: "white"
      }}
    >
      <h1>🔥 JobFlow Elite</h1>

      {jobs.length === 0 && <p>Loading jobs...</p>}

      {jobs.map((job, i) => (
        <div
          key={i}
          style={{
            background: "#1e293b",
            padding: 15,
            marginTop: 15,
            borderRadius: 10
          }}
        >
          <h3>{job.title}</h3>
          <p>{job.company}</p>
          <p>{job.location}</p>

          <p
            style={{
              color:
                job.score > 200
                  ? "#22c55e"
                  : job.score > 100
                  ? "#facc15"
                  : "#ef4444"
            }}
          >
            Score: {job.score}
          </p>

          <div style={{ marginTop: "10px" }}>
            <button onClick={() => generateAI(job)}>
              🤖 Generate Resume
            </button>

            <button onClick={() => apply(job.title)}>
              🚀 Mark Applied
            </button>

            <button onClick={() => generateAnswers(job)}>
              💬 Generate Answers
            </button>
          </div>
        </div>
      ))}

      {/* 🧠 AI MODAL */}
      {showModal && (
        <div
          style={{
            position: "fixed",
            top: 0,
            left: 0,
            width: "100%",
            height: "100%",
            background: "rgba(0,0,0,0.8)",
            display: "flex",
            justifyContent: "center",
            alignItems: "center",
            zIndex: 999
          }}
        >
          <div
            style={{
              background: "#1e293b",
              padding: 20,
              width: "70%",
              maxHeight: "80%",
              overflowY: "auto",
              borderRadius: 10
            }}
          >
            <h2>🧠 AI Output</h2>

            <pre style={{ whiteSpace: "pre-wrap" }}>
              {aiOutput}
            </pre>

            <br />

            <button onClick={() => navigator.clipboard.writeText(aiOutput)}>
              📋 Copy
            </button>

            <button onClick={() => setShowModal(false)}>
              ❌ Close
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
