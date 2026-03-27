const express = require('express');
const path = require('path');

const app = express();

app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(express.static('public'))

app.get('/', (req, res) => {
    // res.json({
    //     msg: 'Hello!'
    // });

    res.send(req.rawHeaders);
})

app.post('/contact', (req, res) => {
    // res.send(req.header('Content-Type'))

    if (!req.body.name) {
        return res.status(400).json('Name is required.');
    }

    return res.status(201).json(`Welcome, ${req.body.name}!`);
})

app.post('/login', (req, res) => {
    if (!req.header('x-auth-token')) {
        return res.status(400).send('No token.');
    }

    if (req.header('x-auth-token') !== 'a1234') {
        return res.status(401).send('Unauthorized.');
    }

    res.send('Logged in successfully!');
})

app.put('/post/:id', (req, res) => {
    res.json({
        id: req.params.id,
        title: req.body.title
    });
})

app.delete('/category/:id', (req, res) => {
    res.json({
        msg: `Category ${req.params.id} deleted successfully`
    });
})

app.listen(5000, () => console.log('Server started on 5000'))
