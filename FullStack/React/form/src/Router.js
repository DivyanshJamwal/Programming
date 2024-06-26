import { BrowserRouter, Route, Switch } from 'react-router-dom';
import App from './App';
import UserInfo from './Userinfo';

const Router = () => {
    return (
      <BrowserRouter>
        <Switch>
          <Route path="/" component={App} exact />
          <Route path="/userinfo" component={UserInfo} />
        </Switch>
      </BrowserRouter>
    );
  };
  
export default Router;