const express = require("express");
const fs = require("fs");
const cors = require("cors");

const app = express();
app.use(cors());
app.use(express.json());

const JOBS_PATH = "/root/projects/jobflow/outputs/hot_jobs.json";

// ==============================
// HARD DEBUG TEST ROUTE
// ==============================
app.get("/debug", (req, res) => {
    try {
        const exists = fs.existsSync(JOBS_PATH);
        const stats = exists ? fs.statSync(JOBS_PATH) : null;

        res.json({
            path: JOBS_PATH,
            exists,
            size: stats ? stats.size : null,
            readable: exists ? fs.accessSync(JOBS_PATH, fs.constants.R_OK) === undefined : false
        });
    } catch (err) {
        res.json({
            error: err.message
        });
    }
});

// ==============================
// GET JOBS (SAFE MODE)
// ==============================
app.get("/jobs", (req, res) => {
    try {
        const raw = fs.readFileSync(JOBS_PATH, "utf-8");

        // ✅ Remove BOM + bad chars
        const clean = raw
            .replace(/^\uFEFF/, "")
            .replace(/\u0000/g, "")
            .trim();

        let jobs;

        try {
            jobs = JSON.parse(clean);
        } catch (parseError) {
            console.error("❌ JSON PARSE ERROR:", parseError.message);

            // 🔥 Fallback: return raw data for debugging
            return res.status(500).json({
                error: "JSON parse failed",
                details: parseError.message
            });
        }

        res.json(jobs);

    } catch (err) {
        console.error("❌ READ ERROR:", err.message);
        res.status(500).json({ error: err.message });
    }
});

// ==============================
app.listen(5000, "0.0.0.0", () => {
    console.log("🚀 Server running on 0.0.0.0:5000");
});
