import React from 'react';
import Axios from 'axios';
import { Button, Card } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css'
import '../App.css';


class Post extends React.Component {
    state = {
        posts: []
    };

    componentDidMount() {
        this.fetchPosts();
    }

    fetchPosts() {

        fetch('http://127.0.0.1:8000/posts/')
        .then(response => response.json())
        .then(data => this.setState({ posts: data }))
        .catch(err => console.log(err))

    }

    render() {
        return (
            <div className="container center">
                {this.state.posts.map(post => {
                    return (
                        <Card key={ post.id } className="ml-5 mr-5 mb-5">
                            <Card.Img variant="top" src={ post.image } width="300px" height="300px" />
                            <Card.Title>{ post.user }</Card.Title>
                            <Card.Text>{ post.content }</Card.Text>
                            <Card.Link href={ post.absolute_url }>Post'a git</Card.Link>
                        </Card>
                    );
                })}
            </div>
        )
    }

}





export default Post;
