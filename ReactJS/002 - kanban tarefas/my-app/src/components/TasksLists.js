import React from "react";
import './TasksLists.css';
import PropTypes from "prop-types";


export default function TasksLists({ title, date, onAddTask, tasks }){
    
    const addTask = () => {
        console.log('tasklist');
        onAddTask("Nova Tarefa", "Pendente");
    };

    return(
        <div className="list">
            <div className="tag-title">
                <h2>{title}</h2>
                <span>{date}</span>
            </div>
            <ul>
                {tasks.map((task) => {
                    return <li key={task.id}>{task.title}</li>
                })}
            </ul>
                <button onClick={addTask}>Add Tarefa</button>
        </div>
    );
};

TasksLists.prototype = {
    title: PropTypes.string.isRequired,
    date: PropTypes.number.isRequired,
    onAddTask: PropTypes.func.isRequired,
    tasks: PropTypes.array.isRequired
};