import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import './index.css';
import Footers from "./Footers";
import reportWebVitals from './reportWebVitals';

import { BrowserRouter, Routes, Route } from "react-router-dom";

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<App />} />
        <Route path="Footers" element={<Footers/>}/>
       
        
      </Routes>
    </BrowserRouter>
  </React.StrictMode>,
);

reportWebVitals();
