import './App.css';
import logo from './logo.svg';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <div className="logo">
          <img src={logo} alt="Octofit Logo" />
          <h1>Octofit Tracker</h1>
        </div>
        <nav>
          <a href="/">Home</a>
          <a href="/users">Users</a>
          <a href="/activities">Activities</a>
          <a href="/teams">Teams</a>
          <a href="/workouts">Workouts</a>
        </nav>
      </header>
      <main>
        {/* Add routing or main content here */}
      </main>
    </div>
  );
}

export default App;
