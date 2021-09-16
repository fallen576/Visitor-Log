import React, { Component } from 'react'
import './App.css';
import axios from "axios";



class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      logs: []
    };
  }

  componentDidMount() {
    this.refreshLogs();
  }

  refreshLogs = () => {
    axios
      .get("http://localhost:8000/api/logs/")
      .then((res) => this.setState({ logs: res.data }))
      .catch((err) => console.log(err));
  };

  renderLogs() {
    console.log(this.state.logs);
    const logs = this.state.logs;

    return logs.map((log) => (
      <tr>
        <td>{log.first_name}</td>
        <td>{log.last_name}</td>
        <td>{log.email}</td>
        <td>{log.in_time}</td>
      </tr>
    ));
  }


  render() {
    return (
      <div className="log">
        <table className="table">
          <thead>
            <tr>
              <th>First Name</th>
              <th>Last Name</th>
              <th>Email</th>
              <th>In Time</th>
            </tr>
          </thead>
          <tbody>
            {this.renderLogs()}
          </tbody>
        </table>
      </div>
    );
  }
}

export default App;
