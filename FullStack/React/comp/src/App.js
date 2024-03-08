import logo from './logo.svg';
import './App.css';
import Name from './component/Name'


function App(props) {
  const colorstyle = {
    color:props.color,
    fontSize:props.font
  }
  return (
    <div style={colorstyle}>
      <Name/>
    </div>
    
  );
}
export default App;