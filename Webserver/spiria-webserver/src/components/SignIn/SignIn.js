import React, { Component } from 'react';
import { Form, Button } from 'react-bootstrap';
import Header from '../Header/Header';
import "./SignIn.css";

class SignIn extends Component {
    constructor(props) {
        super(props);

        this.state = {
            email: "",
            password: ""
        };
    }

    render() {
        return (
            <div class="container-fluid">
                <Header />
                <Form>
                    <Form.Group controlId="formEmail">
                        <Form.Label>Email Address</Form.Label>
                        <Form.Control type="email" placeholder="Enter email" />
                    </Form.Group>

                    <Form.Group controlId="formPassword">
                        <Form.Label>Password</Form.Label>
                        <Form.Control type="password" placeholder="Enter Password" />
                    </Form.Group>
                </Form>
                <Button variant="primary" type="submit">
                    Submit
                </Button>
            </div>
        );
    }
}

export default SignIn;
