import React from 'react';

const Footer = () => {
  return (
    <footer style={footerStyle}>
      <div>
        <a> <a href="https://sweet-druid-839002.netlify.app/">&copy; 2023 by jagadeeshgouda</a></a>
      </div>
    </footer>
  );
};

const footerStyle = {
  backgroundColor: '#333',
  color: '#fff',
  padding: '10px',
  textAlign: 'center',
  position: 'fixed',
  left: '0',
  bottom: '0',
  width: '100%',
};

export default Footer;
