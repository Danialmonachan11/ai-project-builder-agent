import React, { useState } from 'react';
import axios from 'axios';
import { FileText, Loader2, Download, Folder, FileCode, CheckCircle } from 'lucide-react';

function App() {
    const [jobDescription, setJobDescription] = useState('');
    const [isGenerating, setIsGenerating] = useState(false);
    const [projectData, setProjectData] = useState(null);
    const [error, setError] = useState(null);

    const handleGenerate = async () => {
        if (!jobDescription.trim()) return;

        setIsGenerating(true);
        setError(null);

        try {
            const response = await axios.post('/api/generate_project', {
                text: jobDescription
            });
            setProjectData(response.data);
        } catch (err) {
            setError(err.message || 'Failed to generate project');
        } finally {
            setIsGenerating(false);
        }
    };

    const handleDownload = () => {
        if (!projectData) return;
        window.location.href = `http://localhost:8000/download/${projectData.project_id}`;
    };

    return (
        <div className="container">
            <header className="header">
                <h1>Project Builder Agent</h1>
                <p>Turn any Job Description into a full-stack AI project in seconds.</p>
            </header>

            <div className="grid">
                <div className="card">
                    <h2 style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginTop: 0 }}>
                        <FileText size={24} className="text-accent" />
                        Job Description
                    </h2>
                    <p className="text-secondary" style={{ marginBottom: '1rem' }}>
                        Paste the full job description here. The agent will analyze requirements and build a matching project.
                    </p>
                    <textarea
                        value={jobDescription}
                        onChange={(e) => setJobDescription(e.target.value)}
                        placeholder="e.g. We are looking for a Computer Vision Engineer to build a face recognition system..."
                    />
                    <button
                        className="btn"
                        onClick={handleGenerate}
                        disabled={isGenerating || !jobDescription.trim()}
                        style={{ width: '100%', display: 'flex', justifyContent: 'center', alignItems: 'center', gap: '0.5rem' }}
                    >
                        {isGenerating ? (
                            <>
                                <Loader2 className="animate-spin" size={20} />
                                Building Project...
                            </>
                        ) : (
                            'Generate Project'
                        )}
                    </button>
                    {error && (
                        <div style={{ marginTop: '1rem', color: '#ef4444', padding: '0.5rem', backgroundColor: 'rgba(239, 68, 68, 0.1)', borderRadius: '0.5rem' }}>
                            {error}
                        </div>
                    )}
                </div>

                <div className="card">
                    <h2 style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginTop: 0 }}>
                        {projectData ? <CheckCircle size={24} color="var(--success)" /> : <Folder size={24} />}
                        Project Preview
                    </h2>

                    {!projectData ? (
                        <div style={{ height: '200px', display: 'flex', alignItems: 'center', justifyContent: 'center', color: 'var(--text-secondary)', flexDirection: 'column', gap: '1rem' }}>
                            <FileCode size={48} style={{ opacity: 0.2 }} />
                            <p>Generated project structure will appear here.</p>
                        </div>
                    ) : (
                        <div>
                            <div style={{ marginBottom: '1.5rem' }}>
                                <div style={{ display: 'flex', gap: '0.5rem', marginBottom: '0.5rem', flexWrap: 'wrap' }}>
                                    <span className="badge">{projectData.project_type}</span>
                                    <span className="badge" style={{ color: 'var(--text-primary)', backgroundColor: 'var(--bg-primary)' }}>
                                        {(projectData.analysis.domain || '').toUpperCase()}
                                    </span>
                                    <span className="badge" style={{ backgroundColor: 'rgba(34, 197, 94, 0.1)', color: 'var(--success)' }}>
                                        📁 {projectData.project_name}
                                    </span>
                                </div>
                                <h3 style={{ margin: '0.5rem 0' }}>{projectData.analysis.business_goal}</h3>
                                <p className="text-secondary" style={{ fontSize: '0.9rem', marginBottom: '1rem' }}>
                                    Tech Stack: {(projectData.analysis.tech_stack || []).join(', ')}
                                </p>

                                {projectData.scenario && (
                                    <div style={{
                                        backgroundColor: 'rgba(59, 130, 246, 0.1)',
                                        padding: '1rem',
                                        borderRadius: '0.5rem',
                                        borderLeft: '3px solid var(--accent)'
                                    }}>
                                        <h4 style={{ margin: '0 0 0.5rem 0', color: 'var(--accent)', fontSize: '0.95rem' }}>
                                            💡 {projectData.scenario.title}
                                        </h4>
                                        <p style={{ fontSize: '0.85rem', margin: '0.3rem 0', color: 'var(--text-secondary)' }}>
                                            <strong>Problem:</strong> {projectData.scenario.problem.substring(0, 120)}...
                                        </p>
                                        <p style={{ fontSize: '0.85rem', margin: '0.3rem 0', color: 'var(--success)' }}>
                                            <strong>ROI:</strong> {projectData.scenario.roi}
                                        </p>
                                    </div>
                                )}
                            </div>

                            <div className="file-tree" style={{ backgroundColor: 'var(--bg-primary)', padding: '1rem', borderRadius: '0.5rem', marginBottom: '1.5rem' }}>
                                <div className="file-item folder"><Folder size={16} /> src/</div>
                                <div className="file-item" style={{ paddingLeft: '1.5rem' }}><FileCode size={16} /> agents/</div>
                                <div className="file-item" style={{ paddingLeft: '1.5rem' }}><FileCode size={16} /> api/</div>
                                <div className="file-item" style={{ paddingLeft: '1.5rem' }}><FileCode size={16} /> core/</div>
                                <div className="file-item folder"><Folder size={16} /> data/</div>
                                <div className="file-item" style={{ paddingLeft: '1.5rem' }}><FileCode size={16} /> sample_data</div>
                                <div className="file-item folder"><Folder size={16} /> deployments/</div>
                                <div className="file-item" style={{ paddingLeft: '1.5rem' }}><FileCode size={16} /> kubernetes/</div>
                                <div className="file-item"><FileCode size={16} /> PROJECT_SCENARIO.md</div>
                                <div className="file-item"><FileCode size={16} /> README.md</div>
                                <div className="file-item"><FileCode size={16} /> ARCHITECTURE.md</div>
                            </div>

                            <button
                                className="btn"
                                style={{ width: '100%', display: 'flex', justifyContent: 'center', alignItems: 'center', gap: '0.5rem' }}
                                onClick={handleDownload}
                            >
                                <Download size={20} />
                                Download {projectData.project_name}.zip
                            </button>
                        </div>
                    )}
                </div>
            </div>
        </div>
    )
}

export default App
