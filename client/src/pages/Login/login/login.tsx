import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import LayoutLogin from '../default-login-layout/layout-login';
import './login.css';

const Login: React.FC = () => {
  const [login, setLogin] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleLogin = async (event: React.FormEvent) => {
    event.preventDefault();

    try {
      const response = await fetch('http://127.0.0.1:4000/api/user/login', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username: login, password })
      });

      if (!response.ok) {
        throw new Error('Erro na solicitação de login');
      }

      const data = await response.json();

      if (data.message === 'Login successful') {
        console.log('Login bem-sucedido:', data.user);
        navigate('/home');
      } else {
        console.error('Erro de login:', data.message);
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <LayoutLogin>
      <form className="login-form" onSubmit={handleLogin}>
        <div className='logo-ejov'>
          <img src="src/assets/LogoEJOV.png" alt="LogoEJOV" />
        </div>
        <label htmlFor="login">LOGIN:</label>
        <input
          type="text"
          id="login"
          value={login}
          onChange={(e) => setLogin(e.target.value)}
          required
        />
        <label htmlFor="password">SENHA:</label>
        <input
          type="password"
          id="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
        <div className="login-links">
          <a href="/fp">Esqueceu a senha?</a>
        </div>
        <button type="submit" className="login-button">ENTRAR</button>
        <p>
          Não possui uma conta? <a href="/register">Cadastrar conta</a>
        </p>
      </form>
    </LayoutLogin>
  );
};

export default Login;
