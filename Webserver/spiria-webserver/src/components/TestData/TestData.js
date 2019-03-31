import React, { Component } from 'react';
import Header from '../Header/Header';
//import { connect } from 'react-redux';

class TestData extends Component {
    render() {
        return(
            <div>
                <Header />
                <p>
                    Testdata.
                </p>
            </div>
        );
    }
}

export default TestData;