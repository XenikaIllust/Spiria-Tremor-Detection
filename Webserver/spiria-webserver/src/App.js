import React, { Component } from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom';
import { withRouter } from 'react-router';

import SignIn from './components/SignIn/SignIn';
import Homepage from './components/Homepage/Homepage';
import TestsData from './components/TestsData/TestsData';
import TestData from './components/TestData/TestData';

import logo from './logo.svg';
import './App.css';

/*
class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            Edit <code>src/App.js</code> and save to reload.
          </p>
          <a
            className="App-link"
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
          >
            Learn React
          </a>
        </header>
      </div>
    );
  }
}

export default App;
*/

class App extends Component {
  render() {
    return (
      <div>
        <BrowserRouter>
          <Switch>
            <Route exact path="/" component={ Homepage } />
            <Route path="/login" component={ SignIn } />
            <Route path="/tests_data" component={ TestsData } />
            <Route path="/test_data" component={ TestData } />
          </Switch>
        </BrowserRouter>
      </div>
    );
  }
}

export default App;