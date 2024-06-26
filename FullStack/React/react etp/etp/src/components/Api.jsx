import React, { useEffect, useState } from 'react';

const PublicApiData = () => {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch('https://jsonplaceholder.typicode.com/todos/1')
     .then(response => response.json())
     .then(data => setData(data))
     .catch(error => console.error(error));
  }, []);

  return (
    <div>
      {data? (
        <div>
          <h2>Public API Data</h2>
          <p>ID: {data.id}</p>
          <p>User ID: {data.userId}</p>
          <p>Title: {data.title}</p>
          <p>Completed: {data.completed? 'Yes' : 'No'}</p>
        </div>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
};

export default PublicApiData;