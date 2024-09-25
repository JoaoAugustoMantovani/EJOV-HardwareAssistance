import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import LayoutLogin from '../default-login-layout/layout-login';
import './forgot-password.css';

const ForgotPassword: React.FC = () => {
  const [email, setEmail] = useState('');
  const navigate = useNavigate();

  const handleForgotPassword = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    console.log('Email:', email);
    navigate('/reset-password');
  };

  return (
    <LayoutLogin>
      <form className="forgot-password-form" onSubmit={handleForgotPassword}>
        <div className='logo-ejov'>
          <img src="src/assets/LogoEJOV.png" alt="LogoEJOV" />
        </div>
        <label htmlFor="email">Digite seu e-mail:</label>
        <input
          type="email"
          id="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
        <button type="submit" className="forgot-password-button">Enviar</button>
        <div className="forgot-password-links">
          <a href="/login">Voltar para login</a>
        </div>
      </form>
    </LayoutLogin>
  );
};

export default ForgotPassword;