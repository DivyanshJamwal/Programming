import ReactDOM from 'react-dom'


const UserInfo = ({ location }) => {
    const formData = location.state;
    return (
      <div>
        <h1>User Info</h1>
        <p>Name: {formData.name}</p>
        <p>Registration No: {formData.regno}</p>
        <p>Email: {formData.email}</p>
        <p>Password: {formData.password}</p>
      </div>
    );
  };
  
export default Userinfo;