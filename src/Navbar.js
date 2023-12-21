import React from 'react';
import { Navbar, Nav } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';


const MyNavbar = () => {
  return (
    <Navbar bg="dark" variant="dark" expand="lg">
      <Navbar.Brand href="#home">BLOGS</Navbar.Brand>
      <Navbar.Toggle aria-controls="basic-navbar-nav" />
      <Navbar.Collapse id="basic-navbar-nav">
        <Nav className="mr-auto">
          <Nav.Link href="http://127.0.0.1:8000/add/">Add-Blog</Nav.Link>
          <Nav.Link href="http://127.0.0.1:8000/changepassword">changepassword</Nav.Link>
          <Nav.Link href="http://127.0.0.1:8000">Logout</Nav.Link>
          
          
        </Nav>/changepassword
        
      </Navbar.Collapse>
    </Navbar>

    
  );
};
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>

export default MyNavbar;
