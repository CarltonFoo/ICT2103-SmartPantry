import './App.css';
import "antd/dist/antd.css";
import "./assets/css/font.css";
import { useState,useEffect } from 'react'
import {
  BrowserRouter as Router,
  Switch,
  Route,
} from "react-router-dom";

import Navbar from './components/Navbar/Navbar';
import Home from './components/Home/Home';
import Groceries from './components/Groceries/Groceries';
import Recipes from './components/Recipes/Recipes';
import Inventory from './components/Inventory/Inventory';


function App() {
  return (
    <div>
      <Router>
        <Navbar>
          <Switch>

            <Route 
              key="home" 
              path="/" 
              exact 
              component={Home}
            ></Route>
            <Route 
              key="groceries" 
              path="/groceries" 
              exact 
              component={Groceries}
            ></Route>
            <Route 
              key="recipes" 
              path="/recipes" 
              exact 
              component={Recipes}
            ></Route>
            <Route 
              key="inventory" 
              path="/inventory" 
              exact 
              component={Inventory}
            ></Route>


          </Switch>
        </Navbar>
      </Router>
    </div>
  );
}

export default App;
