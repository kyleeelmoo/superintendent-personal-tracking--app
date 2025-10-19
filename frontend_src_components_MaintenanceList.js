import React, { useState, useEffect } from 'react';

function MaintenanceList() {
  const [tasks, setTasks] = useState([]);
  useEffect(() => {
    fetch('/api/maintenance/tasks')
      .then(res => res.json())
      .then(setTasks);
  }, []);
  return (
    <div>
      <h2>Maintenance Tasks</h2>
      <ul>
        {tasks.map(task => (
          <li key={task.id}>
            <b>{task.name}</b> - Due: {task.due} - Assigned: {task.assignedTo} - Status: {task.status}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default MaintenanceList;