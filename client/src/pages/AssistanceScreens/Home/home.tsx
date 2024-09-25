// src/pages/Home/home.tsx
import React from 'react';
import NavBar from '../components/nav-bar/nav-bar';
import Container from '../components/container/container';
import Footer from '../components/footer/footer';
import Chatbot from '../components/ChatBot/chatbot';
import './home.css';

const Home: React.FC = () => {
  return (
    <div className="home-layout">
      <NavBar />
      <Container />
      <Chatbot />
      <Footer />
    </div>
  );
};

export default Home;