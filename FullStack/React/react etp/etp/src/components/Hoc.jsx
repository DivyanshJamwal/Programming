import React from 'react';

const withLogging = (WrappedComponent) => {
  const HOC = (props) => {
    console.log(`Rendering ${WrappedComponent.name}`);
    return <WrappedComponent {...props} />;
  };

  HOC.displayName = `withLogging(${WrappedComponent.name})`;

  return HOC;
};

const MyComponent = ({ name }) => {
  return <div>Hello, {name}!</div>;
};

const LoggedComponent = withLogging(MyComponent);

const Hoc = () => {
  return (
    <div>
      <LoggedComponent name="Alice" />
      <LoggedComponent name="Bob" />
    </div>
  );
};

export default Hoc;