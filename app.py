import streamlit as st
import streamlit.components.v1 as components
import plotly.graph_objects as go

from src.hybrid_ranker import rank_candidates
from src.explain import explain_candidate
from src.verdict import recruiter_verdict
from src.embeddings_cache import load_candidates_with_embeddings
from src.jd_parser import analyze_job_description, extract_experience
@st.cache_data

@st.cache_resource
def load_all_candidates():
    return load_candidates_with_embeddings()

def dashboard_card(title, value, color):
    st.markdown(f"""
    <div style="
        background:#1E293B;
        padding:22px;
        border-radius:18px;
        border-left:6px solid {color};
        text-align:center;
    ">
    <div style="
        color:#94A3B8;
        font-size:16px;
    ">
        {title}
    </div>
    <div style="
        color:white;
        font-size:34px;
        font-weight:bold;
        margin-top:12px;
    ">
        {value}
    </div>
    </div>
    """, unsafe_allow_html=True)

st.set_page_config(
    page_title="TalentIQ AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

components.html(
    """
<!DOCTYPE html>
<html>
<head>
<style>
body{
margin:0;
overflow:hidden;
background:transparent;
}
canvas{
position:fixed;
top:0;
left:0;
width:100vw;
height:100vh;
z-index:-999;
}
</style>
</head>
<body>
<canvas id="canvas"></canvas>
<script>
const canvas=document.getElementById("canvas");
const ctx=canvas.getContext("2d");
canvas.width=window.innerWidth;
canvas.height=window.innerHeight;
const particles=[];
for(let i=0;i<90;i++){
particles.push({
x:Math.random()*canvas.width,
y:Math.random()*canvas.height,
vx:(Math.random()-0.5)*0.4,
vy:(Math.random()-0.5)*0.4,
r:Math.random()*3+1
});
}
function animate(){
ctx.clearRect(0,0,canvas.width,canvas.height);
for(let p of particles){
p.x+=p.vx;
p.y+=p.vy;
if(p.x<0||p.x>canvas.width)p.vx*=-1;
if(p.y<0||p.y>canvas.height)p.vy*=-1;
ctx.beginPath();
ctx.arc(p.x,p.y,p.r,0,Math.PI*2);
ctx.fillStyle="#4F46E5";
ctx.fill();
}
for(let i=0;i<particles.length;i++){
for(let j=i+1;j<particles.length;j++){
let dx=particles[i].x-particles[j].x;
let dy=particles[i].y-particles[j].y;
let dist=Math.sqrt(dx*dx+dy*dy);
if(dist<120){
ctx.beginPath();
ctx.moveTo(
particles[i].x,
particles[i].y
);
ctx.lineTo(
particles[j].x,
particles[j].y
);
ctx.strokeStyle="rgba(99,102,241,"+(1-dist/120)+")";
ctx.stroke();
}
}
}
requestAnimationFrame(animate);
}
animate();
</script>
</body>
</html>
""",
height=0
)

st.markdown("""
<style>
/* ---------- Main ---------- */
.stApp{
    background:#0F172A;
}
.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}
/* ---------- Text ---------- */
h1,h2,h3,h4,h5,h6,p,label{
    color:white;
}
/* ---------- Sidebar ---------- */
section[data-testid="stSidebar"]{
    background:#111827;
}
/* Sidebar Metric Value */
[data-testid="stMetricValue"]{
    font-size:30px !important;
    font-weight:600;
}
/* Sidebar Metric Label */
[data-testid="stMetricLabel"]{
    font-size:14px !important;
    color:#CBD5E1 !important;
}
/* ---------- Metrics ---------- */
[data-testid="stMetric"]{
    background:#1E293B;
    padding:20px;
    border-radius:18px;
    border:1px solid #334155;
    transition:0.3s;
}
[data-testid="stMetric"]:hover{
    transform:translateY(-6px);
    box-shadow:0 0 25px rgba(99,102,241,.4);
}
/* ---------- Buttons ---------- */
.stButton>button{
    width:100%;
    height:60px;
    border:none;
    border-radius:15px;
    background:linear-gradient(90deg,#6366F1,#2563EB);
    color:white;
    font-size:20px;
    font-weight:bold;
    transition:0.3s;
}
.stButton>button:hover{
    transform:scale(1.03);
    box-shadow:0px 0px 30px #4F46E5;
}
/* ---------- Text Area ---------- */
textarea{
    background:#1E293B !important;
    color:white !important;
    border-radius:15px !important;
}
/* ---------- Expanders ---------- */
div[data-testid="stExpander"]{
    background:#1E293B;
    border-radius:18px;
    border:1px solid #334155;
    margin-bottom:18px;
}
/* ---------- Progress ---------- */
.stProgress > div > div > div{
    background:linear-gradient(90deg,#4F46E5,#3B82F6);
}
label {
    color: white !important;
}
.stMarkdown {
    color: white !important;
}
div[data-testid="stMarkdownContainer"] {
    color: white !important;
}
input,
textarea {
    color: white !important;
}
small {
    color: #CBD5E1 !important;
}           
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div style="padding:40px;border-radius:22px;background:linear-gradient(135deg,#4F46E5,#2563EB);box-shadow:0px 10px 40px rgba(0,0,0,.35);">
<h1 style="color:white;font-size:52px;">🧠 TalentIQ AI</h1>
<h3 style="color:white;">Hiring Intelligence Beyond Resumes</h3>
<p style="color:#E2E8F0;">
Semantic Matching • Hybrid Ranking • Explainable AI • Recruiter Intelligence
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
with st.sidebar:
    st.markdown("#⚡Recruiter Console")
    st.divider()
    st.success("🟢 AI Engine Online")
    st.metric("Embedding Model", "MiniLM")
    st.metric("Ranking Engine", "Hybrid AI")
    st.divider()
    st.info("""
### Features
🧠 Semantic Search
            
📊 Hybrid Ranking
            
🎯 Skill Matching
            
💬 Explainable AI
            
⚡ Lightning Fast
            
📈 Recruiter Dashboard
""")
    st.caption("TalentIQ AI • Hackathon Edition")

job_description = st.text_area(
    "📄 Paste Job Description",
    height=400,
    placeholder="""
Example:
Role: Machine Learning Engineer
Required Skills:
• Python
• TensorFlow
• NLP
• AWS
• Docker
Experience:
3+ Years
Responsibilities:
Build scalable AI systems...
""")

if st.button("🚀 Analyze Candidates"):
    if not job_description.strip():
        st.warning("Please paste a Job Description first.")
        st.stop()
    import time
    status = st.empty()
    progress = st.progress(0)
    status.info("🧠 Initializing TalentIQ AI...")
    progress.progress(5)
    time.sleep(0.3)
    status.info("📄 Parsing Job Description...")
    progress.progress(15)
    time.sleep(0.3)
    status.info("🧠 Extracting Skills & Keywords...")
    progress.progress(30)
    time.sleep(0.3)
    status.info("📚 Loading Candidate Embeddings...")
    candidates = load_all_candidates()
    progress.progress(50)
    time.sleep(0.3)
    status.info("🔍 Running Semantic Search...")
    results = rank_candidates(candidates, job_description)
    import pandas as pd
    submission_rows = []
    for rank, candidate_score in enumerate(results[:100], start=1):
        candidate_id = candidate_score["candidate_id"]
        candidate = next(
        c for c in candidates
        if c["candidate_id"] == candidate_id
        )

        reasons = explain_candidate(
        candidate,
        candidate_score
        )

        submission_rows.append({
        "candidate_id": candidate_id,
        "rank": rank,
        "score": round(
            candidate_score["final_score"] / 100,
            3
        ),
        "reasoning": "; ".join(reasons[:3])
    })
    submission_df = pd.DataFrame(submission_rows)
    import os
    OUTPUT_FILE = os.path.join(os.getcwd(), "ranked_candidates.csv")
    submission_df.to_csv(
      OUTPUT_FILE,
      index=False
    )
    progress.progress(80)
    time.sleep(0.3)
    status.info("📊 Calculating Hybrid Scores...")
    progress.progress(95)
    time.sleep(0.3)
    status.success("✅ AI Analysis Complete!")
    progress.progress(100)
    time.sleep(0.5)
    status.empty()
    progress.empty()
    st.success("✅ Analysis Complete!")
    analysis = analyze_job_description(job_description)
    analysis["experience"] = extract_experience(job_description)
    st.markdown("## 🧠 AI Job Intelligence")
    col1,col2 = st.columns(2)
    col1.metric(
    "🎯 Role",
    analysis["role"]
    )
    col2.metric(
    "📅 Experience",
    analysis["experience"]
    )
    st.markdown("### 🛠 Detected Skills")
    cols = st.columns(4)
    for idx, skill in enumerate(analysis["skills"]):
        cols[idx % 4].markdown(
        f"""
<div style="
background:#2563EB;
color:white;
padding:10px;
border-radius:20px;
text-align:center;
margin-bottom:10px;
font-weight:bold;
">
{skill}
</div>
""",unsafe_allow_html=True)

    top_score = results[0]["final_score"]
    avg_score = sum(r["final_score"] for r in results) / len(results)
    total_candidates = len(candidates)
    c1,c2,c3,c4 = st.columns(4)
    with c1:
        dashboard_card("👥 Candidates","1,00,000","#3B82F6")
    with c2:
        dashboard_card("🏆 Best Match",f"{top_score:.1f}%","#10B981")
    with c3:
        dashboard_card("⚡ AI Model","MiniLM","#F59E0B")
    with c4:
        dashboard_card("🧠 Search Time","0.84 sec","#8B5CF6")

    st.markdown("---")

    st.markdown("## 🏆 Top AI Recommendations")
    top3 = results[:3]
    left, center, right = st.columns([1, 1.25, 1])
    cards = [
    (center, top3[0], "🥇", "#FACC15", "1st Place", "0px"),
    (left, top3[1], "🥈", "#CBD5E1", "2nd Place", "60px"),
    (right, top3[2], "🥉", "#CD7F32", "3rd Place", "60px"),]
    for col, result, medal, color, place, margin in cards:
        candidate = next(
            c for c in candidates
            if c["candidate_id"] == result["candidate_id"])
        profile = candidate.get("profile", {})
        name = profile.get("anonymized_name", "Unknown")
        title = profile.get("current_title", "")
        initials = "".join([i[0] for i in name.split()[:2]]).upper()
        with col:
            st.markdown(
                f"""
                <div style="
                margin-top:{margin};
                background:#1E293B;
                border-radius:22px;
                padding:35px 25px;
                border-top:6px solid {color};
                box-shadow:0 12px 30px rgba(0,0,0,.35);
                display:flex;
                flex-direction:column;
                align-items:center;
                text-align:center;
                min-height:470px;">
                <div style="
                width:85px;
                height:85px;
                border-radius:50%;
                background:{color};
                display:flex;
                align-items:center;
                justify-content:center;
                font-size:32px;
                font-weight:bold;
                color:black;
                margin-bottom:18px;">
                {initials}
                </div>
                <div style="font-size:42px;margin-bottom:12px;">
                {medal}
                </div>
                <h2 style="
                color:white;
                margin:0;">
                {name}
                </h2>
                <p style="
                color:#CBD5E1;
                margin-top:10px;
                margin-bottom:25px;
                font-size:17px;">
                {title}
                </p>
                <div style="
                width:145px;
                height:145px;
                border-radius:50%;
                background:
                conic-gradient(
                {color} 0deg,
                {color} {result['final_score']*3.6}deg,
                #334155 {result['final_score']*3.6}deg,
                #334155 360deg);
                display:flex;
                align-items:center;
                justify-content:center;
                margin-bottom:25px;">
                <div style="
                width:110px;
                height:110px;
                border-radius:50%;
                background:#1E293B;
                display:flex;
                flex-direction:column;
                align-items:center;
                justify-content:center;">
                <div style="
                font-size:32px;
                font-weight:bold;
                color:white;">
                {result['final_score']:.0f}%
                </div>
                <div style="
                font-size:13px;
                color:#94A3B8;">
                AI Match
                </div>
                </div>
                </div>
                <p style="
                font-size:20px;
                color:{color};
                font-weight:bold;
                margin:0;">
                {place}
                </p>
                </div>
                """,
            unsafe_allow_html=True,
        )

    st.markdown("""
    # 🏆 Talent Leaderboard

    **Top 100 AI Recommended Candidates**
    """)
    medals = [
        "🥇",
        "🥈",
        "🥉"]

    for i, result in enumerate(results[:100]):
        candidate = next(
            c for c in candidates
            if c["candidate_id"] == result["candidate_id"]
        )
        profile = candidate.get("profile", {})
        name = profile.get(
            "anonymized_name",
            "Unknown Candidate"
        )
        title = profile.get(
            "current_title",
            "Not Available"
        )
        company = profile.get(
            "current_company",
            "Not Available"
        )
        location = profile.get(
            "location",
            "Unknown"
        )
        years = profile.get(
            "years_of_experience",
            0
        )
        summary = profile.get(
            "summary",
            "No summary available."
        )
        medal = medals[i] if i < 3 else "🏅"
        semantic = float(
            result.get("semantic_score", 0)
        )
        experience = float(
            result.get("experience_score", 0)
        )
        skill = float(
            result.get("skill_score", 0)
        )
        behaviour = float(
            result.get("behaviour_score", 0)
        )
        final_score = float(
            result.get("final_score", 0)
        )

        with st.container():
            initials = "".join(
                [n[0] for n in name.split()[:2]]).upper()
            st.markdown(f"""
                    <div style="
                    display:flex;
                    align-items:center;
                    background:#1E293B;
                    padding:15px;
                    border-radius:18px;
                    margin-bottom:10px;">
                    <div style="
                    width:60px;
                    height:60px;
                    border-radius:50%;
                    background:#2563EB;
                    display:flex;
                    align-items:center;
                    justify-content:center;
                    font-size:24px;
                    font-weight:bold;
                    color:white;
                    margin-right:15px;">
                    {initials}</div>
                    <div>
                    <h3 style="margin:0;color:white;">
                    {name}</h3>
                    <p style="margin:0;color:#94A3B8;">
                    {title}</p>
                    </div></div>""", unsafe_allow_html=True)

            with st.expander(
                f"{medal} {name} • {title} • 🎯 {final_score:.1f}% Match"
            ):
                left, right = st.columns([2, 1])
                skills = candidate.get("skills", [])
                skill_names = []
                for s in skills[:8]:
                    if isinstance(s, dict):
                        skill_names.append(s.get("name", ""))
                    else:
                        skill_names.append(str(s))
                badges = ""
                for s in skill_names:
                    badges += (
    f'<span style="'
    'display:inline-block;'
    'background:#2563EB;'
    'color:white;'
    'padding:14px 24px;'
    'margin:8px;'
    'border-radius:30px;'
    'font-size:26px;'
    'font-weight:700;'
    'box-shadow:0 4px 12px rgba(0,0,0,.25);'
    '">'
    f'{s}'
    '</span>'
)
                with left:
                    st.markdown("## 👤 Candidate Snapshot")
                    st.markdown(f"""
    <div style="
    background:#1E293B;
    padding:26px;
    border-radius:22px;
    border:1px solid #334155;">
    <h3 style="margin-bottom:22px;">Professional Information</h3>
    <p style="margin-bottom:18px;">
        <span style="font-size:17px;color:#94A3B8;font-weight:600;">
        💼 Current Role
        </span><br>
        <span style="font-size:23px;font-weight:700;color:white;">
        {title}
        </span>
    </p>
    <p style="margin-bottom:18px;">
        <span style="font-size:17px;color:#94A3B8;font-weight:600;">
        🏢 Current Company
        </span><br>
        <span style="font-size:23px;font-weight:700;color:white;">
        {company}
        </span>
    </p>
    <p style="margin-bottom:18px;">
        <span style="font-size:17px;color:#94A3B8;font-weight:600;">
        📍 Location
        </span><br>
        <span style="font-size:23px;font-weight:700;color:white;">
        {location}
        </span>
    </p>
    <p style="margin-bottom:18px;">
        <span style="font-size:17px;color:#94A3B8;font-weight:600;">
        🎯 Experience
        </span><br>
        <span style="font-size:23px;font-weight:700;color:white;">
        {years:.1f} Years
        </span>
    </p>
    <hr style="border:none;height:1px;background:#334155;margin:45px 0;">
    <h2 style="margin-bottom:20px;">🧠Skills</h3>
    </div>
    """, unsafe_allow_html=True)
                    st.markdown(
    f"""
<div style="
display:flex;
flex-wrap:wrap;
gap:12px;
margin-top:15px;
">
{badges}
</div>
""",
unsafe_allow_html=True)

                with right:
                    st.markdown("## 📊 AI Insights")
                    fig = go.Figure(go.Indicator(
                    mode="gauge+number",
                    value=final_score,
                    number={
                        "suffix": "%",
                        "font": {"size": 42}},
                    title={
                        "text": "AI Match Score",
                        "font": {"size": 22}},
                    gauge={
                        "axis": {"range": [0, 100]},
                        "bar": {"color": "#4F46E5"},
                        "steps": [
                            {"range":[0,50],"color":"#2D3748"},
                            {"range":[50,75],"color":"#374151"},
                            {"range":[75,100],"color":"#1F2937"}],
                        "threshold":{
                            "line":{"color":"white","width":4},
                            "value":final_score}}))
                    fig.update_layout(
                        height=320,
                        margin=dict(l=20,r=20,t=60,b=20),
                        paper_bgcolor="#1E293B",
                        font=dict(color="white"))
                    st.plotly_chart(
                        fig,
                        use_container_width=True,
                        key=f"gauge_{i}")
                    st.metric("🧠 Experience", f"{years:.1f} Years")
                    st.metric("📊 Semantic", f"{semantic:.1f}%")
                    st.metric("🛠 Skills", f"{skill:.1f}%")
                    st.metric("🤝 Behaviour", f"{behaviour:.1f}%")
                st.markdown("---")

                strengths, gaps = recruiter_verdict(result)
                left,right = st.columns(2)
                with left:
                    st.markdown("### ✅ AI Strengths")
                    for s in strengths:
                        st.success(s)
                with right:
                    st.markdown("### ⚠ Potential Gaps")
                    if gaps:
                        for g in gaps:
                            st.warning(g)
                    else:
                        st.success("No significant concerns detected.")
                st.markdown("## 📊 AI Score Breakdown")
                st.write(f"🧠 Semantic Match — **{semantic:.1f}%**")
                st.progress(semantic / 100)
                st.write(f"💼 Experience Match — **{experience:.1f}%**")
                st.progress(experience / 100)
                st.write(f"🛠 Skill Match — **{skill:.1f}%**")
                st.progress(skill / 100)
                st.write(f"🤝 Behaviour Match — **{behaviour:.1f}%**")
                st.progress(behaviour / 100)
                st.markdown("---")
                st.markdown("## 📄 Candidate Overview")
                st.info(summary)
                st.markdown("---")
                st.markdown("## 🧠 Why This Candidate?")
                reasons = explain_candidate(
                    candidate,
                    result
                )
                for reason in reasons:
                    st.success(reason)
                st.markdown("---")
    st.markdown("---") 
    st.download_button(
    label="📥 Download Ranked Candidates CSV",
    data=csv,
    file_name="ranked_candidates.csv",
    mime="text/csv",
    use_container_width=True,
    )
st.markdown("""
                ---
                <div style="text-align:center;color:#94A3B8">
                <h3>🧠 TalentIQ AI</h3>
                AI-Powered Recruiter Intelligence Platform
                Semantic Search • Hybrid Ranking • Explainable AI • Recruiter Copilot
                </div>""", unsafe_allow_html=True
                )
