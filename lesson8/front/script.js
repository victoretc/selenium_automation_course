document.addEventListener('DOMContentLoaded', function () {
    fetchUsers();
});

function fetchUsers() {
    fetch('http://127.0.0.1:8000/users')
        .then(response => response.json())
        .then(data => {
            const usersList = document.getElementById('usersList');
            usersList.innerHTML = '';
            data.forEach(user => {
                const userItem = document.createElement('li');
                userItem.textContent = `Имя: ${user.name}, Email: ${user.email}`;
                usersList.appendChild(userItem);
            });
        });
}

function addUser() {
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;

    fetch('http://127.0.0.1:8000/users', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name, email })
    })
    .then(response => response.json())
    .then(data => {
        fetchUsers(); // Обновляем список пользователей
        document.getElementById('name').value = '';
        document.getElementById('email').value = '';
    });
}
