import React, { useState } from 'react';

const ControlledForm = () => {
  const [formState, setFormState] = useState({
    name: '',
    email: '',
    message: '',
  });

  const handleInputChange = (event) => {
    setFormState({
     ...formState,
      [event.target.name]: event.target.value,
    });
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log('Form submitted:', formState);
  };

  return (
    <form onSubmit={handleSubmit}>
      <label htmlFor="name">Name:</label>
      <input
        type="text"
        name="name"
        value={formState.name}
        onChange={handleInputChange}
      />

      <label htmlFor="email">Email:</label>
      <input
        type="email"
        name="email"
        value={formState.email}
        onChange={handleInputChange}
      />

      <label htmlFor="message">Message:</label>
      <textarea
        name="message"
        value={formState.message}
        onChange={handleInputChange}
      />

      <button type="submit">Submit</button>
    </form>
  );
};

export default ControlledForm;