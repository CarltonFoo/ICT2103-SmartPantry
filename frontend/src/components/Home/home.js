import { React,useState,useEffect } from 'react';
import ReactDOM from 'react-dom';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
import { Button, Card, Col, Row } from "antd";

import ArticleList from '../ExampleList/ArticleList';

const Home = () => {
  const [articles, setArticles] = useState([]);

  // Modify the current state by setting the new data to
  // the response from the backend
  useEffect(()=>{
    fetch('http://localhost:5000/allarticles',{
      'methods':'GET',
      headers : {
        'Content-Type':'application/json'
      }
    }
    )
    .then(response => response.json())
    .then(response => setArticles(response))
    .catch(error => console.log(error))
  },[])

  return (
    <div class="m-auto w-11/12">
        
      <div class="text-2xl font-bold my-6">
        Connecting a React Frontend to a Flask Backend.
      </div>

      <ArticleList 
        articles={articles} 
      />

    </div>
  );
}

export default Home;
