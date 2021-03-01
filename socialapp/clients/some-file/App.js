import React from 'react';
import HomePage from './pages/Home.js';
import { Container, Row, Col } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';
import { BrowserRouter as Router, Switch, Route, Link, Redirect } from 'react-router-dom';

class App extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    return(
      <Router>
        <Switch>
          <Route exact path="/" component={ HomePage }></Route>
        </Switch>
      </Router>
    )
  }

}


export default App;
