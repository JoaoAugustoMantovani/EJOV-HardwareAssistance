// src/components/chatbot/Chatbot.tsx
import React, { useState, useEffect } from 'react';
import './Chatbot.css';

const Chatbot: React.FC = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState<string[]>([]);
  
  // Abrir e fechar o chat
  const toggleChat = () => {
    setIsOpen(!isOpen);
  };

  // Simular um chat inicial
  const handleSendMessage = (message: string) => {
    setMessages([...messages, message]);
  };

  // Função para limpar as conversas quando o usuário sair/deslogar
  const handleLogout = () => {
    localStorage.removeItem('chatMessages'); // Limpa do localStorage
    setMessages([]); // Limpa o estado
  };

  // Salvando as conversas no localStorage (por usuário)
  useEffect(() => {
    const storedMessages = localStorage.getItem('chatMessages');
    if (storedMessages) {
      setMessages(JSON.parse(storedMessages));
    }
  }, []);

  useEffect(() => {
    localStorage.setItem('chatMessages', JSON.stringify(messages));
  }, [messages]);

  return (
    <div className={`chatbot-container ${isOpen ? 'open' : ''}`}>
      {/* Ícone do Chatbot */}
      {!isOpen && <img src="src/assets/bot.png" alt="Chatbot" className="chatbot-icon" onClick={toggleChat} />}

      {/* Janela do Chat */}
      {isOpen && (
        <div className="chatbot-window">
          <div className="chatbot-header">
            <span>Chatbot</span>
            <button onClick={toggleChat} className="close-btn">X</button>
          </div>
          <div className="chatbot-messages">
            {messages.map((msg, index) => (
              <div key={index} className="chatbot-message">{msg}</div>
            ))}
          </div>
          <div className="chatbot-input">
            <input
              type="text"
              placeholder="Digite sua mensagem..."
              onKeyDown={(e) => {
                if (e.key === 'Enter') {
                  handleSendMessage((e.target as HTMLInputElement).value);
                  (e.target as HTMLInputElement).value = '';
                }
              }}
            />
            <button onClick={() => handleLogout()}>Sair</button>
          </div>
        </div>
      )}
    </div>
  );
};

export default Chatbot;
