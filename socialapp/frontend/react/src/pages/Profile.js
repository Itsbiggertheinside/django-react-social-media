import React from 'react';
import Post from '../partials/Post.js'
import Menu from '../partials/Menu.js'
import { Container, Row, Col } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../App.css';

class ProfilePage extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    return(
      <div className="mt-5">
        <Container>
          <Row>
            <Col xs="12">
              <Menu />
            </Col>
            <Col xs="12">
              <Post />
            </Col>
          </Row>
        </Container>
      </div>
    )
  }

}


export default ProfilePage;
