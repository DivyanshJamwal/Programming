import React, { Component } from 'react';

class Timer extends Component {
  constructor(props) {
    super(props);
    this.state = {
      time: 60,
      isRunning: false
    };
  }

  componentDidMount() {
    this.timerID = setInterval(() => this.tick(), 1000);
  }

  componentWillUnmount() {
    clearInterval(this.timerID);
  }

  tick() {
    if (this.state.isRunning) {
      this.setState((prevState) => ({
        time: prevState.time - 1
      }));
    }
  }

  handleStartStopClick = () => {
    this.setState((prevState) => ({
      isRunning: !prevState.isRunning
    }));
  };

  handleResetClick = () => {
    this.setState({
      time: 0,
      isRunning: false
    });
  };

  render() {
    return (
      <div className="timer">
        <h2>Timer: {this.state.time} seconds</h2>
        <div className="buttons">
          <button onClick={this.handleStartStopClick}>
            {this.state.isRunning ? 'Stop' : 'Start'}
          </button>
          <button onClick={this.handleResetClick}>Reset</button>
        </div>
      </div>
    );
  }
}

function TimerComp() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Interactive Timer</h1>
        <h3>Divyansh Jamwal : 12114805</h3>
        <Timer />
      </header>
    </div>
  );
}

export default TimerComp;