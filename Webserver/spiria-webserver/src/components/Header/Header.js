import React from 'react';
import ReactDOM from 'react-dom';
import { Navbar } from 'react-bootstrap';

class Header extends React.Component {
    render() {
        return (
            <div className="container-fluid">
                <Navbar bg="dark" variant="dark" expand="lg">
                    <Navbar.Brand href="/">Spiria Gateway</Navbar.Brand>
                </Navbar>
            </div>
        );
    }
}

export default Header;