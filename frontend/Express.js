const express = require('express');
const bcrypt = require('bcryptjs');
const axios = require('axios');

const app = express();
const port = 3000;

// Body Parser Middleware
app.use(express.json());
app.use(express.urlencoded({ extended: false }));

// Register Route
app.post('/register', async (req, res) => {
    try {
        const { username, email, password } = req.body;

        // Hash password
        const hashedPassword = await bcrypt.hash(password, 10);

        // Send registration request to backend
        const response = await axios.post('http://localhost:5000/register', {
            username,
            email,
            password: hashedPassword
        });

        res.json(response.data);
    } catch (error) {
        console.error(error);
        res.status(500).json({ message: 'Internal server error' });
    }
});

app.listen(port, () => console.log(Frontend server running on http://localhost:${port}));