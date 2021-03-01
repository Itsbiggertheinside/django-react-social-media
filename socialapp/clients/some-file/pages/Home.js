import React from 'react';
import Post from '../partials/Post.js'
import Menu from '../partials/Menu.js'
import { Container, Row, Col } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../App.css';
import { BrowserRouter as Router, Switch, Route, Link, Redirect } from 'react-router-dom';

class HomePage extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    return(
      <div className="mt-5">
        <Container>
          <Row>
            <Col md="4">
              <Menu />
            </Col>
            <Col md="8">
              <Post />
            </Col>
          </Row>
        </Container>
      </div>
    )
  }

}


export default HomePage;
