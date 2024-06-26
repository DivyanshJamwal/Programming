const express = require('express');
const nodemailer = require('nodemailer');
const bodyParser = require('body-parser');
const multer = require('multer');

const app = express();
const PORT = process.env.PORT || 3000;

// Multer configuration for file uploads
const upload = multer({ dest: 'uploads/' });

// Body parser middleware
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

// POST route to send email with attachment
app.post('/', upload.single('attachment'), (req, res) => {
  const { email, subject, message } = req.body;
  const attachment = req.file;

  // Create a transporter object using SMTP transport
  const transporter = nodemailer.createTransport({
    service: 'Gmail',
    auth: {
      user: 'your-email@gmail.com',
      pass: 'your-password'
    }
  });

  // Define email options
  const mailOptions = {
    from: 'your-email@gmail.com',
    to: email,
    subject: subject,
    text: message,
    attachments: attachment ? [{ filename: attachment.originalname, path: attachment.path }] : []
  };

  // Send email
  transporter.sendMail(mailOptions, (error, info) => {
    if (error) {
      console.error('Error occurred:', error);
      res.status(500).send('Error sending email');
    } else {
      console.log('Email sent:', info.response);
      res.status(200).send('Email sent successfully');
    }
  });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});