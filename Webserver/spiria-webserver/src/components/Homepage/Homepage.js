import React, { Component } from 'react';
import { Button } from 'react-bootstrap';
import Header from '../Header/Header'
// import { connect } from 'react-redux';

class Homepage extends Component {
    render() {
        return(
            <div>
                <Header />
                <p>
                    Welcome to the Spiria Gateway.
                </p>
                <Button variant="primary">
                    See The Test Data
                </Button>
            </div>
        );
    }
}

export default Homepage;