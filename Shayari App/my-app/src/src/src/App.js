import React, { useState } from 'react';
import './App.css';

const App = () => {
  const [keyword, setKeyword] = useState('');
  const [joke, setJoke] = useState('');

  const handleKeywordChange = (e) => {
    setKeyword(e.target.value);
  };

  const handleGenerateJoke = () => {
    fetch(`https://clumsy-boot-goat.cyclic.app/jokes?keyword=${keyword}`)
      .then((response) => response.json())
      .then((data) => setJoke(data.joke))
      .catch((error) => console.log(error));
  };

  return (
    <div className="container">
      <div className="background"></div>
      <div className="content">
        <h1>Joke Generator</h1>
        <div className="search-container">
          <input
            type="text"
            placeholder="Enter a keyword..."
            value={keyword}
            onChange={handleKeywordChange}
          />
          <button onClick={handleGenerateJoke}>Generate Joke</button>
        </div>
        {joke && (
          <div className="joke-container">
            <h2>Generated Joke:</h2>
            <p>{joke}</p>
          </div>
        )}
      </div>
    </div>
  );
};

export default App;
