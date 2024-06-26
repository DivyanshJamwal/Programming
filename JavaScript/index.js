const button = document.querySelector('#addTask');
const ADD_TASK = () => {
    // value of input
    const inputValue = document.querySelector("#taskInput");

    const task = inputValue.value;
    //value of Priority

    const selectPriority = document.querySelector('#priority');

    const priority = selectPriority.value;

    //or const priority = document.getElementById('priority').value;

    // Now create a Card 

    if (task) {
        const taskCardContainer = document.querySelector('#task-card');

        const taskCard = document.createElement("div");
        taskCard.classList.add("card");

        taskCard.innerHTML = `
            <h3>${task}</h3>
            <h4>Priority: ${priority}</h4>
        `;

        taskCardContainer.appendChild(taskCard);

        inputValue.value = '';  // Clear input field
    } else {
        alert('Please enter a task');
    }
}

button.addEventListener('click', ADD_TASK);
