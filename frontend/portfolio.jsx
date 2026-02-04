import React, { useState, useEffect, useRef } from 'react';
import { Send, Sparkles, Terminal, Code, Award, Brain, MessageSquare, X, ChevronDown } from 'lucide-react';

export default function AIPortfolio() {
  const [messages, setMessages] = useState([]);
  const [inputValue, setInputValue] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [chatOpen, setChatOpen] = useState(false);
  const [flippedCards, setFlippedCards] = useState({});
  const messagesEndRef = useRef(null);
  const [apiEndpoint, setApiEndpoint] = useState('');
  const [showApiInput, setShowApiInput] = useState(true);

  // Auto-scroll chat to bottom
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  // Sample projects data - customize with your actual projects
  const projects = [
    {
      id: 1,
      title: "LLM-Powered Chatbot",
      tools: ["OpenAI API", "LangChain", "FastAPI", "React"],
      image: "🤖",
      description: "Built an intelligent conversational AI using GPT-4 with custom knowledge base integration. Implemented RAG (Retrieval Augmented Generation) for domain-specific responses with 95% accuracy.",
      achievements: "Won 1st place at TechHack 2024",
      github: "#",
      demo: "#"
    },
    {
      id: 2,
      title: "Document Intelligence System",
      tools: ["Python", "OCR", "NLP", "Vector DB"],
      image: "📄",
      description: "Developed an AI system to extract, analyze, and summarize insights from legal documents. Utilized transformer models for entity recognition and classification with 92% F1 score.",
      achievements: "2nd prize at AI Innovation Summit",
      github: "#",
      demo: "#"
    },
    {
      id: 3,
      title: "Real-time Sentiment Analyzer",
      tools: ["BERT", "PyTorch", "FastAPI", "WebSocket"],
      image: "💭",
      description: "Created a real-time sentiment analysis dashboard for social media monitoring. Processes 10k+ messages per minute with custom fine-tuned BERT model achieving 89% accuracy.",
      achievements: "Best AI Project - HackFest 2024",
      github: "#",
      demo: "#"
    },
    {
      id: 4,
      title: "AI Code Assistant",
      tools: ["Code Llama", "VSCode Extension", "Node.js"],
      image: "💻",
      description: "Built an intelligent code completion and bug detection tool. Integrated with popular IDEs, providing context-aware suggestions and automated code review capabilities.",
      achievements: "Finalist - DevAI Hackathon",
      github: "#",
      demo: "#"
    }
  ];

  const skills = [
    { category: "LLMs & APIs", items: ["GPT-4", "Claude", "LangChain", "OpenAI API", "Anthropic API"] },
    { category: "ML/DL", items: ["PyTorch", "TensorFlow", "Hugging Face", "BERT", "Fine-tuning"] },
    { category: "Backend", items: ["FastAPI", "Python", "REST APIs", "WebSocket", "Docker"] },
    { category: "Vector & Data", items: ["Pinecone", "Chroma", "PostgreSQL", "Redis"] },
    { category: "Frontend", items: ["React", "JavaScript", "Gradio", "Streamlit"] }
  ];

  const handleCardFlip = (id) => {
    setFlippedCards(prev => ({
      ...prev,
      [id]: !prev[id]
    }));
  };

  const handleSendMessage = async () => {
    if (!inputValue.trim() || !apiEndpoint) return;

    const userMessage = inputValue.trim();
    setInputValue('');
    setMessages(prev => [...prev, { role: 'user', content: userMessage }]);
    setIsLoading(true);

    try {
      // Replace this URL with your actual FastAPI endpoint
      const response = await fetch(`${apiEndpoint}/chat`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: userMessage })
      });

      if (!response.ok) throw new Error('Failed to get response');

      const data = await response.json();
      setMessages(prev => [...prev, { 
        role: 'assistant', 
        content: data.response || data.message || 'I received your question!'
      }]);
    } catch (error) {
      setMessages(prev => [...prev, { 
        role: 'assistant', 
        content: 'Sorry, I encountered an error. Please make sure your API endpoint is running and accessible.'
      }]);
      console.error('Chat error:', error);
    } finally {
      setIsLoading(false);
    }
  };

  const suggestedQuestions = [
    "How confident is she with LLMs?",
    "What are her strongest technical skills?",
    "Tell me about her hackathon achievements",
    "What projects has she built with AI?"
  ];

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-950 via-purple-950 to-slate-900 text-white overflow-x-hidden">
      {/* Animated background particles */}
      <div className="fixed inset-0 overflow-hidden pointer-events-none">
        {[...Array(30)].map((_, i) => (
          <div
            key={i}
            className="absolute w-1 h-1 bg-purple-400 rounded-full animate-float"
            style={{
              left: `${Math.random() * 100}%`,
              top: `${Math.random() * 100}%`,
              animationDelay: `${Math.random() * 5}s`,
              animationDuration: `${15 + Math.random() * 10}s`,
              opacity: 0.3
            }}
          />
        ))}
      </div>

      {/* Hero Section */}
      <div className="relative z-10 container mx-auto px-6 pt-20 pb-12">
        <div className="text-center mb-16 animate-fadeIn">
          <div className="inline-flex items-center gap-2 px-4 py-2 bg-purple-500/20 rounded-full border border-purple-400/30 mb-6 backdrop-blur-sm">
            <Sparkles className="w-4 h-4 text-purple-300" />
            <span className="text-sm font-medium text-purple-200">AI Engineer • Hackathon Winner</span>
          </div>
          
          <h1 className="text-6xl md:text-7xl font-bold mb-6 bg-gradient-to-r from-purple-200 via-pink-200 to-purple-300 bg-clip-text text-transparent animate-shimmer">
            Your Name
          </h1>
          
          <p className="text-xl md:text-2xl text-purple-100 mb-4 font-light">
            Building the Future with Artificial Intelligence
          </p>
          
          <p className="text-purple-300 max-w-2xl mx-auto mb-8">
            9 months of transforming ideas into intelligent solutions • Multiple hackathon victories • 
            Specializing in LLMs, NLP, and AI-powered applications
          </p>

          <div className="flex gap-4 justify-center flex-wrap">
            <button
              onClick={() => setChatOpen(true)}
              className="px-6 py-3 bg-gradient-to-r from-purple-600 to-pink-600 rounded-full font-semibold hover:shadow-lg hover:shadow-purple-500/50 transition-all duration-300 hover:scale-105 flex items-center gap-2"
            >
              <Brain className="w-5 h-5" />
              Ask AI About Me
            </button>
            <a
              href="#projects"
              className="px-6 py-3 bg-white/10 backdrop-blur-sm rounded-full font-semibold border border-white/20 hover:bg-white/20 transition-all duration-300 flex items-center gap-2"
            >
              <Code className="w-5 h-5" />
              View Projects
            </a>
          </div>
        </div>

        {/* Skills Grid */}
        <div className="mb-20">
          <h2 className="text-3xl font-bold text-center mb-10 flex items-center justify-center gap-3">
            <Terminal className="w-8 h-8 text-purple-400" />
            Technical Arsenal
          </h2>
          <div className="grid md:grid-cols-5 gap-4 max-w-6xl mx-auto">
            {skills.map((skillGroup, idx) => (
              <div
                key={idx}
                className="bg-white/5 backdrop-blur-md border border-purple-500/20 rounded-xl p-6 hover:bg-white/10 transition-all duration-300 hover:scale-105 hover:shadow-lg hover:shadow-purple-500/20"
                style={{ animationDelay: `${idx * 100}ms` }}
              >
                <h3 className="text-purple-300 font-semibold mb-3 text-sm uppercase tracking-wider">
                  {skillGroup.category}
                </h3>
                <div className="flex flex-wrap gap-2">
                  {skillGroup.items.map((skill, i) => (
                    <span
                      key={i}
                      className="text-xs px-2 py-1 bg-purple-500/20 rounded-md text-purple-100 border border-purple-400/20"
                    >
                      {skill}
                    </span>
                  ))}
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Projects Section */}
        <div id="projects" className="mb-20">
          <h2 className="text-3xl font-bold text-center mb-10 flex items-center justify-center gap-3">
            <Award className="w-8 h-8 text-purple-400" />
            Award-Winning Projects
          </h2>
          
          <div className="grid md:grid-cols-2 gap-6 max-w-6xl mx-auto">
            {projects.map((project, idx) => (
              <div
                key={project.id}
                className="relative h-80 perspective-1000"
                style={{ animationDelay: `${idx * 150}ms` }}
              >
                <div
                  className={`relative w-full h-full transition-transform duration-700 transform-style-3d cursor-pointer ${
                    flippedCards[project.id] ? 'rotate-y-180' : ''
                  }`}
                  onClick={() => handleCardFlip(project.id)}
                >
                  {/* Front of card */}
                  <div className="absolute inset-0 backface-hidden bg-gradient-to-br from-purple-900/40 to-pink-900/40 backdrop-blur-md border border-purple-500/30 rounded-2xl p-8 hover:shadow-2xl hover:shadow-purple-500/30 transition-all">
                    <div className="flex flex-col h-full">
                      <div className="text-6xl mb-4">{project.image}</div>
                      <h3 className="text-2xl font-bold mb-3 text-purple-100">{project.title}</h3>
                      <div className="flex flex-wrap gap-2 mb-4">
                        {project.tools.slice(0, 3).map((tool, i) => (
                          <span
                            key={i}
                            className="px-3 py-1 bg-purple-500/30 rounded-full text-xs font-medium text-purple-200 border border-purple-400/30"
                          >
                            {tool}
                          </span>
                        ))}
                        {project.tools.length > 3 && (
                          <span className="px-3 py-1 bg-purple-500/30 rounded-full text-xs font-medium text-purple-200 border border-purple-400/30">
                            +{project.tools.length - 3}
                          </span>
                        )}
                      </div>
                      <div className="mt-auto">
                        <p className="text-purple-300 text-sm flex items-center gap-2">
                          <Sparkles className="w-4 h-4" />
                          Click to see details
                        </p>
                      </div>
                    </div>
                  </div>

                  {/* Back of card */}
                  <div className="absolute inset-0 backface-hidden rotate-y-180 bg-gradient-to-br from-pink-900/40 to-purple-900/40 backdrop-blur-md border border-pink-500/30 rounded-2xl p-8 overflow-y-auto">
                    <h3 className="text-xl font-bold mb-4 text-pink-100">{project.title}</h3>
                    <p className="text-purple-200 text-sm mb-4 leading-relaxed">
                      {project.description}
                    </p>
                    <div className="bg-green-500/20 border border-green-400/30 rounded-lg p-3 mb-4">
                      <p className="text-green-200 text-sm font-semibold flex items-center gap-2">
                        <Award className="w-4 h-4" />
                        {project.achievements}
                      </p>
                    </div>
                    <div className="flex flex-wrap gap-2 mb-4">
                      {project.tools.map((tool, i) => (
                        <span
                          key={i}
                          className="px-2 py-1 bg-purple-500/30 rounded-md text-xs text-purple-200 border border-purple-400/20"
                        >
                          {tool}
                        </span>
                      ))}
                    </div>
                    <div className="flex gap-3 mt-auto">
                      <a
                        href={project.github}
                        className="px-4 py-2 bg-white/10 rounded-lg text-sm hover:bg-white/20 transition-colors"
                        onClick={(e) => e.stopPropagation()}
                      >
                        GitHub
                      </a>
                      <a
                        href={project.demo}
                        className="px-4 py-2 bg-purple-500/30 rounded-lg text-sm hover:bg-purple-500/50 transition-colors"
                        onClick={(e) => e.stopPropagation()}
                      >
                        Live Demo
                      </a>
                    </div>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* CTA to Chat */}
        <div className="text-center py-12 bg-gradient-to-r from-purple-900/30 to-pink-900/30 rounded-3xl border border-purple-500/20 backdrop-blur-sm">
          <Brain className="w-16 h-16 mx-auto mb-4 text-purple-300" />
          <h3 className="text-2xl font-bold mb-3">Want to Know More?</h3>
          <p className="text-purple-200 mb-6 max-w-xl mx-auto">
            Ask my AI assistant anything about my projects, skills, or experience. 
            It's powered by my custom knowledge base!
          </p>
          <button
            onClick={() => setChatOpen(true)}
            className="px-8 py-4 bg-gradient-to-r from-purple-600 to-pink-600 rounded-full font-semibold hover:shadow-lg hover:shadow-purple-500/50 transition-all duration-300 hover:scale-105 flex items-center gap-2 mx-auto"
          >
            <MessageSquare className="w-5 h-5" />
            Start Conversation
          </button>
        </div>
      </div>

      {/* Chat Interface */}
      {chatOpen && (
        <div className="fixed inset-0 bg-black/50 backdrop-blur-sm z-50 flex items-center justify-center p-4 animate-fadeIn">
          <div className="bg-slate-900 border border-purple-500/30 rounded-3xl w-full max-w-2xl h-[600px] flex flex-col shadow-2xl shadow-purple-500/20 animate-slideUp">
            {/* Chat Header */}
            <div className="bg-gradient-to-r from-purple-600 to-pink-600 p-6 rounded-t-3xl flex justify-between items-center">
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 bg-white/20 rounded-full flex items-center justify-center">
                  <Brain className="w-6 h-6" />
                </div>
                <div>
                  <h3 className="font-bold text-lg">AI Portfolio Assistant</h3>
                  <p className="text-sm text-purple-100">Ask me anything about my work!</p>
                </div>
              </div>
              <button
                onClick={() => setChatOpen(false)}
                className="w-8 h-8 hover:bg-white/20 rounded-full flex items-center justify-center transition-colors"
              >
                <X className="w-5 h-5" />
              </button>
            </div>

            {/* API Configuration (if not set) */}
            {showApiInput && !apiEndpoint && (
              <div className="p-6 bg-purple-900/20 border-b border-purple-500/20">
                <p className="text-sm text-purple-200 mb-3">
                  <strong>Setup Required:</strong> Enter your FastAPI endpoint URL
                </p>
                <div className="flex gap-2">
                  <input
                    type="text"
                    placeholder="https://your-api.com"
                    className="flex-1 px-4 py-2 bg-slate-800 border border-purple-500/30 rounded-lg focus:outline-none focus:border-purple-400"
                    onKeyDown={(e) => {
                      if (e.key === 'Enter') {
                        setApiEndpoint(e.target.value);
                        setShowApiInput(false);
                      }
                    }}
                  />
                  <button
                    onClick={(e) => {
                      const input = e.target.previousSibling;
                      setApiEndpoint(input.value);
                      setShowApiInput(false);
                    }}
                    className="px-4 py-2 bg-purple-600 rounded-lg hover:bg-purple-700 transition-colors"
                  >
                    Connect
                  </button>
                </div>
              </div>
            )}

            {/* Messages Area */}
            <div className="flex-1 overflow-y-auto p-6 space-y-4">
              {messages.length === 0 && (
                <div className="text-center py-8">
                  <Brain className="w-16 h-16 mx-auto mb-4 text-purple-400 opacity-50" />
                  <p className="text-purple-300 mb-6">Try asking me:</p>
                  <div className="grid gap-2">
                    {suggestedQuestions.map((q, i) => (
                      <button
                        key={i}
                        onClick={() => {
                          setInputValue(q);
                          handleSendMessage();
                        }}
                        className="px-4 py-3 bg-purple-500/20 hover:bg-purple-500/30 rounded-lg text-sm text-left transition-colors border border-purple-400/20"
                      >
                        {q}
                      </button>
                    ))}
                  </div>
                </div>
              )}

              {messages.map((msg, idx) => (
                <div
                  key={idx}
                  className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'} animate-fadeIn`}
                >
                  <div
                    className={`max-w-[80%] px-4 py-3 rounded-2xl ${
                      msg.role === 'user'
                        ? 'bg-gradient-to-r from-purple-600 to-pink-600 text-white'
                        : 'bg-slate-800 border border-purple-500/20 text-purple-100'
                    }`}
                  >
                    {msg.content}
                  </div>
                </div>
              ))}

              {isLoading && (
                <div className="flex justify-start animate-fadeIn">
                  <div className="bg-slate-800 border border-purple-500/20 px-4 py-3 rounded-2xl">
                    <div className="flex gap-2">
                      <div className="w-2 h-2 bg-purple-400 rounded-full animate-bounce" style={{ animationDelay: '0ms' }} />
                      <div className="w-2 h-2 bg-purple-400 rounded-full animate-bounce" style={{ animationDelay: '150ms' }} />
                      <div className="w-2 h-2 bg-purple-400 rounded-full animate-bounce" style={{ animationDelay: '300ms' }} />
                    </div>
                  </div>
                </div>
              )}

              <div ref={messagesEndRef} />
            </div>

            {/* Input Area */}
            <div className="p-6 border-t border-purple-500/20">
              <div className="flex gap-2">
                <input
                  type="text"
                  value={inputValue}
                  onChange={(e) => setInputValue(e.target.value)}
                  onKeyDown={(e) => e.key === 'Enter' && handleSendMessage()}
                  placeholder={apiEndpoint ? "Ask about projects, skills, experience..." : "Connect your API first..."}
                  disabled={!apiEndpoint}
                  className="flex-1 px-4 py-3 bg-slate-800 border border-purple-500/30 rounded-xl focus:outline-none focus:border-purple-400 disabled:opacity-50"
                />
                <button
                  onClick={handleSendMessage}
                  disabled={!inputValue.trim() || isLoading || !apiEndpoint}
                  className="px-6 py-3 bg-gradient-to-r from-purple-600 to-pink-600 rounded-xl hover:shadow-lg hover:shadow-purple-500/50 transition-all disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-2"
                >
                  <Send className="w-5 h-5" />
                </button>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Floating Chat Button */}
      {!chatOpen && (
        <button
          onClick={() => setChatOpen(true)}
          className="fixed bottom-8 right-8 w-16 h-16 bg-gradient-to-r from-purple-600 to-pink-600 rounded-full shadow-2xl shadow-purple-500/50 flex items-center justify-center hover:scale-110 transition-transform z-40 animate-pulse"
        >
          <MessageSquare className="w-7 h-7" />
        </button>
      )}

      <style jsx>{`
        @keyframes float {
          0%, 100% { transform: translateY(0px); }
          50% { transform: translateY(-20px); }
        }
        @keyframes fadeIn {
          from { opacity: 0; }
          to { opacity: 1; }
        }
        @keyframes slideUp {
          from { transform: translateY(20px); opacity: 0; }
          to { transform: translateY(0); opacity: 1; }
        }
        @keyframes shimmer {
          0% { background-position: -200% center; }
          100% { background-position: 200% center; }
        }
        .animate-float { animation: float ease-in-out infinite; }
        .animate-fadeIn { animation: fadeIn 0.5s ease-out; }
        .animate-slideUp { animation: slideUp 0.4s ease-out; }
        .animate-shimmer { 
          background-size: 200% auto;
          animation: shimmer 3s linear infinite;
        }
        .perspective-1000 { perspective: 1000px; }
        .transform-style-3d { transform-style: preserve-3d; }
        .backface-hidden { backface-visibility: hidden; }
        .rotate-y-180 { transform: rotateY(180deg); }
      `}</style>
    </div>
  );
}
