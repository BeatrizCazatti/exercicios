import React, { useState } from 'react';
import './App.css';
import TasksLists from './components/TasksLists';

const task = {
  id: 0,
  title: "Nova Tarefa",
  state: "to do",
};

let idAccumulate = 0;
const generateId = () => {
  idAccumulate ++;
  return idAccumulate;
};

export default function App() {
  const [tasks, setTasks] = useState([]);


  const addTask = (title, state) => {
    console.log('App')
    const newTask = {
      id: generateId(),
      title,
      state
    };
    setTasks((existingTasks) => {
      return [...existingTasks, newTask];
    });
  };

  return (
    <div className="App">
      <div className="menu"></div>
      <main>
        <header></header>
        <div className='tasks-lists'>
          <TasksLists title="To do" onAddTask={addTask} tasks={tasks} />
          <TasksLists title="In Progress" onAddTask={addTask} tasks={tasks}  />
          <TasksLists title="Done" onAddTask={addTask} tasks={tasks} />
        </div>
      </main>  
    </div>
  );
}

